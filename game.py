import pygame as pg
import sys

from scenes import MainScene
from settings import Color, FPS, GAME_RESOLUTION, PathCtrl


class Game:

    # region Pygame setup

    pg.display.init()
    pg.font.init()
    pg.display.set_caption('Snake')
    pg.display.set_icon(pg.transform.scale(pg.image.load(PathCtrl.get_img_path('logo.png')), (90, 90)))

    # endregion

    def __init__(self):
        self.screen = pg.display.set_mode(GAME_RESOLUTION)
        self.scene = MainScene(self)
        self.last_scene = self.scene
        self.__clock = pg.time.Clock()

    # region Private

    def __process_all_events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit(0)
            self.scene.process_event(event)
            self.scene.additional_event(event)

    def __process_all_draw(self) -> None:
        self.screen.fill(Color.BLACK)
        self.scene.process_draw(self.screen)
        self.scene.additional_draw(self.screen)
        pg.display.flip()

    def __process_all_logic(self) -> None:
        self.scene.process_logic()
        self.scene.additional_logic()

    # endregion

    # region Public

    def main_loop(self) -> None:
        while True:
            self.__process_all_logic()
            self.__process_all_events()
            self.__process_all_draw()
            self.__clock.tick(FPS)

    # endregion
