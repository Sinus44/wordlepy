import pygame

from .element import Element
from .style import Style


class ImageStyle(Style):
    def __init__(self):
        Style.__init__(self)
        self.create_property("normal", "mode", "auto")


class Image(Element):
    # region Properties
    # region Path property

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        if self.__path == value:
            return

        self.__path = value
        for handler in self.prop_path_set_handlers:
            handler(None, self)

    @path.deleter
    def path(self):
        del self.__path

    # endregion
    # endregion

    def __init__(self):
        Element.__init__(self)

        # region Properties

        self.__path = ""
        self.style = ImageStyle()

        # endregion

        # region Property handlers

        self.prop_path_set_handlers = []

        # endregion

    def render(self):
        self.update_style_state()

        if self.__path:
            original_image = pygame.image.load(self.__path)

        else:
            original_image = pygame.Surface(self.size)

        image_ratio = original_image.get_width() / original_image.get_height()
        self_ratio = self.size[0] / self.size[1]

        if self.style.get_property("mode") == "auto":
            if self_ratio > image_ratio:
                height = self.size[1]
                width = height * image_ratio
            else:
                width = self.size[0]
                height = width / image_ratio

        elif self.style.get_property("mode") == "stretch":
            width, height = self.size

        else:  # crop
            width = original_image.get_width()
            height = original_image.get_height()

        scaled_image = pygame.transform.scale(original_image, (width, height))

        self.surface = pygame.Surface(self.size)
        self.surface.blit(scaled_image, scaled_image.get_rect(center=[self.size[0] / 2, self.size[1] / 2]))

        self._post_render()
