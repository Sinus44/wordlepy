import jsonreader
from scenectrl import Scene
from .settingsscenegui import back_button, word_validate, history_checkbox, layout


class SettingsScene(Scene):
    def __init__(self, app):
        Scene.__init__(self, app)
        self.app = app
        self.games = []
        back_button.on_click_handlers.append(self.back_button_click)
        self.settings = jsonreader.read("userdata/settigns.json", {})
        word_validate.checked = self.settings.get("use_word_validator", True)
        history_checkbox.checked = self.settings.get("save_history", True)
        word_validate.prop_checked_set_handlers.append(self.change)
        history_checkbox.prop_checked_set_handlers.append(self.change)

    def change(self, event, sender):
        jsonreader.write("userdata/settings.json", {"use_word_validator": word_validate.checked,
                                                    "save_history": history_checkbox.checked})

    def select(self):
        layout.reset()

    def back_button_click(self, event, sender):
        self.app.scene_controller.select_scene("menu")

    def event(self, event):
        layout.event(event, self)

    def draw_tick(self):
        layout.draw(self.app.screen)
