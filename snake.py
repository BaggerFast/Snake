import random
import sys
from copy import copy
import pygame as pg
from constants import Color


class Direction:
    def __init__(self, velocity, key=pg.K_a):
        self.key, self.velocity = key, velocity


class KeyBoard:
    direction = {
        pg.K_w: Direction(velocity=(0, -1), key=pg.K_s),
        pg.K_a: Direction(velocity=(-1, 0), key=pg.K_d),
        pg.K_s: Direction(velocity=(0, 1), key=pg.K_w),
        pg.K_d: Direction(velocity=(1, 0), key=pg.K_a),
    }

    @staticmethod
    def check(event, current: Direction):
        if event.type == pg.KEYDOWN and event.key in KeyBoard.direction.keys() and current.key != event.key:
            new_key = KeyBoard.direction[event.key]
            if current.key != new_key.key:
                return Direction(new_key.velocity, event.key)
        return current


class Snake:
    def __init__(self, game):
        self.game = game
        self.head = pg.transform.scale(pg.image.load('images/head.png'), (40, 40))
        self.x, self.y = random.randint(0, 45) * self.game.cell_size, random.randint(0, 30) * self.game.cell_size
        self.dir = Direction((0, 0))
        self.body = [[self.x, self.y]]
        self.upgrade = False

    def draw(self):
        self.game.surface.blit(self.head, (self.body[0][0]-5, self.body[0][1]-10))
        for body in self.body[1:]:
            pg.draw.rect(self.game.surface, color=Color.yellow, rect=(body[0], body[1], self.game.cell_size, self.game.cell_size), width=5)

    @property
    def head_(self):
        return self.body[0]

    @property
    def nail(self):
        return self.body[1:]

    def logic(self):
        last = [row[:] for row in self.body]

        self.head_[0], self.head_[1] = (self.head_[0] + self.dir.velocity[0] * self.game.cell_size) % self.game.width, \
                                       (self.head_[1] + self.dir.velocity[1] * self.game.cell_size) % self.game.height

        self.body = [self.body[0]] + last[:len(last)-1]

        if self.upgrade:
            self.body.append(last[-1])
            self.upgrade = False

    def check_death(self):
        if self.head_ in self.nail:
            pg.time.delay(10000)
            sys.exit(0)

    def control(self, event: pg.event):
        self.dir = KeyBoard.check(event, self.dir)
        print(self.dir.key, KeyBoard.check(event, self.dir).key)




