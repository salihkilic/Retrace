from typing import Optional
from Engine.object import Item, Poi


class Location:
    def __init__(self, name: str,
                 description: str,
                 pois: Optional[list[Poi]],
                 items: Optional[list[Item]],
                 location_ascii: str,
                 needs_item_name: Optional[str] = None,  # The name of the needed item
                 locked_reason: str = ""):
        self.name = name
        self.description = description
        self.pois = pois if pois else []
        self.items = items if items else []
        self.location_ascii = location_ascii
        self.needs_item_name = needs_item_name if needs_item_name else None
        self.locked_reason = locked_reason


class Map:
    def __init__(self, name: str, locations: list[Location], ascii_art: str):
        self.name = name
        self.locations = locations
        self.ascii = ascii_art
        self.initial_location = locations[0]
