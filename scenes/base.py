import sys
import pygame as pg

from objects import Objects
from misc import IGenericObject


class Scene(IGenericObject):

    def __init__(self, game):
        self.game = game
        self._objects = Objects()
        self._create_objects()

    # region Public

    # region Implementation of IGenericObject

    def process_event(self, event: pg.event.Event) -> None:
        self._objects.process_event(event)

    def process_logic(self) -> None:
        self._objects.process_logic()

    def process_draw(self, screen: pg.Surface) -> None:
        self._objects.process_draw(screen)

    # endregion

    # endregion

    # region Private

    def _create_objects(self) -> None:
        pass

    # endregion
