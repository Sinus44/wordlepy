import pygame.event

from scenectrl import Scene
import keyconverter
from .mainscenegui import layout, cells, keyboard, enter_button, delete_button, new_game_button
import colors
import cellcodes

class MainScene(Scene):
    def __init__(self, app):
        Scene.__init__(self, app)

        for line in keyboard:
            for button in line:
                button.on_click_handlers.append(self.gui_keyboard_press)

        delete_button.on_click_handlers.append(self.gui_keyboard_delete_symbol)
        enter_button.on_click_handlers.append(self.gui_enter_press)
        new_game_button.on_click_handlers.append(self.gui_new_game)
        self.render_require = False

    def gui_new_game(self, event, sender):
        self.app.game.start()
        self.render_require = True

    def keyboard_key_press(self, key_code):
        pressed_char = keyconverter.convert_code_to_char(key_code)
        if pressed_char is not None:
            self.app.game.add_symbol(pressed_char)

    def gui_enter_press(self, event, sender):
        self.app.game.enter()

    def gui_keyboard_press(self, event, sender):
        self.app.game.add_symbol(sender.text)
        self.render_require = True

    def gui_keyboard_delete_symbol(self, event, sender):
        self.app.game.delete_symbol()
        self.render_require = True

    def get_color_by_state(self, state):
        if state == cellcodes.EMPTY:
            return colors.EMPTY
        elif state == cellcodes.NO:
            return colors.NO
        elif state == cellcodes.IN_WORD:
            return colors.IN_WORD
        elif state == cellcodes.POSITION:
            return colors.POSITION

    def copy_plane(self):
        for i, line in enumerate(self.app.game.plane):
            for j, cell in enumerate(line):
                cells[i][j].text = cell.char
                cells[i][j].style.set_property("normal", "background_color", self.get_color_by_state(cell.type))

    def update_keyboard(self):
        for i, line in enumerate(keyboard):
            for j, key in enumerate(line):
                key.style.set_property("normal", "background_color", self.get_color_by_state(self.app.game.get_state_keyboard(key.text)))

    def draw_tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.stop()

            if event.type == pygame.KEYDOWN:
                self.keyboard_key_press(event.scancode)

                if event.key == pygame.K_BACKSPACE:
                    self.app.game.delete_symbol()

                elif event.key == pygame.K_RETURN:
                    self.app.game.enter()

            layout.event(event, self)

        enter_button.enable = self.app.game.is_full_string() and not self.app.game.ended
        delete_button.enable = not self.app.game.ended and len(self.app.game.get_text()) > 0

        self.copy_plane()
        self.update_keyboard()

        layout.draw(self.app.screen, self.render_require)
        self.render_require = False
        pygame.display.update()

