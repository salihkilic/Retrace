from GameLogic.Inventory import Inventory


class Player:
    def __init__(self):
        self.inventory = Inventory()
        self.name = "Player"
        self.visited_locations = []

    def name_player(self, name):
        self.name = name

    def has_item_by_str(self, item_string):
        if self.inventory.find_item(item_string):
            return True
        else:
            return False

    def visit_location(self, location_name):
        if location_name not in self.visited_locations:
            self.visited_locations.append(location_name)

    def has_visited_location(self, location_name):
        if location_name in self.visited_locations:
            return True
        else:
            return False


