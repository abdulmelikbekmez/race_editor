from typing import List
from pygame.math import Vector2
from pygame.surface import Surface
import pygame as pg
from border import Border
from ray import Ray
from rectangle import Rectangle
from uiElement import UIElement


class Car(Rectangle):

    WIDTH = 20
    HEIGHT = 40
    COLOR = (255, 0, 0)

    def __init__(
        self,
        screen: Surface,
        pos: Vector2,
        angle_heading: float = -90,
        is_static: bool = False,
    ) -> None:
        super().__init__(
            screen, pos, self.COLOR, angle_heading, self.WIDTH, self.HEIGHT
        )
        self.POS_INITIAL = pos.copy()
        self.velocity = 0
        self.list_ray = [
            Ray(self.screen, self.vector_up, self.pos),
            Ray(self.screen, self.vector_right, self.pos),
            Ray(self.screen, self.vector_left, self.pos),
            Ray(self.screen, self.vector_right_up, self.pos),
            Ray(self.screen, self.vector_left_up, self.pos),
            Ray(self.screen, self.vector_rear, self.pos),
        ]
        self.is_static = is_static

    def event_handler(self):
        keys = pg.key.get_pressed()

        self.update_angle_heading(keys[pg.K_RIGHT] - keys[pg.K_LEFT])
        self.velocity += (keys[pg.K_UP] - keys[pg.K_DOWN]) * 0.1

    def update(self, list_border: List[Border]):
        self.pos += self.vector_up * self.velocity
        for ray in self.list_ray:
            ray.update(list_border)

    def is_pressed(self):
        pos_mouse = Vector2(pg.mouse.get_pos())
        if UIElement.is_collides(pos_mouse):
            return False

        distance = pos_mouse - self.pos
        return distance.length() < self.HEIGHT

    def draw(self):
        super().draw()
        if self.is_static:
            return
        for ray in self.list_ray:
            ray.draw()
