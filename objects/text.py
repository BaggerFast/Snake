import pygame as pg

from settings import Color, PathCtrl
from misc.interfaces import IDrawable


class Text(IDrawable):

    def __init__(self, text: str = "", size: int = 0, rect: pg.rect = pg.rect.Rect(0, 0, 0, 0), color=Color.WHITE,
                 font=PathCtrl.get_asset_path('fonts/main.ttf')):
        self.__surface: pg.Surface
        self.__size = size
        self.__color = color
        self.__rect = rect
        self.__font = pg.font.Font(font, self.__size)

        self.__text = ""
        self.text = text

    # region Public

    # region Implementation of IDrawable

    def process_draw(self, screen: pg.Surface) -> None:
        screen.blit(self.__surface, self.rect)

    # endregion

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str) -> None:
        self.__text = text if text else self.__text
        self.__surface = self.__font.render(self.__text, False, self.__color)
        top_left = self.__rect.topleft
        self.rect = self.__surface.get_rect()
        self.rect.topleft = top_left

    # endregion
