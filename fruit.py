import random
import pygame as pg

from snake import Cord


class Fruit:
    def __init__(self, game):
        self.game = game
        self.cord = Cord(*self.random_cord())
        self.img = pg.image.load('images/apple.png')

    def random_cord(self):
        return [(random.randint(0, 45) * self.game.cell_size) % self.game.width,
                (random.randint(0, 30) * self.game.cell_size) % self.game.height]

    def draw(self):
        self.game.surface.blit(self.img, (self.cord.x, self.cord.y))

    def logic(self):
        if self.cord in self.game.snake.body:
            self.game.snake.upgrade = True
            self.cord = Cord(*self.random_cord())
