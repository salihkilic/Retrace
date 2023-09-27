from abc import abstractmethod, ABC
from GameLogic.Inventory import Inventory


class BaseLocation(ABC):

    def __init__(self, actions=None,
                 sublocations: list = None,
                 adjacent_locations: list = None):
        self.location_inventory = Inventory()
        # Sublocations are other locations, part of this location
        self.sublocations: list = sublocations if sublocations else []
        self.adjacent_locations: list = adjacent_locations if adjacent_locations else []
        self.actions = actions if actions else []

    def available_actions(self, player):
        # Return the list of actions that the player can perform in this location
        return [action for action in self.actions if action.player_can_perform(player)]

    @abstractmethod
    def room_description(self):
        """
        This is the base description of the location. This will not change by gameplay
        :return: string
        """
        pass

    @abstractmethod
    def background_image(self):
        """
        The file path to the image
        :return: string
        """

    @abstractmethod
    def background_music(self):
        """
        The file path to the sound file
        :return: string
        """
        pass

    def item_descriptions(self):
        amount_of_items = len(self.location_inventory.items)
        if amount_of_items == 1:
            return f"You see a {self.location_inventory.items[0].description}"
        if amount_of_items == 2:
            return (f"You see a {self.location_inventory.items[0].description} and"
                    f" a {self.location_inventory.items[1].description}")
        if amount_of_items >= 3:
            proto_string = ""
            for item in self.location_inventory.items[0:-2]:
                proto_string += f"a {item.description}, "
            return (f"You see {proto_string}a {self.location_inventory.items[-2].description} "
                    f"and a {self.location_inventory.items[-1].description}")
        else:
            return self.room_description()


class LocationAction:
    def __init__(self, description, conditions: list = None):
        self.description = description
        self.conditions = conditions  # A lambda function or callable to check if the action can be performed

    def player_can_perform(self, player):
        if not self.conditions:
            return True
        else:
            return all(condition(player) for condition in self.conditions)
