from copy import copy
from random import choice
import pygame as pg

from settings import Keyboard
from misc import IEventful, ILogical, Direction


class DirectionParser(IEventful, ILogical):

    direction = {
        Keyboard.UP: Direction(velocity=(0, -1), key=Keyboard.DOWN),
        Keyboard.DOWN: Direction(velocity=(0, 1), key=Keyboard.UP),
        Keyboard.LEFT: Direction(velocity=(-1, 0), key=Keyboard.RIGHT),
        Keyboard.RIGHT: Direction(velocity=(1, 0), key=Keyboard.LEFT),
    }

    def __init__(self):
        self.__keyboard_activate = True
        self.__dir = self.get_random_dir()

    # region Public

    # region Implementation of IEventful, ILogical

    def process_event(self, event: pg.event.Event) -> None:
        if event.type != pg.KEYDOWN or not self.__keyboard_activate:
            return
        for key, direction in self.direction.items():
            if event.key in key:
                if key != self.__dir.key:
                    self.__dir = direction
                    self.__keyboard_activate = False
                    return

    def process_logic(self) -> None:
        self.__keyboard_activate = True

    # endregion

    @property
    def velocity(self):
        return copy(self.__dir.velocity)

    def get_random_dir(self) -> Direction:
        return choice(list(self.direction.values()))

    # endregion
