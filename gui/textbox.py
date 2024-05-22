from .element import Element
from .button import Button, ButtonStyle
from .style import Style
import pygame


class TextboxStyle(Style):
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
        }
    }

    def __init__(self):
        Style.__init__(self)
        self.copy_style_by_map(ButtonStyle(), self.COPY_MAP["button"])
        self.create_state("hint")
        self.create_state("hint_active")


class Textbox(Element):
    # region Properties

    # region Text property

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
        for handler in self.prop_text_set_handlers:
            handler(None, self)

    @text.deleter
    def text(self):
        del self.__text

    # endregion

    # region Hint property

    @property
    def hint(self):
        return self.__hint

    @hint.setter
    def hint(self, value):
        self.__hint = value
        for handler in self.prop_hint_set_handlers:
            handler(None, self)

    @hint.deleter
    def hint(self):
        del self.__hint

    # endregion

    # region Max_Length property

    @property
    def max_length(self):
        return self.__max_length

    @max_length.setter
    def max_length(self, value):
        self.__max_length = value
        for handler in self.prop_max_length_set_handlers:
            handler(None, self)

    @max_length.deleter
    def max_length(self):
        del self.__max_length

    # endregion

    # region Alphabet property

    @property
    def alphabet(self):
        return self.__alphabet

    @alphabet.setter
    def alphabet(self, value):
        self.__alphabet = value
        for handler in self.prop_alphabet_set_handlers:
            handler(None, self)

    @alphabet.deleter
    def alphabet(self):
        del self.__alphabet

    # endregion

    # endregion

    def __init__(self):
        Element.__init__(self)

        # region Properties

        self.__text = "Text"
        self.__hint = "Hint"
        self.__max_length = 10
        self.__alphabet = None
        self.style = TextboxStyle()

        # endregion

        # region Property handlers

        self.prop_text_set_handlers = []
        self.prop_hint_set_handlers = []
        self.prop_max_length_set_handlers = []
        self.prop_alphabet_set_handlers = []

        # endregion

        # region Child

        self.__button1 = Button()

        # endregion

        # region Binding events

        self.event_handlers.append(self.__event)
        self.on_click_handlers.append(self.__click_event)
        self.on_miss_click_handlers.append(self.__miss_click_event)

        # endregion

        self.render()

    def reset(self):
        self.hovered = False
        self.active = False

    def render(self):
        self.surface = pygame.Surface(self.size)
        self.update_style_state()

        if self.text == "":
            self.style.state = "hint" + ("_active" if self.active else "")

        if self.style.state == "hint" or self.style.state == "hint_active":
            self.__button1.text = self.hint
        else:
            self.__button1.text = self.text

        self.__button1.size = self.size
        self.__button1.style.copy_property_by_map(self.style, self.style.COPY_MAP["button"])

        self.__button1.draw(self.surface, True)

    def __click_event(self, event, sender):
        self.active = True
        self.render()

    def __miss_click_event(self, event, sender):
        self.active = False
        self.render()

    def add_symbol(self, symbol):
        if self.active and (self.alphabet is None or symbol in self.alphabet) and len(self.text) < self.max_length:
            self.text += symbol
            self.render()

    def del_symbol(self):
        if self.active:
            self.text = self.text[:-1]
            self.render()

    def __event(self, event, sender):
        if event.type == pygame.TEXTINPUT:
            self.add_symbol(event.text)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.del_symbol()


