import pygame as pg
import sys
from constants import Color
from fruit import Fruit
from snake import Snake


class Game:
    cell_size = 20
    resolution = width, height = 60 * cell_size, 40 * cell_size
    surface = pg.display.set_mode(resolution)
    pg.display.set_caption('Snake')
    __FPS = 20
    game_over = False
    time: pg.time = pg.time.Clock()

    def __init__(self):
        self.snake = Snake(self)
        self.fruit = Fruit(self)

    def event_check(self, event):
        if event.type == pg.QUIT:
            sys.exit(0)
        self.snake.control(event)

    def draw_to_screen(self):

        # for i in range((self.width // self.cell_size)):
        #     pg.draw.line(self.surface, Color.white, (i * self.cell_size, 0), (i * self.cell_size, self.height), 1)
        # for i in range((self.height // self.cell_size)):
        #     pg.draw.line(self.surface, Color.white, (0, i * self.cell_size), (self.width, i * self.cell_size), 1)
        self.surface.fill(Color.black)
        self.snake.draw()
        self.fruit.draw()

    def finish(self):
        ...

    def start(self):
        while not self.game_over:
            for event in pg.event.get():
                self.event_check(event)
            self.snake.logic()
            self.fruit.logic()
            self.draw_to_screen()
            pg.display.update()
            self.time.tick(self.__FPS)
        self.finish()
