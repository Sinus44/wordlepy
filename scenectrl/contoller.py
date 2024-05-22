import threading

import pygame.time


class SceneController:
    def __init__(self):
        self.scenes = {}
        self.selected_scene_name = ""
        self.update_clock = pygame.time.Clock()
        self.frame_clock = pygame.time.Clock()
        self.ups = 100
        self.fps = 60
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
            self.scenes[self.selected_scene_name].draw_tick()
            self.frame_clock.tick(self.fps)

    def update_wrapper(self):
        while self.enable:
            self.scenes[self.selected_scene_name].update_tick()
            self.update_clock.tick(self.ups)

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
