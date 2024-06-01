"""Package for buttons"""

import pygame

from .element import Element
from .label import Label, LabelStyle
from .rect import Rect, RectStyle
from .style import Style


class ButtonStyle(Style):
    COPY_MAP = {
        "label": {
            "font_color": "font_color",
            "font_name": "font_name",
            "font_size": "font_size",
            "horizontal_align": "horizontal_align",
            "vertical_align": "vertical_align",
            "font_bold": "font_bold",
            "font_italic": "font_italic",
            "font_antialiasing": "font_antialiasing",
            "horizontal_stretch": "horizontal_stretch",
            "vertical_stretch": "vertical_stretch"
        },
        "rect": {
            "color": "background_color",
            "outline_enable": "outline_enable",
            "outline_color": "outline_color",
            "outline_width": "outline_width"
        }
    }

    def __init__(self):
        Style.__init__(self)
        self.copy_style_by_map(LabelStyle(), self.COPY_MAP["label"])
        self.copy_style_by_map(RectStyle(), self.COPY_MAP["rect"])


class Button(Element):

    # region Properties

    # region Text property

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if value == self.__text:
            return

        self.__text = value
        for handler in self.prop_text_set_handlers:
            handler(None, self)

    @text.deleter
    def text(self):
        del self.__text

    # endregion

    # endregion

    def __init__(self):
        Element.__init__(self)

        # region Properties

        self.__text = "Button"
        self.style = ButtonStyle()

        # endregion

        # region Property handlers

        self.prop_text_set_handlers = []

        # endregion

        # region Child

        self.__rect1 = Rect()
        self.__label1 = Label()

        # endregion

        # binds

        self.prop_hovered_set_handlers.append(self.request_render)
        self.prop_text_set_handlers.append(self.request_render)
        self.style.change_handlers.append(self.request_render)

    def render(self):
        self.surface = pygame.Surface(self.size)
        self.update_style_state()

        self.__label1.text = self.text
        self.__label1.size = self.size
        self.__rect1.size = self.size

        self.__rect1.style.copy_property_by_map(self.style, self.style.COPY_MAP["rect"])
        self.__label1.style.copy_property_by_map(self.style, self.style.COPY_MAP["label"])

        self.__rect1.draw(self.surface, True)
        self.__label1.draw(self.surface, False)

        self._post_render()
