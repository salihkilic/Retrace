from abc import abstractmethod, ABC
from typing import Optional


class LocationObject:
    """
    An object tied to a location, for example a computer the player might interact with in a lab
    """
    pass


class Item:
    pass


class BaseLocation(ABC):

    # For future me: Optional makes the argument nullable.
    # Either we get a list of objects, or a null
    def __init__(self,
                 description: str,
                 location_objects: list[LocationObject] = None,
                 location_items: list[Item] = None):
        self.description = description
        self.objects = location_objects
        self.items = location_items

    @abstractmethod
    def try_this(self):
        pass


if __name__ == '__main__':
    pass
