import pygame as pg


class Scene:
    objects = []

    def __init__(self, game):
        self.game = game
        self.screen: pg.Surface = self.game.surface

    def process_event(self, event: pg.event.Event) -> None:
        for item in self.objects:
            item.process_event(event)
        self.additional_event_check(event)

    def create_obj(self) -> list:
        pass

    def process_logic(self) -> None:
        for item in self.objects:
            item.process_logic()
        self.additional_logic()

    def process_draw(self) -> None:
        for item in self.objects:
            item.process_draw()
        self.additional_draw()

    def additional_event_check(self, event: pg.event.Event) -> None:
        ...

    def additional_logic(self) -> None:
        pass

    def additional_draw(self) -> None:
        ...

    def additional(self):
        ...
