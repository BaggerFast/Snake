import pygame as pg

from scenes.base import Scene


class GameOver(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.fon = pg.image.load('images/game_over.png')
        self.fon_rect = self.fon.get_rect(center=self.surface.get_rect().center)
        self.surface.blit(self.fon, self.fon_rect)

    def additional_event_check(self, event: pg.event.Event) -> None:
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            self.game.scene = self.game.Scenes.main(self.game)
