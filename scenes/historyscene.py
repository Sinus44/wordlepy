import gui
import history
from scenectrl import Scene
from .historyscenegui import layout, palette, pw, ph, slide, back_button, clear_button


class HistoryScene(Scene):
    def __init__(self, app):
        Scene.__init__(self, app)
        self.app = app
        self.games = []
        back_button.on_click_handlers.append(self.back_button_click)
        clear_button.on_click_handlers.append(self.clear_button_click)
        self.generate_child()

    def select(self):
        self.games = history.History.load()
        self.generate_child()
        layout.reset()

    def clear_button_click(self, event, sender):
        history.History.clear()
        self.select()

    def back_button_click(self, event, sender):
        self.app.scene_controller.select_scene("menu")

    def open_game_button(self, event, sender):
        self.app.view_game = sender.userdata["game_index"]
        self.app.scene_controller.select_scene("viewgame")
        return True

    def generate_child(self):
        records = [f'{game["word"]} - {"победа" if game["win"] else "поражение"}' for game in self.games[::-1]]
        slide.clear_child()

        for i, record in enumerate(records):
            btn = gui.Button()
            btn.size = (100 * pw, 3 * ph)
            btn.text = f"#{len(records) - i} {record}"
            btn.userdata["game_index"] = len(records) - i - 1
            btn.style.set_property("normal", "background_color", palette[4] if i % 2 else (50, 50, 50))
            btn.on_click_handlers.append(self.open_game_button)
            btn.prop_hovered_set_handlers = []
            slide.add_child(btn)

        layout.render()

    def event(self, event):
        layout.event(event, self)

    def draw_tick(self):
        layout.draw(self.app.screen)
