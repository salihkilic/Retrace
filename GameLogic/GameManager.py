from Scenes import StartScene, LocationScene
from GameLogic import Inventory, Player


class Manager:
    def __init__(self, switch_scene):
        self.switch_scene = switch_scene
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

        # TODO
        # Thing of note: The screen is drawn on every tick. So if we simply add a button
        # to the list of buttons in a scene, it gets drawn dynamically.
        # Also, we can feed the scene a list of actions to be able to take.

        # Let the scene handle ONLY the drawing
        # Feed it a dict, like "take sword: take_sword_func"

        # Then we can feed it two dicts: One with pathways, another with actions AT that location.
        # We may need a way to communicate to the scene we updated the options

        # Load all the scene instances (They won't draw until asked to)
