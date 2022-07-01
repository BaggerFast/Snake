import pygame as pg

from settings import CELL_SIZE, Color
from misc import get_random_coord, Coord, IDrawable


class Fruit(IDrawable):

    def __init__(self):
        self.__coord = get_random_coord()

    # region Public

    # region Implementation of IDrawable

    def process_draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, color=Color.RED, rect=(self.__coord.x, self.__coord.y, CELL_SIZE, CELL_SIZE))

    # endregion

    def has_collision(self, snake_body: list[Coord]) -> bool:
        status = self.__coord in snake_body
        if status:
            self.__coord = get_random_coord()
        return status

    # endregion
