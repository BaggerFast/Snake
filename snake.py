import copy
import dataclasses
import random
import pygame as pg
from constants import Color


class Direction:
    def __init__(self, velocity, key=pg.K_a):
        self.key, self.velocity = key, velocity


class KeyBoard:
    direction = {
        pg.K_w: Direction(velocity=(0, -1), key=pg.K_s),
        pg.K_a: Direction(velocity=(-1, 0), key=pg.K_d),
        pg.K_s: Direction(velocity=(0, 1), key=pg.K_w),
        pg.K_d: Direction(velocity=(1, 0), key=pg.K_a),
    }

    @staticmethod
    def check(event, current: Direction):
        if event.type == pg.KEYDOWN and event.key in KeyBoard.direction.keys() and current.key != event.key:
            new_key = KeyBoard.direction[event.key]
            if current.key != new_key.key:
                return Direction(new_key.velocity, event.key)
        return current


@dataclasses.dataclass
class Cord:
    x: int
    y: int


class Snake:
    def __init__(self, game):
        self.game = game
        self.head = pg.transform.scale(pg.image.load('images/head.png'), (40, 40))
        self.dir = Direction((0, 0))
        self.body: list[Cord] = [Cord(x=random.randint(0, 35) * self.game.cell_size,
                                      y=random.randint(0, 20) * self.game.cell_size)]
        self.upgrade = False

    def process_draw(self):
        self.game.surface.blit(self.head, (self.body[0].x - 5, self.body[0].y - 10))
        for body in self.body[1:]:
            pg.draw.rect(self.game.surface, color=Color.yellow,
                         rect=(body.x, body.y, self.game.cell_size, self.game.cell_size), width=5)

    def process_logic(self):
        last = copy.copy(self.body)

        self.body[0] = Cord(x=(self.body[0].x + self.dir.velocity[0] * self.game.cell_size) % self.game.width,
                            y=(self.body[0].y + self.dir.velocity[1] * self.game.cell_size) % self.game.height)

        self.body = [self.body[0]] + last[:len(last) - 1]

        if self.upgrade:
            self.body.append(last[-1])
            self.upgrade = False

    def check_death(self):
        if self.body[0] in self.body[1:]:
            self.game.scene = self.game.Scenes.game_over(self.game)
            self.game.process_all_logic()

    def process_event(self, event: pg.event):
        self.dir = KeyBoard.check(event, self.dir)
