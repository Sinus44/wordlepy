import pygame.event

import src.logic.cellcodes as cellcodes
import src.ui.colors as colors
import src.ui.keyconverter as keyconverter
from src.scenectrl import Scene
from .mainscenegui import layout, cells, keyboard, enter_button, delete_button, new_game_button, label, menu_button


class MainScene(Scene):
    def __init__(self, app):
        Scene.__init__(self, app)

        for line in keyboard:
            for button in line:
                button.on_click_handlers.append(self.gui_keyboard_press)

        delete_button.on_click_handlers.append(self.gui_keyboard_delete_symbol)
        enter_button.on_click_handlers.append(self.gui_enter_press)
        new_game_button.on_click_handlers.append(self.gui_new_game)
        menu_button.on_click_handlers.append(self.gui_menu)

    def gui_menu(self, event, sender):
        self.app.scene_controller.select_scene("menu")

    def gui_new_game(self, event, sender):
        self.app.game.start()

    def keyboard_key_press(self, key_code):
        pressed_char = keyconverter.convert_code_to_char(key_code)
        if pressed_char is not None:
            self.app.game.add_symbol(pressed_char)
            return True

    def gui_enter_press(self, event, sender):
        self.app.game.enter()

    def gui_keyboard_press(self, event, sender):
        self.app.game.add_symbol(sender.text)

    def gui_keyboard_delete_symbol(self, event, sender):
        self.app.game.delete_symbol()

    @staticmethod
    def get_color_by_state(state):
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
                cells[i][j].style.set_property("normal", "background_color", self.get_color_by_state(cell.type))
                cells[i][j].text = cell.char

    def update_keyboard(self):
        for i, line in enumerate(keyboard):
            for j, key in enumerate(line):
                key.style.set_property("normal", "background_color",
                                       self.get_color_by_state(self.app.game.get_state_keyboard(key.text)))
                # key.render()

    def select(self):
        layout.reset()

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.app.game.delete_symbol()

            elif event.key == pygame.K_RETURN:
                if self.app.game.ended:
                    self.gui_new_game(None, None)
                else:
                    self.app.game.enter()

            elif event.key == pygame.K_ESCAPE:
                self.gui_menu(None, None)

            else:
                self.keyboard_key_press(event.scancode)

        layout.event(event, self)

    def draw_tick(self):
        enter_button.enable = self.app.game.is_full_string() and not self.app.game.ended
        delete_button.enable = not self.app.game.ended and len(self.app.game.get_text()) > 0

        self.copy_plane()
        self.update_keyboard()

        if self.app.game.ended:
            label.text = ("Победа!" if self.app.game.win else "Поражение.") + " Слово: " + self.app.game.current_word
            # label.render()
        else:
            label.text = "XXXXXX"

        layout.draw(self.app.screen)
