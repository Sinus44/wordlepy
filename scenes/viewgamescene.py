import pygame

import cellcodes
import colors
import history
from scenectrl import Scene
from .viewgamescenegui import menu_button, layout, cells, label


class ViewGameScene(Scene):
    def __init__(self, app):
        Scene.__init__(self, app)

        self.game = None  # history.History.load()[self.app.view_game]

        # delete_button.on_click_handlers.append(self.gui_keyboard_delete_symbol)
        # enter_button.on_click_handlers.append(self.gui_enter_press)
        # new_game_button.on_click_handlers.append(self.gui_new_game)
        menu_button.on_click_handlers.append(self.gui_menu)

    def gui_menu(self, event, sender):
        self.app.scene_controller.select_scene("history")

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
        for i, line in enumerate(self.game["field"]):
            for j, cell in enumerate(line):
                cells[i][j].style.set_property("normal", "background_color", self.get_color_by_state(cell[1]))
                cells[i][j].text = cell[0]

    def select(self):
        layout.reset()
        self.game = history.History.load()[self.app.view_game]
        label.text = ("Победа!" if self.game["win"] else "Поражение.") + " Слово: " + self.game["word"]
        self.copy_plane()

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.app.scene_controller.select_scene("history")
                return True

        layout.event(event, self)

    def draw_tick(self):
        # self.copy_plane()
        # self.update_keyboard()

        # if self.app.game.ended:
        #    label.text = ("Победа!" if self.app.game.win else "Поражение.") + " Слово: " + self.app.game.current_word
        #    # label.render()
        # else:
        #    label.text = "XXXXXX"

        layout.draw(self.app.screen)
