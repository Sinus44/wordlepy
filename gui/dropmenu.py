import pygame

from .button import Button, ButtonStyle
from .element import Element
from .slidepanel import SlidePanel, SlidePanelStyle
from .style import Style


class DropMenuStyle(Style):
    COPY_MAP = {
        "button": {
            "font_color": "font_color",
            "font_name": "font_name",
            "font_size": "font_size",
            "horizontal_align": "horizontal_align",
            "vertical_align": "vertical_align",
            "font_bold": "font_bold",
            "font_italic": "font_italic",
            "font_antialiasing": "font_antialiasing",
            "horizontal_stretch": "horizontal_stretch",
            "vertical_stretch": "vertical_stretch",
            "background_color": "background_color",
            "outline_enable": "outline_enable",
            "outline_color": "outline_color",
            "outline_width": "outline_width"
        },

        "slide_panel": {
            "background_color": "slide_background_color",
            "outline_enable": "slide_outline_enable",
            "outline_color": "slide_outline_color",
            "outline_width": "slide_outline_width",
            "align": "slide_align"
        }
    }

    def __init__(self):
        Style.__init__(self)
        self.copy_style_by_map(ButtonStyle(), self.COPY_MAP["button"])
        self.copy_style_by_map(SlidePanelStyle(), self.COPY_MAP["slide_panel"])
        self.create_state("opened")


class DropMenu(Element):
    # region Properties

    # region Opened property

    @property
    def opened(self):
        return self.__opened

    @opened.setter
    def opened(self, value):
        if value != self.__opened:
            self.__opened = value
            for handler in self.prop_opened_set_handlers:
                handler(None, self)

    @opened.deleter
    def opened(self):
        del self.__opened

    # endregion

    # region Text property

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if value != self.__text:
            self.__text = value
            for handler in self.prop_text_set_handlers:
                handler(None, self)

    @text.deleter
    def text(self):
        del self.__text

    # endregion

    # region Opened_size property

    @property
    def opened_size(self):
        return self.__opened_size

    @opened_size.setter
    def opened_size(self, value):
        if value == self.__opened_size:
            return

        self.__opened_size = value
        for handler in self.prop_opened_size_set_handlers:
            handler(None, self)

    @opened_size.deleter
    def opened_size(self):
        del self.__opened_size

    # endregion

    # endregion

    def __init__(self):
        Element.__init__(self)

        # region Properties

        self.__opened = False
        self.__opened_size = (100, 100)
        self.__text = "menu"
        self.style = DropMenuStyle()

        # endregion

        # region Property handlers

        self.prop_child_set_handlers = []
        self.prop_opened_set_handlers = []
        self.prop_text_set_handlers = []
        self.prop_opened_size_set_handlers = []

        # endregion

        # region Child

        self.__button1 = Button()
        self.__slidePanel1 = SlidePanel()

        # endregion

        # region Bind handlers

        self.event_handlers.append(self.__button1._event)
        self.event_handlers.append(self.__slidePanel1._event)
        self.event_handlers.append(self.request_render())
        self.__button1.on_click_handlers.append(self._on_click)

        # endregion

    def reset(self):
        self.hovered = False
        self.opened = False
        self.__button1.reset()
        self.__slidePanel1.reset()
        self.request_render()

    def _on_click(self, event, sender):
        self.opened = not self.opened
        self.request_render()

    def add_child(self, element):
        self.__slidePanel1.add_child(element)

    def render(self):
        self.surface = pygame.Surface([self.size[0] + self.opened_size[0], self.size[1] + self.opened_size[1]],
                                      pygame.SRCALPHA)
        self.update_style_state()

        if self.enable and self.opened:
            self.style.state = "opened"

        self.__button1.text = self.text
        self.__button1.position = self.position
        self.__button1.size = self.size

        self.__slidePanel1.size = self.opened_size
        self.__slidePanel1.position = (self.position[0], self.position[1] + self.__button1.size[1])
        self.__slidePanel1.visible = self.opened

        self.__button1.style.copy_property_by_map(self.style, self.style.COPY_MAP["button"])
        self.__slidePanel1.style.copy_property_by_map(self.style, self.style.COPY_MAP["slide_panel"])
        self.__slidePanel1.style.set_property("normal", "align", "vertical")

        self.__button1.draw(self.surface, True)
        self.__slidePanel1.draw(self.surface, True)

        self._post_render()
