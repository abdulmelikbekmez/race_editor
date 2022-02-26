import math
from typing import Tuple
from pygame.color import Color
from pygame.math import Vector2
from pygame.surface import Surface
from pygame.draw import line, circle
from drawable import Drawable


class Border(Drawable):

    COLOR = Color(127, 127, 127)

    def __init__(self, screen: Surface, start: Vector2, finish: Vector2) -> None:
        super().__init__(screen, ((start + finish) / 2))
        self.start = start
        self.finish = finish

    def __str__(self) -> str:
        return f"start => {self.start}\nmiddle => {self.pos}\nfinish => {self.finish}"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def direction(self):
        v = self.finish - self.start
        return v.normalize() if v.length() != 0 else v

    @property
    def lenght(self):
        v = self.finish - self.start
        return v.length()

    @property
    def vector(self):
        return self.direction * self.lenght

    @classmethod
    def for_ui(cls, screen: Surface, pos: Vector2, angle_heading: float, length: float):
        v = Vector2(
            math.cos(math.radians(angle_heading)), math.sin(math.radians(angle_heading))
        )
        start = pos + (v * length)
        finish = pos + (-v * length)
        return cls(screen, start, finish)

    @classmethod
    def from_mouse(cls, screen: Surface, pos: Tuple[int, int]):
        start = Vector2(pos)
        finish = Vector2(pos)
        return cls(screen, start, finish)

    def update_finish(self, pos: Tuple[int, int]):
        self.finish.update(pos)
        self.pos = (self.start + self.finish) / 2

    def draw(self):
        line(self.screen, self.COLOR, self.start, self.finish, 5)
        circle(self.screen, (128, 0, 0), self.start, 5)
        circle(self.screen, (128, 0, 0), self.finish, 5)
        circle(self.screen, (128, 0, 0), self.pos, 5)
