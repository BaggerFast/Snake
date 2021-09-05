import random
import pygame as pg


class Fruit:
    def __init__(self, game):
        self.game = game
        self.x, self.y = self.random_cord()
        self.img = pg.image.load('images/apple.png')

    def random_cord(self):
        return (random.randint(0, 45) * self.game.cell_size) % self.game.width, (
                    random.randint(0, 30) * self.game.cell_size) % self.game.height

    def draw(self):
        self.game.surface.blit(self.img, (self.x, self.y))

    def logic(self):
        if [self.x, self.y] in self.game.snake.body:
            self.game.snake.upgrade = True
            self.x, self.y = self.random_cord()
