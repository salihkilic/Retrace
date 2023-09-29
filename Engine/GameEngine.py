import time
import os
from rich import print
from Engine.location import map1, map2
from Engine.player import Player
from Engine.ui import GameUI


class GameEngine:

    def __init__(self):
        self.running = False
        self.discovered_maps = [map1]
        self.current_map = map1
        self.current_location = map1.locations[0]
        self.game_message = "Welcome to Retrace: Forgotten Paths. Please select your first action..."
        self.ui = GameUI()
        self.player = Player()

    def run(self):
        self.running = True
        while self.running:
            self.draw_ui()
            player_action = self.request_input()
            self.handle_commands(player_action)

    def request_input(self):
        return int(input("Please enter your action (number): "))

    def handle_commands(self, player_action):
        match player_action:
            case 1:
                # 1) Go to location on map
                self.log_ui(self.goto_location())
            case 2:
                # 2) Travel to different map
                self.log_ui(self.goto_map())
            case 3:
                # 3) Interact with an item
                self.log_ui(self.interact_with_item())
            case 4:
                # 4) Pick up an item
                self.log_ui(self.pick_up_item())
            case 5:
                # 5) Interact with a point of interest
                self.log_ui(self.interact_with_poi())
            case 6:
                #6) Exit Game
                self.clear_screen()
                quit("\n ---------------------"
                     "\n Player exit from game"
                     "\n  Thanks for playing! "
                     "\n ---------------------")
            case _:
                self.game_message = "[ERROR] You didn't pick a correct number, try again..."

    def draw_ui(self):
        self.clear_screen()
        self.ui.update_layout(self.current_location,
                              self.current_map.ascii,
                              self.game_message,
                              self.player)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.2)

    def goto_location(self) -> str:
        # Show the options we can travel to
        print("What location do you want to move to on this map?")
        for num, loc in enumerate(self.current_map.locations):
            print(f"{num + 1}). {loc.name}")
        # Let the user tell us where they want to go
        destination_pick = int(input("Enter your number: "))
        target_location = self.current_map.locations[destination_pick - 1]

        # Check if location is available / not locked
        if target_location.needs_item_name:

            if not self.check_inventory_by_name(target_location.needs_item_name):
                return f"You can't access this location because: [bold red]{target_location.locked_reason}[/bold red]"

            # If they have the item, tell the user they used it to get in
            self.current_location = target_location
            return (f"You used the [bold green]{target_location.needs_item_name}[/bold green] and"
                    f" traveled to the location: [bold green]{self.current_location.name}[/bold green]")

        # If no item needed, let's just go!
        self.current_location = target_location
        return f"You traveled to the location: {self.current_location.name}"

    def goto_map(self) -> str:
        print("What map do you want to move to?")
        for num, loc in enumerate(self.discovered_maps):
            print(f"{num + 1}). {loc.name}")
        destination_pick = int(input("Enter your number: "))
        self.current_map = self.discovered_maps[destination_pick - 1]
        # We go to the first location of the new map as well
        self.current_location = self.current_map.locations[0]
        return f"You traveled to the map: {self.current_map.name}"

    def interact_with_poi(self):
        try:
            poi_pick = int(input("What point of interest do you want to interact with? (Pick the number): "))
            if poi_pick > len(self.current_location.pois):
                return f"Your pick ({poi_pick}) is not a valid choice. Try again."
            return self.current_location.pois[poi_pick - 1].interact(self.current_location, self.discovered_maps)
        except ValueError:
            return f"You entered an invalid input, try again..."

    def interact_with_item(self):
        try:
            item_pick = int(input("Which item do you want to interact with? (Pick the number): "))
            if item_pick > len(self.player.inventory):
                return f"Your pick ({item_pick}) is not a valid choice. Try again."
            return self.player.inventory[item_pick - 1].interact(self.current_location, self.discovered_maps)
        except ValueError:
            return f"You entered an invalid input, try again..."

    def log_ui(self, msg):
        self.game_message = msg

    def check_inventory_by_name(self, item_name) -> bool:
        for item in self.player.inventory:
            if item.name == item_name:
                return True
        return False

    def pick_up_item(self):
        # Dear user, why would you even choose this
        if len(self.current_location.items) == 0:
            return "There don't seem to be any items here..."
        # Remove item from location and add to inventory
        # Because there's only one item here, no need to ask the user which one
        if len(self.current_location.items) == 1:
            item = self.current_location.items.pop(0)
            self.player.inventory.append(item)
            return f"You picked up a [bold green]{item.name}[/bold green]!"
        try:
            poi_pick = int(input("What point of interest do you want to interact with? (Pick the number): "))
            if poi_pick > len(self.current_location.pois):
                return f"Your pick ({poi_pick}) is not a valid choice. Try again."
            return self.current_location.pois[poi_pick - 1].interact(self.current_location, self.discovered_maps)
        except ValueError:
            return f"You entered an invalid input, try again..."


# TODO We could probably highlight the panel that needs the attention at certain actions!
