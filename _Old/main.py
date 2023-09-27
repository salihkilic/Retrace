import pygame
from Scenes import StartScene, LocationScene
from pygame.locals import *
from GameLogic.GameManager import Manager
from Scenes.GameEvents import START_SCREEN, GAME_START


class GameWindow:
    def __init__(self):
        pygame.init()

        # Screen Setup
        self.screenInfo = pygame.display.Info()
        # Screen set to 90% of max resolution
        self.screen = pygame.display.set_mode((self.screenInfo.current_w * 0.9, self.screenInfo.current_h * 0.9))
        pygame.display.set_caption('Retrace: Forgotten Paths')
        self.clock = pygame.time.Clock()

        # Setup Scenes
        self.start_screen = StartScene.StartScene()
        self.game_screen = LocationScene.LocationScene()
        # First scene is the starting screen
        self.scene = self.start_screen

        # Start the Engine
        self.manager = Manager()

    def switch_scene(self, new_scene):
        self.scene = new_scene

    def execute(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

                if event.type == GAME_START:
                    self.switch_scene(self.game_screen)
                if event.type == START_SCREEN:
                    self.switch_scene(self.start_screen)

                # Pass event to the scene
                self.scene.handle_event(event)

            # Update the scene
            self.scene.update()

            # Draw the scene
            self.scene.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


if __name__ == '__main__':
    game_screen = GameWindow()
    game_screen.execute()
