import sys
import pygame as pg
from constants import Color
from scenes import *


class Game:
    cell_size = 28
    resolution = width, height = 35 * cell_size, 20 * cell_size
    surface = pg.display.set_mode(resolution)
    pg.display.set_caption('Snake')
    fon = pg.image.load('images/fon.jpg')
    pg.display.set_icon(pg.transform.scale(pg.image.load('images/head.png'), (70, 70)))

    class Scenes:
        main = Main
        pause = Pause
        game_over = GameOver

    def __init__(self):
        self.scene: Scene = Main(self)
        self.__game_over = False
        self.__FPS = 20
        self.__clock = pg.time.Clock()
        self.last_scene = self.scene

    def main_loop(self) -> None:
        while not self.__game_over:
            self.__process_all_events()
            self.process_all_logic()
            self.process_all_draw()
            self.scene.additional()
            self.__clock.tick(self.__FPS)

    def process_all_logic(self):
        self.scene.process_logic()

    def process_all_draw(self):
        if type(self.scene) == self.Scenes.main:
            self.surface.blit(self.fon, (0, 0))
            for i in range((self.width // self.cell_size)):
                pg.draw.line(self.surface, Color.gray, (i * self.cell_size, 0), (i * self.cell_size,
                                                                                 self.height), 1)
            for i in range((self.height // self.cell_size)):
                pg.draw.line(self.surface, Color.gray, (0, i * self.cell_size), (self.width,
                                                                                 i * self.cell_size), 1)

        self.scene.process_draw()
        pg.display.flip()

    def __process_all_events(self) -> None:
        for event in pg.event.get():
            self.scene.process_event(event)
            if event.type == pg.QUIT:
                sys.exit(0)