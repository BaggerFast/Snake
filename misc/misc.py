import pygame as pg
import dataclasses

from random import randint
from settings import CELL_SIZE, GAME_WIDTH, GAME_HEIGHT


@dataclasses.dataclass
class Coord:
    x: int
    y: int


@dataclasses.dataclass
class Direction:
    key: tuple[pg.key, ...]
    velocity: tuple[int, int]


def get_random_coord() -> Coord:
    return Coord(randint(0, GAME_WIDTH - 1) * CELL_SIZE, randint(0, GAME_HEIGHT - 1) * CELL_SIZE)


