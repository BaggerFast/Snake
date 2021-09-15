from objects import Fruit, Snake
import pygame as pg

from scenes.base import Scene


class Main(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.snake = Snake(self.game)
        self.fruit = Fruit(self.game)
        self.objects = [self.snake, self.fruit]

    def additional(self):
        self.snake.check_death()

    def additional_event_check(self, event: pg.event.Event) -> None:
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.game.last_scene = self.game.scene
            self.game.scene = self.game.Scenes.pause(self.game)

