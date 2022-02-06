
from pygame.font import SysFont
from pygame.math import Vector2
from pygame.surface import Surface
from drawable import Drawable


class TextRenderer(Drawable):
    def __init__(self,screen : Surface, pos: Vector2 , text:str = "") -> None:
        super().__init__(screen, pos)
        self.__font = SysFont("firamono", 24)
        self.__text = text
        self.__surface_text = self.__font.render(self.__text,True,(128,0,0))
        self.__rect_text = self.__surface_text.get_rect(center=pos)

    def set_text(self, text:str):
        self.__text = text
        self.__surface_text = self.__font.render(self.__text,True,(128,0,0))
        self.__rect_text = self.__surface_text.get_rect(center=self.pos)

    def draw(self):
        self.screen.blit(self.__surface_text,self.__rect_text )


