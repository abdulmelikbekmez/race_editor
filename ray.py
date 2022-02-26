import math
from typing import List
from pygame.draw import line
from pygame.math import Vector2
from pygame.surface import Surface
from border import Border

from drawable import Drawable
from linearAlgebra import get_inverse_matrix_2


class Ray(Drawable):
    HEIGHT_MAX = 250

    def __init__(self, screen: Surface, direction: Vector2, pos: Vector2) -> None:
        super().__init__(screen, pos)
        self.direction = direction
        self.__height = self.HEIGHT_MAX

    @property
    def angle(self):
        return math.degrees(math.atan2(self.direction.y, self.direction.x))

    def get_height(self) -> float:
        return self.__height

    def draw(self):
        line(
            self.screen,
            (127, 0, 0),
            self.pos,
            self.pos + self.direction * self.get_height(),
            5,
        )

    def update(self, list_border: List[Border]):
        list_height = []
        for border in list_border:
            list_height.append(self.__get_height_from_border(border))
        h = min(list_height) if list_height else self.HEIGHT_MAX
        self.__height = h if h < self.HEIGHT_MAX else self.HEIGHT_MAX

    def __get_height_from_border(self, border: Border):
        inverse = get_inverse_matrix_2(self.direction, -border.direction)
        if inverse is None:
            return self.HEIGHT_MAX
        b = border.start - self.pos
        v1, v2 = inverse
        length_ray = v1.dot(b)
        length_border = v2.dot(b)
        if (not (0 <= length_border <= border.lenght)) or length_ray <= 0:
            return self.HEIGHT_MAX

        return length_ray
