import pygame
from _Old.Scenes.BaseScene import BaseScene


class LocationScene(BaseScene):
    def __init__(self):
        super().__init__()

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.fill([255, 255, 255])
        pygame.display.update()

    def description_box(self):
        pass


# Build the scene, based on the location the gamemanager is providing

