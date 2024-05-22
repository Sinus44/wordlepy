import pygame

from .element import Element
from .style import Style


class RectStyle(Style):
    """Style for RECT-Element"""

    def __init__(self):
        Style.__init__(self)

        self.create_property("normal", "color", (30, 30, 30))
        self.create_property("normal", "outline_enable", False)
        self.create_property("normal", "outline_width", 3)
        self.create_property("normal", "outline_color", (100, 100, 100))


class Rect(Element):
    def __init__(self):
        Element.__init__(self)

        # region Properties

        self.style = RectStyle()

        # endregion

        self.render()

    def render(self):
        self.surface = pygame.Surface(self.size)
        self.update_style_state()
        self.surface.fill(self.style.get_property("color"))

        if self.style.get_property("outline_enable"):
            pygame.draw.rect(self.surface, self.style.get_property("outline_color"), (0, 0, *self.size),
                             self.style.get_property("outline_width"))
