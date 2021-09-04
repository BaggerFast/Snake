import random
import pygame as pg
from constants import Color


class KeyBoard:
    direction = {
        pg.K_w: (0, -1),
        pg.K_a: (-1, 0),
        pg.K_s: (0, 1),
        pg.K_d: (1, 0),
    }

    @staticmethod
    def check(event):
        if event.type == pg.KEYDOWN and event.key in KeyBoard.direction.keys():
            return KeyBoard.direction[event.key]
        return False

class Snake:
    def __init__(self, game):
        self.game = game
        self.x, self.y = random.randint(0, 60), random.randint(0, 40)
        self.direction = 0, 0

    def draw(self):
        self.x, self.y = self.x + self.direction[0] * 4, self.y + self.direction[1] * 4
        pg.draw.rect(self.game.surface, color=Color.white, rect=(self.x, self.y, self.game.cell_size, self.game.cell_size), width=3)

    def control(self, event: pg.event):
        self.direction = KeyBoard.check(event) if KeyBoard.check(event) else self.direction




