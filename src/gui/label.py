import pygame.font

from .element import Element
from .style import Style

pygame.font.init()


class LabelStyle(Style):
    def __init__(self):
        Style.__init__(self)
        self.create_property("normal", "font_color", (230, 230, 230))
        self.create_property("normal", "font_name", "Consolas")
        self.create_property("normal", "font_size", 12)
        self.create_property("normal", "horizontal_align", "center")
        self.create_property("normal", "vertical_align", "center")
        self.create_property("normal", "font_bold", False)
        self.create_property("normal", "font_italic", False)
        self.create_property("normal", "font_antialiasing", True)
        self.create_property("normal", "horizontal_stretch", False)
        self.create_property("normal", "vertical_stretch", False)


class Label(Element):
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

        self.prop_text_set_handlers = []

        # region Properties
        self.__text = "Label"
        self.style = LabelStyle()
        # endregion

        self.prop_text_set_handlers.append(self.request_render)
        self.style.change_handlers.append(self.request_render)

    def render(self):

        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.update_style_state()

        font = pygame.font.SysFont(self.style.get_property("font_name"), self.style.get_property("font_size"),
                                   self.style.get_property("font_bold"), self.style.get_property("font_italic"))

        rendered = font.render(self.text, self.style.get_property("font_antialiasing"),
                               self.style.get_property("font_color"))

        if self.style.get_property("horizontal_stretch"):
            width = self.size[0]
        else:
            width = min(self.size[0], rendered.get_width())

        if self.style.get_property("vertical_stretch"):
            height = self.size[1]
        else:
            height = min(self.size[1], rendered.get_height())

        rendered = pygame.transform.scale(rendered, [width, height])

        kwargs = {}

        if self.style.get_property("horizontal_align") == "left":
            kwargs["left"] = 0

        elif self.style.get_property("horizontal_align") == "right":
            kwargs["right"] = self.size[0]

        else:
            kwargs["centerx"] = self.size[0] / 2

        if self.style.get_property("vertical_align") == "top":
            kwargs["top"] = 0

        elif self.style.get_property("vertical_align") == "bottom":
            kwargs["bottom"] = self.size[1]

        else:
            kwargs["centery"] = self.size[1] / 2

        rect = rendered.get_rect(**kwargs)
        rect.y += 2

        self.surface.blit(rendered, rect)
        self._post_render()
