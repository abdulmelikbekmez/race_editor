from typing import Tuple
from pygame.draw import line
from pygame.math import Vector2
from pygame.surface import Surface
import math
from drawable import Drawable


class Rectangle(Drawable):
    def __init__(
        self,
        screen: Surface,
        pos: Vector2,
        color: Tuple[int, int, int],
        angle_heading: float = -90,
        width: float = 100,
        height: float = 100,
    ) -> None:
        super().__init__(screen, pos)
        self.__angle_heading = angle_heading
        self.COLOR = color
        self.WIDTH = width
        self.HEIGHT = height

        self.vector_left = self.__get_vector_from_angle(self.__angle_heading - 90)
        self.vector_left_up = self.__get_vector_from_angle(self.__angle_heading - 45)
        self.vector_right = self.__get_vector_from_angle(self.__angle_heading + 90)
        self.vector_right_up = self.__get_vector_from_angle(self.__angle_heading + 45)
        self.vector_up = self.__get_vector_from_angle(self.__angle_heading)
        self.vector_rear = self.__get_vector_from_angle(self.__angle_heading + 180)

    def update_angle_heading(self, angle: float):
        self.__angle_heading += angle
        self.vector_left.update(self.__angle_to_coord(self.__angle_heading - 90))
        self.vector_left_up.update(self.__angle_to_coord(self.__angle_heading - 45))
        self.vector_right.update(self.__angle_to_coord(self.__angle_heading + 90))
        self.vector_right_up.update(self.__angle_to_coord(self.__angle_heading + 45))
        self.vector_up.update(self.__angle_to_coord(self.__angle_heading))
        self.vector_rear.update(self.__angle_to_coord(self.__angle_heading + 180))

    @property
    def point_rear_left(self):
        return (
            self.pos
            + self.vector_left * self.WIDTH / 2
            + self.vector_rear * self.HEIGHT / 2
        )

    @property
    def point_rear_right(self):
        return (
            self.pos
            + self.vector_right * self.WIDTH / 2
            + self.vector_rear * self.HEIGHT / 2
        )

    @property
    def point_up_left(self):
        return (
            self.pos
            + self.vector_left * self.WIDTH / 2
            + self.vector_up * self.HEIGHT / 2
        )

    @property
    def point_up_right(self):
        return (
            self.pos
            + self.vector_right * self.WIDTH / 2
            + self.vector_up * self.HEIGHT / 2
        )

    def __get_vector_from_angle(self, angle: float):
        return Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle)))

    @staticmethod
    def __angle_to_coord(angle: float):
        return math.cos(math.radians(angle)), math.sin(math.radians(angle))

    def draw(self):

        line(self.screen, self.COLOR, self.point_rear_left, self.point_up_left)
        line(self.screen, self.COLOR, self.point_rear_right, self.point_up_right)

        line(self.screen, self.COLOR, self.point_rear_left, self.point_rear_right)
        line(self.screen, self.COLOR, self.point_up_left, self.point_up_right)
