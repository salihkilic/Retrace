import pygame
from pygame.locals import *
from Scenes.BaseScene import BaseScene
from Scenes.HelperFunctions import Button, wrap_text


class LocationScene(BaseScene):
    def __init__(self, story_text, location_image_path, action_choices=[]):
        super().__init__()
        self.story_text = story_text
        self.font = pygame.font.Font(None, 36)
        self.text_lines = wrap_text(story_text, self.font, 300)  # Wrap text to a max width of 300 pixels for example
        self.location_image = pygame.image.load(location_image_path).convert_alpha()
        self.action_image = None  # Can be updated later when relevant to the story
        self.buttons = [Button(choice, 50, 500 + i * 70, 300, 50, (100, 100, 200), self.perform_action) for i, choice in
                        enumerate(action_choices)]

    def set_action_image(self, image_path):
        self.action_image = pygame.image.load(image_path).convert_alpha()

    def perform_action(self, choice):
        # Handle what should happen when a specific choice is made
        pass

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        y_offset = 50
        for line in self.text_lines:
            screen.blit(line, (50, y_offset))
            y_offset += self.font.get_height()

        screen.blit(self.location_image, (400, 50))
        if self.action_image:
            screen.blit(self.action_image, (700, 50))

        for button in self.buttons:
            button.draw(screen)