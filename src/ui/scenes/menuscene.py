from src.scenectrl import Scene
from .menuscenegui import layout, start_button, exit_button, history_button


class MenuScene(Scene):
    def __init__(self, app):
        Scene.__init__(self, app)
        self.app = app
        start_button.on_click_handlers.append(self.start_button_click)
        exit_button.on_click_handlers.append(lambda event, sender: self.app.stop())
        history_button.on_click_handlers.append(self.history_button_click)

    def history_button_click(self, event, sender):
        self.app.scene_controller.select_scene("history")

    def select(self):
        layout.reset()

    def start_button_click(self, event, sender):
        self.app.scene_controller.select_scene("main")

    def event(self, event):
        layout.event(event, self)

    def draw_tick(self):
        layout.draw(self.app.screen)
