from typing import List, Union

from pygame.event import Event
from appMode import AppMode
from border import Border
import pygame as pg
from pygame.math import Vector2
from car import Car
from config import HEIGHT, WIDTH
from settingManager import SettingsManager
from ui import UI
from uiElement import UIElement


class App:
    FPS = 60
    BACKGROUND_COLOR = pg.color.Color(0, 0, 0)

    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.running = True
        self.clock = pg.time.Clock()
        self.list_border: List[Border] = SettingsManager.init_borders(self.screen)
        self.current_border: Union[Border, None] = None
        self.car: Union[Car, None] = None
        self.ui = UI(self.screen)

    @property
    def mode(self):
        return self.ui.get_mode()

    def main(self):

        while self.running:
            self.__event_handler()

            self.screen.fill(self.BACKGROUND_COLOR)

            self.__update()
            self.__draw()

            pg.display.flip()
            self.clock.tick(self.FPS)
            pg.display.set_caption(f"FPS => {self.clock.get_fps()}")

    def __event_handler(self):
        self.ui.event()
        self.event_car()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False

            self.event_border(event)

    def event_border(self, event: Event):
        if self.mode is not AppMode.PLACE_BORDER:
            self.current_border = None
            return

        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                pos_mouse = pg.mouse.get_pos()
                if not UIElement.is_collides(Vector2(pos_mouse)):
                    self.current_border = Border.from_mouse(self.screen, pos_mouse)
                    self.list_border.append(self.current_border)

        if event.type == pg.MOUSEBUTTONUP:
            self.current_border = None

        if not self.current_border:
            return
        self.current_border.update_finish(pg.mouse.get_pos())

    def event_car(self):
        if self.car is None and self.mode is AppMode.PLACE_CAR:
            pos_mouse = pg.mouse.get_pos()
            if pg.mouse.get_pressed()[0] and not UIElement.is_collides(
                Vector2(pos_mouse)
            ):
                self.car = Car(self.screen, Vector2(pos_mouse))

        if self.car and self.mode is AppMode.PLACE_CAR:
            if pg.mouse.get_pressed()[2] and self.car.is_pressed():
                self.car = None

        if self.mode is not AppMode.RUN or self.car is None:
            return

        self.car.event_handler()

    def __del__(self):
        SettingsManager.write_borders(self.list_border)
        pg.quit()

    def __update(self):
        self.__update_car()
        self.ui.update()

    def __update_car(self):
        if self.mode is not AppMode.RUN or self.car is None:
            return
        self.car.update(self.list_border)

    def __draw(self):
        for border in self.list_border:
            border.draw()
        self.ui.draw()
        self.__draw_car()

    def __draw_car(self):
        if self.car is None:
            return
        self.car.draw()
