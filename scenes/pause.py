import pygame as pg

from settings import PathCtrl
from .base import Scene


class PauseScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.fon = pg.image.load(PathCtrl.get_img_path('pause.png'))
        self.fon_rect = self.fon.get_rect(center=self.game.screen.get_rect().center)

    # region Public

    def additional_draw(self, screen: pg.Surface) -> None:
        self.game.last_scene.process_draw(screen)
        self.game.last_scene.additional_draw(screen)
        screen.blit(self.fon, self.fon_rect)

    def additional_event(self, event: pg.event.Event) -> None:
        if event.type == pg.KEYDOWN and event.key in (pg.K_ESCAPE, pg.K_SPACE):
            self.game.scene = self.game.last_scene

    # endregion
