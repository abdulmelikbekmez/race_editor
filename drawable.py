from abc import ABC, abstractmethod
from pygame.math import Vector2
from pygame.surface import Surface

class Drawable(ABC):

    def __init__(self,screen:Surface, pos:Vector2) -> None:
        super().__init__()
        self.pos = pos
        self.screen = screen

    @abstractmethod 
    def draw(self):
        pass
