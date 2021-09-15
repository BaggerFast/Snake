import random
import pygame as pg

from objects.base import Base
from objects.snake import Cord
from objects.text import Text


class Fruit(Base):
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.cord = Cord(*self.random_cord())
        self.text = Text(self.game, f'Length: {self.score}', 50, pg.rect.Rect(10, 10, 30, 30))
        self.img = pg.image.load('images/apple.png')

    def random_cord(self):
        return [(random.randint(0, 35) * self.game.cell_size) % self.game.width,
                (random.randint(0, 20) * self.game.cell_size) % self.game.height]

    def process_draw(self):
        self.game.surface.blit(self.img, (self.cord.x, self.cord.y))
        self.text.process_draw()

    def process_logic(self):
        if self.cord in self.game.scene.snake.body:
            self.game.scene.snake.upgrade = True
            self.cord = Cord(*self.random_cord())
            self.score += 1
            self.text.text = f'Length: {self.score}'
