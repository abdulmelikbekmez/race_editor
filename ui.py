from typing import Dict 
from pygame.math import Vector2
from pygame.surface import Surface
from appMode import AppMode
from border import Border
from car import Car
from config import BELOW_SCREEN, WIDTH
from drawable import Drawable
from uiElement import UIElement
from textRenderer import TextRenderer
import pygame as pg


class UI:
    COLOR = (128,128, 128)
    def __init__(self, screen:Surface) -> None:
        self.__screen = screen
        self.__mode_app = AppMode.PLACE_BORDER
        self.elements : Dict[UIElement, AppMode] = {}
        self.__add_element(Car(self.__screen, self.get_pos_element(),is_static=True),AppMode.PLACE_CAR)
        self.__add_element_border()
        self.renderer_text = TextRenderer(screen,Vector2(BELOW_SCREEN),self.__mode_app.value)

    def draw(self):
        self.__draw_buttons()
        self.renderer_text.draw()


    def get_mode(self):
        return self.__mode_app

    def update(self):
        if self.__mode_app is AppMode.RUN:
            return

        for el, mode in self.elements.items():
            if el.is_clicked():
                self.__set_mode(mode)
    
    def get_pos_element(self):
        l = len(self.elements)
        padding_x = 15 + UIElement.WIDTH / 2
        return Vector2(WIDTH - padding_x - ( l * (padding_x + UIElement.WIDTH/2)), UIElement.WIDTH / 2)

    def __add_element(self, drawable: Drawable, mode: AppMode):
        pos = self.get_pos_element()
        element = UIElement(self.__screen,pos,self.COLOR,drawable)
        self.elements[element] = mode

    def __add_element_border(self):
        border = Border.for_ui(self.__screen, self.get_pos_element(),45, UIElement.WIDTH/2)
        element = UIElement(self.__screen, self.get_pos_element(),self.COLOR, border)
        self.elements[element] = AppMode.PLACE_BORDER

    def __draw_buttons(self):
        if self.__mode_app is AppMode.RUN:
            return
        for el in self.elements:
            el.draw()

    def __set_mode(self, mode:AppMode):
        self.__mode_app = mode
        self.renderer_text.set_text(self.__mode_app.value)

    def __change_mode_event(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_e]:
            self.__set_mode(AppMode.PLACE_BORDER)
        elif keys[pg.K_r]:
            self.__set_mode(AppMode.RUN)

    def event(self):
        self.__change_mode_event()


