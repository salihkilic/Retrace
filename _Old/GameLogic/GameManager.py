from GameLogic import Inventory
from _Old.GameLogic import Player


class Manager:
    def __init__(self):
        self.player = Player.Player()
        self.inventory = Inventory.Inventory()

        # Create locations (at game start) and populate
        def load_locations(locations: list):
            """
            Takes in a list of locations for the manager to handle
            :param locations:
            :return:
            """
            pass

        # Load first location into scene, the location itself leads to new locations
        # TODO Make functions for the different actions a player might take: take item, use item, move to location and report that to the UI

