from base_scene import Scene
import pygame as pg


class Pause(Scene):

    def additional_event_check(self, event: pg.event.Event) -> None:
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.game.scene = self.game.last_scene
