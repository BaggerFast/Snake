import pygame as pg
import sys
from constants import Color
from fruit import Fruit
from snake import Snake


class Game:
    cell_size = 28
    resolution = width, height = 45 * cell_size, 30 * cell_size
    surface = pg.display.set_mode(resolution)
    pg.display.set_caption('Snake')
    fon = pg.image.load('images/fon.jpg').convert()
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
        def draw_grid():
            for i in range((self.width // self.cell_size)):
                pg.draw.line(self.surface, Color.gray, (i * self.cell_size, 0), (i * self.cell_size, self.height), 1)
            for i in range((self.height // self.cell_size)):
                pg.draw.line(self.surface, Color.gray, (0, i * self.cell_size), (self.width, i * self.cell_size), 1)

        self.surface.blit(self.fon, (0, 0))
        draw_grid()
        self.fruit.draw()
        self.snake.draw()

    def finish(self):
        ...

    def start(self):
        while not self.game_over:
            for event in pg.event.get():
                self.event_check(event)
            self.fruit.logic()
            self.snake.logic()
            self.draw_to_screen()
            pg.display.update()
            self.snake.check_death()
            self.time.tick(self.__FPS)
        self.finish()
