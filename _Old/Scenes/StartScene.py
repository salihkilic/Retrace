import pygame
import math
from _Old.Scenes.BaseScene import BaseScene
from Scenes.HelperFunctions import Button
from Scenes.GameEvents import game_start


class StartScene(BaseScene):
    def __init__(self):
        # Background and logo
        super().__init__()
        self.background = pygame.image.load('Assets/city_background.jpg')
        self.logo = pygame.image.load('Assets/LogoRetrace.png').convert_alpha()
        self.logo_original = self.logo.copy()
        self.logo = pygame.Surface(self.logo_original.get_size(), pygame.SRCALPHA)
        self.logo.blit(self.logo_original, (0, 0))
        self.angle = 0

        # Buttons
        self.play_button = Button('Play', 300, 500, 200, 60, (50, 200, 50), self.play_game)
        self.quit_button = Button('Quit', 300, 570, 200, 60, (200, 50, 50), self.quit_game)

    def play_game(self):
        game_start()

    def quit_game(self):
        pygame.quit()

    def handle_event(self, event):
        self.play_button.handle_event(event)
        self.quit_button.handle_event(event)

    def update(self):
        # Pulsing effect
        self.angle += 0.01
        alpha = 128 + 127 * math.sin(self.angle)
        self.logo = self.logo_original.copy()
        self.logo.fill((255, 255, 255, alpha), None, pygame.BLEND_RGBA_MULT)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.logo, (200, 100))
        self.play_button.draw(screen)
        self.quit_button.draw(screen)
