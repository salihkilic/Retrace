from abc import abstractmethod, ABC
from GameLogic.Inventory import Inventory


# Todo Let's create an enum of locations:strings and their sublocations so we can pass them easily


class BaseLocation(ABC):
    sublocations: list

    def __init__(self):
        self.location_inventory = Inventory()

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

    # TODO
    # Description of travel options, "adjacent locations"
    # Function that describes actions that can be taken and removes them from the list of actions to be taken if needed
    # The action should also understand whether an item is needed to perform it,
    # but the game manager does the check for it

    # Later, the scene manager uses these actions to present them as buttons
