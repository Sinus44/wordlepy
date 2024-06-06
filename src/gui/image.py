import pygame

from .element import Element


class Image(Element):
    def __init__(self):
        Element.__init__(self)
        self.image_path = None

    def render(self):
        self.surface = pygame.transform.scale(pygame.image.load(self.image_path), self.size)
        self._post_render()
