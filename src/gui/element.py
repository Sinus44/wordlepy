import gui
import pygame


class Element:

    # region Properties

    # region Hovered property

    @property
    def hovered(self):
        return self.__hovered

    @hovered.setter
    def hovered(self, value):
        if value != self.__hovered:
            self.__hovered = value
            for handler in self.prop_hovered_set_handlers:
                handler(self, None)

    @hovered.deleter
    def hovered(self):
        del self.__hovered

    # endregion

    # region Visible property

    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, value):
        if value != self.__visible:
            self.__visible = value
            for handler in self.prop_enable_set_handlers:
                handler(self, None)

    @visible.deleter
    def visible(self):
        del self.__visible

    # endregion

    # region Enable property

    @property
    def enable(self):
        return self.__enable

    @enable.setter
    def enable(self, value):
        if value != self.__enable:
            self.__enable = value
            for handler in self.prop_enable_set_handlers:
                handler(self, None)

    @enable.deleter
    def enable(self):
        del self.__enable

    # endregion

    # region Active property

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, value):
        if value != self.__active:
            self.__active = value
            for handler in self.prop_active_set_handlers:
                handler(self, None)

    @active.deleter
    def active(self):
        del self.__active

    # endregion

    # region Position property

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if value != self.__position:
            self.__position = value
            for handler in self.prop_position_set_handlers:
                handler(None, self)

    @position.deleter
    def position(self):
        del self.__position

    # endregion

    # region Offset property

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, value):
        if value != self.__offset:
            self.__offset = value
            for handler in self.prop_offset_set_handlers:
                handler(None, self)

    @offset.deleter
    def offset(self):
        del self.__offset

    # endregion

    # region Size property

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value != self.__size:
            self.__size = value
            for handler in self.prop_size_set_handlers:
                handler(self, None)

    @size.deleter
    def size(self):
        del self.__size

    # endregion

    # region Style property

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, value):
        if value != self.__style:
            self.__style = value
            for handler in self.prop_style_set_handlers:
                handler(self, None)

    @style.deleter
    def style(self):
        del self.__style

    # endregion

    # region Userdata property

    @property
    def userdata(self):
        return self.__userdata

    @userdata.setter
    def userdata(self, value):
        if value != self.__userdata:
            self.__userdata = value
            for handler in self.prop_userdata_set_handlers:
                handler(self, None)

    @userdata.deleter
    def userdata(self):
        del self.__userdata

    # endregion

    # endregion

    def __init__(self):
        # region Properties

        self.__position = (0, 0)
        self.__offset = (0, 0)
        self.__size = [100, 100]
        self.__style = gui.Style()
        self.__userdata = {}

        self.__hovered = False
        self.__enable = True
        self.__active = False
        self.__visible = True

        # endregion

        self.surface = None
        self.render_required = True

        self.event_handlers = []
        self.on_click_handlers = []
        self.on_miss_click_handlers = []
        self.post_render_handlers = []

        self.prop_style_set_handlers = [self.request_render]
        self.prop_enable_set_handlers = [self.request_render]
        self.prop_hovered_set_handlers = [self.request_render]
        self.prop_active_set_handlers = [self.request_render]
        self.prop_position_set_handlers = [self.request_render]
        self.prop_offset_set_handlers = [self.request_render]
        self.prop_size_set_handlers = [self.request_render]
        self.prop_userdata_set_handlers = []

    def request_render(self, event=None, sender=None):
        self.render_required = True

    def _post_render(self):
        self.render_required = False
        for handler in self.post_render_handlers:
            if handler(None, self):
                return

    def update_style_state(self):
        if not self.enable:
            self.style.state = "disabled"

        elif self.active:
            self.style.state = "active"

        elif self.hovered:
            self.style.state = "hovered"

        else:
            self.style.state = "normal"

    def _event(self, event, sender):
        if not self.enable:
            return False

        for handler in self.event_handlers:
            if handler(event, self):
                return False

        self.hovered = self.collide(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONUP:
            if self.collide(event.pos):
                if self.__on_click(event, sender):
                    return True

            else:
                self.__on_miss_click(event, sender)

        elif event.type == pygame.WINDOWLEAVE:
            self.hovered = False

    def __on_click(self, event, sender):
        for on_click_handler in self.on_click_handlers:
            if on_click_handler(event, self):
                return True

    def __on_miss_click(self, event, sender):
        for on_miss_click_handler in self.on_miss_click_handlers:
            if on_miss_click_handler(event, self):
                return True

    def reset(self):
        self.hovered = False

    def render(self):
        self.surface = pygame.Surface(self.size)
        self.update_style_state()
        self._post_render()

    def draw(self, surface, auto_render=False):
        if not self.visible:
            return

        if auto_render or self.render_required:
            self.render()

        surface.blit(self.surface, self.position)

    def collide(self, position):
        return self.position[0] + self.offset[0] <= position[0] <= self.position[0] + self.offset[0] + self.size[0] and \
            self.position[1] + self.offset[1] <= position[1] <= self.position[1] + self.offset[1] + self.size[1]
