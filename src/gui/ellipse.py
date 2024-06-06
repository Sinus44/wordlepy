import pygame

from .element import Element
from .rect import RectStyle
from .style import Style


class EllipseStyle(Style):
    COPY_MAP = {
        "rect": {
            "color": "color",
            "outline_enable": "outline_enable",
            "outline_color": "outline_color",
            "outline_width": "outline_width"
        }
    }

    def __init__(self):
        Style.__init__(self)
        self.copy_style_by_map(RectStyle(), self.COPY_MAP["rect"])


class Ellipse(Element):
    def __init__(self):
        Element.__init__(self)

        # region Properties

        self.style = EllipseStyle()

        # endregion

    def render(self):
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.update_style_state()

        pygame.draw.ellipse(self.surface, self.style.get_property("color"), [0, 0, *self.size])
        if self.style.get_property("outline_enable"):
            pygame.draw.ellipse(self.surface, self.style.get_property("outline_color"), [0, 0, *self.size],
                                self.style.get_property("outline_width"))

        self._post_render()

    def collide(self, position):
        dx = self.size[0] / 2
        dy = self.size[1] / 2

        return (((position[0] - self.position[0] - self.size[0] / 2) ** 2) / (dx ** 2) + (
                (position[1] - self.position[1] - self.size[1] / 2) ** 2) / (dy ** 2)) < 1
