from game import Game
import pygame as pg


def main():
    pg.display.init()
    game = Game()
    game.start()


if __name__ == '__main__':
    main()