import pygame

from game import Game
from scenectrl import SceneController
from scenes import MainScene


class App:
    def __init__(self):
        self.size = (500, 700)
        self.screen = pygame.display.set_mode(self.size)
        self.scene_controller = SceneController()
        self.scene_controller.add_scenes({
            "main": MainScene(self)
        })
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load("logo.png"), (64, 64)))
        pygame.display.set_caption("WORDLE by Sinus44")
        self.game = Game()

        self.scene_controller.select_scene("main")

    def draw(self):
        ...

    def start(self):
        self.scene_controller.start()

    def stop(self):
        self.scene_controller.stop()


if __name__ == "__main__":
    app = App()
    app.start()
