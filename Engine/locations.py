from typing import Optional
from Engine.objects import Item


class Location:
    def __init__(self, name: str, description: str, pois: Optional[list], items: Optional[Item], location_ascii: str):
        self.name = name
        self.description = description
        self.pois = pois
        self.items = items
        self.location_ascii = location_ascii


class Map:
    def __init__(self, name: str, locations: list[Location], ascii_art: str):
        self.name = name
        self.locations = locations
        self.ascii = ascii_art
        self.initial_location = locations[0]


"""
###################
LOCATIONS
###################
"""
location1 = Location("Square",
                     "A small square with houses",
                     None,
                     None,
                     "$$$$$$$$$$\n"
                     "$$$$$$$$$$\n"
                     "$$$$L1$$$$\n"
                     "$$$$$$$$$$\n"
                     "$$$$$$$$$$\n")

location2 = Location("House",
                     "My little house in the city",
                     None,
                     None,
                     "$$$$$$$$$$\n"
                     "$$$$$$$$$$\n"
                     "$$$$L2$$$$\n"
                     "$$$$$$$$$$\n"
                     "$$$$$$$$$$\n")

location3 = Location("Laboratory",
                     "A lab where they steal memories",
                     None,
                     None,
                     "$$$$$$$$$$\n"
                     "$$$$$$$$$$\n"
                     "$$$$L3$$$$\n"
                     "$$$$$$$$$$\n"
                     "$$$$$$$$$$\n")

location4 = Location("School",
                     "Where I learn to code",
                     None,
                     None,
                     "$$$$$$$$$$\n"
                     "$$$$$$$$$$\n"
                     "$$$$L4$$$$\n"
                     "$$$$$$$$$$\n"
                     "$$$$$$$$$$\n")

"""
###################
MAPS
###################
"""

map1 = Map("Map 1",
           [location1, location2],
           "######\n"
           "######\n"
           "##M1##\n"
           "######\n"
           "######\n")

map2 = Map("Map 2",
           [location3, location4],
           "######\n"
           "######\n"
           "##M2##\n"
           "######\n"
           "######\n")

# TODO Build two maps with each two proto-locations (with proto-ascii art, just #####)
