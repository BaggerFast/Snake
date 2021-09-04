import pygame as pg
import sys
from constants import Color
from snake import Snake


class Game:
    cell_size = 15
    resolution = width, height = 60 * cell_size, 40 * cell_size
    surface = pg.display.set_mode(resolution)
    pg.display.set_caption('Snake')
    __FPS = 60
    game_over = False
    time: pg.time = pg.time.Clock()

    def __init__(self):
        self.snake = Snake(self)

    def event_check(self, event):
        if event.type == pg.QUIT:
            sys.exit(0)
        self.snake.control(event)

    def draw_to_screen(self):
        self.surface.fill(Color.black)
        self.snake.draw()

    def finish(self):
        ...

    def start(self):
        while not self.game_over:
            for event in pg.event.get():
                self.event_check(event)
            self.draw_to_screen()
            pg.display.update()
            self.time.tick(self.__FPS)
        self.finish()
