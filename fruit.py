import random
import pygame as pg

from constants import Color
from snake import Body


class Fruit:
    def __init__(self, game):
        self.game = game
        self.x, self.y = random.randint(0, 60) * self.game.cell_size, random.randint(0, 40) * self.game.cell_size

    def draw(self):
        pg.draw.rect(self.game.surface, color=Color.green, rect=(self.x, self.y, self.game.cell_size, self.game.cell_size), width=15)

    def logic(self):
        if self.game.snake.body[0][0] == self.x and self.game.snake.body[0][1] == self.y:
            self.game.snake.body.insert(1, [0, 0])
            self.game.snake.logic()
            self.x, self.y = random.randint(0, 60) * self.game.cell_size, random.randint(0, 40) * self.game.cell_size
