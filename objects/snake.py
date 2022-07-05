from copy import deepcopy
import pygame as pg

from misc import IGenericObject, Coord, get_random_coord
from settings import Color, CELL_SIZE, GAME_WIDTH, GAME_HEIGHT
from .direction_parser import DirectionParser


class Snake(IGenericObject):

    def __init__(self):
        self.__dir_parser = DirectionParser()
        self.__body: list[Coord] = [get_random_coord()]
        self.__update_status = False

    # region Public

    # region Implementation of IGenericObject

    def process_draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, color=Color.YELLOW, rect=(self.__body[0].x, self.__body[0].y, CELL_SIZE, CELL_SIZE))
        for body in self.__body[1:]:
            pg.draw.rect(screen, color=Color.GREEN, rect=(body.x, body.y, CELL_SIZE - 2, CELL_SIZE - 2))

    def process_logic(self) -> None:
        self.__dir_parser.process_logic()

        last = deepcopy(self.__body)

        self.__body[0] = Coord(
            x=(self.__body[0].x + self.__dir_parser.velocity[0] * CELL_SIZE) % (GAME_WIDTH * CELL_SIZE),
            y=(self.__body[0].y + self.__dir_parser.velocity[1] * CELL_SIZE) % (GAME_HEIGHT * CELL_SIZE)
        )

        self.__body = self.__body[0:1] + last[:-1]

        if self.__update_status:
            self.__body.append(last[-1])
            self.__update_status = False

    def process_event(self, event: pg.event.Event) -> None:
        self.__dir_parser.process_event(event)

    # endregion

    @property
    def body(self) -> list[Coord]:
        return deepcopy(self.__body)

    def check_death(self) -> bool:
        return self.__body[0] in self.__body[1:]

    def update_nail(self) -> None:
        self.__update_status = True

    # endregion

