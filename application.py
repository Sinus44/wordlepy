import pygame

from game import Game
from scenectrl import SceneController
from scenes import MainScene, MenuScene


class WordleGame:
    def __init__(self):
        self.size = (500, 700)
        self.screen = pygame.display.set_mode(self.size)
        self.scene_controller = SceneController()
        self.scene_controller.add_scenes({
            "main": MainScene(self),
            "menu": MenuScene(self)
        })
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load("logo.png"), (64, 64)))
        pygame.display.set_caption("WORDLE by Sinus44")
        self.game = Game()

        self.scene_controller.select_scene("menu")

    def start(self):
        self.scene_controller.start()

    def stop(self):
        self.scene_controller.stop()
