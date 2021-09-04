import random
import sys
from copy import copy

import pygame as pg
from constants import Color


class KeyBoard:
    direction = {
        pg.K_w: (0, -1, pg.K_s),
        pg.K_a: (-1, 0, pg.K_d),
        pg.K_s: (0, 1, pg.K_w),
        pg.K_d: (1, 0, pg.K_a),
    }

    @staticmethod
    def check(event, snake, current):
        if event.type == pg.KEYDOWN and event.key in KeyBoard.direction.keys():
            data = {
                (-1, 0): pg.K_a,
                (0, 1): pg.K_s,
                (0, -1): pg.K_w,
                (1, 0): pg.K_d,
            }
            if current in data:
                current = data[current]
            if current != KeyBoard.direction[event.key][2] or len(snake.body) == 1:
                return KeyBoard.direction[event.key][:2]
        return False


class Body:
    def __init__(self, coord, dir):
        self.x, self.y = coord
        self.dir = dir


class Snake:
    def __init__(self, game):
        self.game = game
        self.x, self.y = random.randint(0, 60) * self.game.cell_size, random.randint(0, 40) * self.game.cell_size
        self.direction = 0, 0
        self.body = [[self.x, self.y]]

    def draw(self):
        pg.draw.rect(self.game.surface, color=Color.white,
                     rect=(self.body[0][0], self.body[0][1], self.game.cell_size, self.game.cell_size), width=15)
        for body in self.body[1::]:
            pg.draw.rect(self.game.surface, color=Color.red, rect=(body[0], body[1], self.game.cell_size, self.game.cell_size), width=15)

    def logic(self):
        last = copy(self.body[0])
        self.body[0][0], self.body[0][1] = self.body[0][0] + self.direction[0] * self.game.cell_size, self.body[0][1] + self.direction[1] * self.game.cell_size
        for i in range(1, len(self.body)):
            tmp = copy(self.body[i])
            self.body[i] = last
            last = tmp
        if self.body[0] in self.body[1:]:
            sys.exit(0)

    def control(self, event: pg.event):
        self.direction = KeyBoard.check(event, self, self.direction) if KeyBoard.check(event, self, self.direction) else self.direction




