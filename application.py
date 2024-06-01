import pygame

from game import Game
from scenectrl import PGSceneController
from scenes import MainScene, MenuScene, HistoryScene


class WordleGame:
    def __init__(self):
        self.size = [500, 700]
        self.screen = pygame.display.set_mode(self.size)
        self.scene_controller = PGSceneController()
        self.scene_controller.add_scenes({
            "main": MainScene(self),
            "menu": MenuScene(self),
            "history": HistoryScene(self)
        })
        self.scene_controller.add_global_event_handler(self.global_event_handler)
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load("logo.png"), [64, 64]))
        pygame.display.set_caption("WORDLE by Sinus44")
        self.game = Game()

        self.scene_controller.select_scene("menu")

    def global_event_handler(self, event):
        if event.type == pygame.QUIT:
            self.stop()
            return True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                self.scene_controller.print_fps = not self.scene_controller.print_fps
                return True

            elif event.key == pygame.K_F2:
                self.scene_controller.set_fps(75)
                return True

            elif event.key == pygame.K_F3:
                self.scene_controller.set_fps(0)
                return True

    def start(self):
        self.scene_controller.start()

    def stop(self):
        self.scene_controller.stop()
