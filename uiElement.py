import pygame as pg
from typing import Tuple
from pygame.math import Vector2
from pygame.surface import Surface
from drawable import Drawable
from rectangle import Rectangle


class UIElement(Rectangle):
    WIDTH = 100
    HEIGHT = 100

    def __init__(
        self,
        screen: Surface,
        pos: Vector2,
        color: Tuple[int, int, int],
        drawable: Drawable,
    ):
        super().__init__(screen, pos, color)
        self.drawable = drawable
        self.drawable.pos = self.pos

    def draw(self):
        super().draw()
        self.drawable.draw()

    @classmethod
    def is_collides(cls, pos: Vector2):
        return pos.y <= cls.HEIGHT

    def is_clicked(self):
        if pg.mouse.get_pressed()[0]:
            x, y = pg.mouse.get_pos()
            x_rect = self.point_up_left.x
            y_rect = self.point_up_left.y
            if x_rect < x < x_rect + self.WIDTH and y_rect < y < y_rect + self.HEIGHT:
                return True
        return False
