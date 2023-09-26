from abc import abstractmethod, ABCMeta


class BaseScene(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        # Handle scene-specific events here
        pass

    @abstractmethod
    def update(self):
        # Update the scene's state here
        pass

    @abstractmethod
    def draw(self, screen):
        # Draw the scene's objects on the given screen here
        pass