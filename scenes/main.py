import pygame as pg

from .base import Scene
from objects import Fruit, Snake, Text


class MainScene(Scene):

    def __init__(self, game):
        self.score = 0
        self.text = Text(f'Length: {self.score}', 50, pg.rect.Rect(10, 10, 30, 30))
        super().__init__(game)

    # region Private

    def _create_objects(self) -> None:
        self.snake = Snake()
        self.fruit = Fruit()
        self._objects.append(self.snake, self.fruit, self.text)

    # endregion

    # region Public

    def additional_logic(self) -> None:
        if self.fruit.has_collision(self.snake.body):
            self.score += 1
            self.text.text = f'Length: {self.score}'
            self.snake.update_nail()
        elif self.snake.check_death():
            from .game_over import GameOverScene
            self.game.last_scene = self.game.scene
            self.game.scene = GameOverScene(self.game)

    def additional_event(self, event: pg.event.Event) -> None:
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            from .pause import PauseScene
            self.game.last_scene = self.game.scene
            self.game.scene = PauseScene(self.game)

    # endregion
