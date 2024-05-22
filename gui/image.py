from .element import Element
import pygame


class Image(Element):
    def __init__(self):
        Element.__init__(self)
        self.image_path = None

    def render(self):
        self.surface = pygame.transform.scale(pygame.image.load(self.image_path), self.size)
