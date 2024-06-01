import gui


class Scene:
    def __init__(self, app):
        self.app = app
        self.layout = gui.Layout()

    def event(self, event):
        ...

    def update_tick(self):
        ...

    def draw_tick(self):
        ...

    def select(self):
        ...
