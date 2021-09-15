import pygame as pg


class Text:
    def __init__(self, game, text: str = "", size: int = 0, rect: pg.Rect = pg.rect.Rect(0, 0, 0, 0),
                 color=pg.Color(255, 255, 255), font='fonts/main.ttf'):
        self.game = game
        self.rect = rect
        self.__pos = rect
        self.size = size
        self.__color = color
        self.font = pg.font.Font(font, self.size)
        self.__text: str
        self.text = text
        self.surface: pg.Surface

    @property
    def pos(self):
        return self.__pos

    @property
    def text(self):
        return self.__text

    @property
    def color(self):
        return self.color

    @text.setter
    def text(self, text: str):
        self.__text = text if text else self.__text
        self.surface = self.font.render(self.__text, False, self.__color)
        topleft = self.rect.topleft
        self.rect = self.surface.get_rect()
        self.rect.topleft = topleft

    def draw(self) -> None:
        self.game.surface.blit(self.surface, self.rect)
