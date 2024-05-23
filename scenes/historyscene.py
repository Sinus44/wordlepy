import pygame

import gui
from scenectrl import Scene
from .historyscenegui import layout, palette, pw, ph, slide, back_button


class HistoryScene(Scene):
    def __init__(self, app):
        Scene.__init__(self, app)
        self.app = app
        self.generate_child()
        back_button.on_click_handlers.append(self.back_button_click)

    def select(self):
        layout.reset()

    def back_button_click(self, event, sender):
        self.app.scene_controller.select_scene("menu")

    def generate_child(self):
        records = ["Слово: кружка Победа: Да", "Слово: пиздец Победа: Нет", "Слово: блядьта Победа: Да"]

        for i, record in enumerate(records):
            btn = gui.Button()
            btn.size = (100 * pw, 3 * ph)
            btn.text = f"#{len(records) - i} {record}"
            btn.style.set_property("normal", "background_color", palette[4] if i % 2 else (50, 50, 50))
            btn.render()
            slide.add_child(btn)

    def draw_tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.stop()

            layout.event(event, self)

        layout.draw(self.app.screen)
        pygame.display.update()
