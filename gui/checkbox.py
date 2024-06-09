import pygame

from .element import Element
from .label import Label
from .label import LabelStyle
from .rect import Rect
from .rect import RectStyle
from .style import Style


class CheckboxStyle(Style):
    COPY_MAP = {
        "rect1": {
            "color": "background_color",
            "outline_enable": "background_outline_enable",
            "outline_width": "background_outline_width",
            "outline_color": "background_outline_color"
        },
        "rect2": {
            "color": "check_color",
            "outline_enable": "check_outline_enable",
            "outline_width": "check_outline_width",
            "outline_color": "check_outline_color"
        },
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
    }

    def __init__(self):
        Style.__init__(self)
        self.copy_style_by_map(RectStyle(), self.COPY_MAP["rect1"])
        self.copy_style_by_map(RectStyle(), self.COPY_MAP["rect2"])
        self.copy_style_by_map(LabelStyle(), self.COPY_MAP["label"])
        self.create_state("checked")
        self.create_property("normal", "check_width", 50)
        self.set_property("normal", "check_color", (50, 50, 50))
        self.set_property("checked", "check_color", (150, 250, 150))


class Checkbox(Element):
    # region Properties
    # region Checked property

    @property
    def checked(self):
        return self.__checked

    @checked.setter
    def checked(self, value):
        if self.__checked == value:
            return

        self.__checked = value
        for handler in self.prop_checked_set_handlers:
            handler(None, self)

    @checked.deleter
    def checked(self):
        del self.__checked

    # endregion
    # region Text property

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if self.__text == value:
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

        self.__checked = False
        self.__text = "checkbox"
        self.style = CheckboxStyle()

        # endregion

        # region Property handlers

        self.prop_checked_set_handlers = [self.request_render]
        self.prop_text_set_handlers = [self.request_render]

        # endregion

        # region Child

        self.__rect1 = Rect()
        self.__rect2 = Rect()
        self.__label1 = Label()

        # endregion

        self.__rect2.on_click_handlers.append(self.__check_click)

        self.event_handlers.append(self.__rect2._event)

    def __check_click(self, event, sender):
        self.checked = not self.checked

    def render(self):
        self.surface = pygame.Surface(self.size)
        self.update_style_state()

        if self.checked:
            self.style.state = "checked"

        self.__rect1.style.copy_property_by_map(self.style, self.style.COPY_MAP["rect1"])
        self.__rect2.style.copy_property_by_map(self.style, self.style.COPY_MAP["rect2"])
        self.__label1.style.copy_property_by_map(self.style, self.style.COPY_MAP["label"])

        self.__rect1.size = self.size
        self.__rect2.offset = self.position
        self.__rect2.size = self.style.get_property("check_width"), self.size[1]

        self.__label1.position = [self.style.get_property("check_width"), 0]
        self.__label1.size = [self.size[0] - self.style.get_property("check_width"), self.size[1]]
        self.__label1.text = self.text
        self.__label1.style.copy_property_by_map(self.style, self.style.COPY_MAP["label"])

        self.__rect1.draw(self.surface, True)
        self.__rect2.draw(self.surface, True)
        self.__label1.draw(self.surface, True)

        self._post_render()
