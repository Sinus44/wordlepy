import threading
import time

import pygame
import pygame.time


class SceneController:
    def __init__(self):
        self.scenes = {}
        self.selected_scene_name = ""
        self.update_clock = pygame.time.Clock()
        self.frame_clock = pygame.time.Clock()
        self.ups = 1
        self.fps = 75
        self.enable = False

    def set_fps(self, new_fps):
        self.fps = new_fps

    def set_ups(self, new_ups):
        self.ups = new_ups

    def add_scenes(self, scenes):
        for scene_name in scenes:
            if scene_name == "":
                raise Exception("Invalid scene name")

            if scene_name in self.scenes:
                raise Exception(f"Scene {scene_name} already exists in controller")

            self.scenes[scene_name] = scenes[scene_name]

    def select_scene(self, scene_name):
        if scene_name not in self.scenes:
            raise Exception(f"Scene {scene_name} not found in controller")

        self.selected_scene_name = scene_name
        self.scenes[self.selected_scene_name].select()

    def draw_wrapper(self):
        while self.enable:
            t = time.time()
            self.scenes[self.selected_scene_name].draw_tick()
            time.sleep((1 / self.fps) - (time.time() - t))

    def update_wrapper(self):
        while self.enable:
            t = time.time()
            self.scenes[self.selected_scene_name].update_tick()
            time.sleep((1 / self.ups) - (time.time() - t))

    def stop(self):
        self.enable = False

    def start(self):
        if self.enable:
            raise Exception("Already running")

        if self.selected_scene_name == "":
            raise Exception("Not selected scene")

        self.enable = True
        threading.Thread(target=self.update_wrapper, daemon=True).start()
        self.draw_wrapper()


