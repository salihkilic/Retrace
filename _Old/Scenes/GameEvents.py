import pygame

START_SCREEN = pygame.event.custom_type()
GAME_START = pygame.event.custom_type()


def start_screen():
    pygame.event.post(pygame.event.Event(START_SCREEN))


def game_start():
    pygame.event.post(pygame.event.Event(GAME_START))
