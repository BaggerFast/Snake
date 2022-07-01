import os
import pygame as pg

from abc import ABC
from typing import Final

CELL_SIZE: Final = 50
FPS: Final = 10

GAME_WIDTH: Final = 16
GAME_HEIGHT: Final = 16
GAME_RESOLUTION: Final = (GAME_WIDTH * CELL_SIZE, GAME_HEIGHT * CELL_SIZE)


class Color:
    WHITE: Final = pg.Color('white')
    BLACK: Final = pg.Color('black')
    GREEN: Final = pg.Color('green')
    RED: Final = (255, 36, 0)
    GRAY: Final = (50, 50, 50)
    YELLOW: Final = (255, 186, 0)


class PathCtrl(ABC):
    BASE: Final = os.path.dirname(os.path.abspath(__file__))
    ASSET: Final = os.path.join(BASE, 'assets')
    IMAGE: Final = os.path.join(ASSET, 'images')

    @classmethod
    def get_img_path(cls, path: str) -> str:
        return os.path.join(cls.IMAGE, path)

    @classmethod
    def get_asset_path(cls, path: str) -> str:
        return os.path.join(cls.ASSET, path)


class Keyboard(ABC):
    RIGHT: Final = (pg.K_d, pg.K_RIGHT)
    LEFT: Final = (pg.K_a, pg.K_LEFT)
    UP: Final = (pg.K_w, pg.K_UP)
    DOWN: Final = (pg.K_s, pg.K_DOWN)
    ENTER: Final = (pg.K_SPACE, pg.K_RETURN)
