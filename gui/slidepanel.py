import pygame

from gui.element import Element
from gui.rect import Rect
from gui.rect import RectStyle
from gui.style import Style


class SlidePanelStyle(Style):
    COPY_MAP = {
        "rect": {
            "color": "background_color",
            "outline_enable": "outline_enable",
            "outline_color": "outline_color",
            "outline_width": "outline_width"
        }
    }

    def __init__(self):
        Style.__init__(self)
        self.copy_style_by_map(RectStyle(), self.COPY_MAP["rect"])
        self.create_property("normal", "align", "horizontal")


class SlidePanel(Element):
    # region Properties

    # region Child property

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        self.__child = value
        for handler in self.prop_child_set_handlers:
            handler(None, self)

    @child.deleter
    def child(self):
        del self.__child

    # endregion

    # region Slide_Position property

    @property
    def slide_position(self):
        return self.__slide_position

    @slide_position.setter
    def slide_position(self, value):
        self.__slide_position = value
        for handler in self.prop_slide_position_set_handlers:
            handler(None, self)

    @slide_position.deleter
    def slide_position(self):
        del self.__slide_position

    # endregion

    # endregion

    def __init__(self):
        Element.__init__(self)

        # region Properties

        self.__child = []
        self.__slide_position = 0
        self.style = SlidePanelStyle()

        # endregion

        # region Property handlers

        self.prop_child_set_handlers = []
        self.prop_slide_position_set_handlers = []

        # endregion

        # region Child

        self.__rect1 = Rect()

        # endregion

        # region Bind handlers

        self.event_handlers.append(self.__change_clide_position)
        self.event_handlers.append(self.__call_event_child)

        # endregion

        self.render()

    def __call_event_child(self, event, sender):
        if self.collide(pygame.mouse.get_pos()):
            for child in self.child:
                if child._event(event, sender):
                    break

        else:
            self.reset()

        self.render()

    def reset(self):
        self.hovered = False
        self.slide_position = 0
        for child in self.child:
            child.reset()

    def __change_clide_position(self, event, sender):
        if event.type == pygame.MOUSEWHEEL:
            if self.collide(pygame.mouse.get_pos()):
                if self.style.get_property("align") == "vertical":
                    self.slide_position = max(0, min(1, self.slide_position - event.precise_y / 25))
                else:
                    self.slide_position = max(0, min(1, self.slide_position + event.precise_x / 25))

                self.render()

    def render(self):
        self.surface = pygame.Surface(self.size)
        self.update_style_state()

        self.__rect1.style.copy_property_by_map(self.style, self.style.COPY_MAP["rect"])

        self.__rect1.size = self.size
        self.__rect1.draw(self.surface, True)

        self.calculate_position()

        for child in self.child:
            child.draw(self.surface, True)

    def add_child(self, element):
        self.child.append(element)
        self.calculate_position()

    def clear_child(self):
        self.child = []

    def calculate_position(self):
        sum_width = sum([elem.size[0] for elem in self.child])
        sum_height = sum([elem.size[1] for elem in self.child])

        delta_width = max(0, sum_width - self.size[0])
        delta_height = max(0, sum_height - self.size[1])

        if self.style.get_property("align") == "vertical":
            previous_height = 0
            for element in self.child:
                y = previous_height - delta_height * self.slide_position
                element.position = (0, y)
                element.size = (min(self.size[0], element.size[0]), element.size[1])
                element.offset = self.position
                previous_height += element.size[1]

        else:
            previous_width = 0
            for element in self.child:
                x = previous_width - delta_width * self.slide_position
                element.position = (x, 0)
                element.size = (element.size[0], min(self.size[1], element.size[1]))
                element.offset = self.position
                previous_width += element.size[0]
