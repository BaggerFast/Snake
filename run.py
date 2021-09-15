from game import Game
import pygame as pg


def main():
    pg.display.init()
    pg.font.init()
    game = Game()
    game.main_loop()


if __name__ == '__main__':
    main()