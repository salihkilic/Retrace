import time
import os
from rich import print
from Engine.location import map1
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
            player_action = self.request_input_int("Please enter your action (number): ", 6)
            self.handle_commands(player_action)

    def request_input_int(self, msg: str, choice_amount: int):
        try:
            usr_input = int(input(msg))
        except ValueError:
            print(f"Error: Did you enter the right type of command? Most actions need a number.")
            usr_input = self.request_input_int(msg, choice_amount)
        except Exception:
            print(f"Something went wrong and an exception was raised after your command was entered "
                  f"but the dev didn't expect it. Maybe try again?")
            usr_input = self.request_input_int(msg, choice_amount)
        if usr_input > choice_amount or usr_input <= 0:
            print(f"That number ({usr_input}) is not available. Pick a number between 1 and {choice_amount}")
            usr_input = self.request_input_int(msg, choice_amount)
        return usr_input

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
                # 6) Exit Game
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
        destination_pick = self.request_input_int("Enter your number: ", len(self.current_map.locations))
        target_location = self.current_map.locations[destination_pick - 1]

        # Check if location is available / not locked by item
        if target_location.needs_item_name:

            if not self.check_inventory_by_name(target_location.needs_item_name):
                return (f"You see {target_location.description} \n\n"
                        f"You can't access this location because: [bold red]{target_location.locked_reason}[/bold red]")

            # If they have the item, tell the user they used it to get in
            self.current_location = target_location
            return (f"You used the [bold green]{target_location.needs_item_name}[/bold green] and"
                    f" traveled to the location: [bold green]{self.current_location.name}[/bold green]")

        # If no item needed, let's just go!
        self.current_location = target_location
        return f"You traveled to the location: {self.current_location.name}"

    def goto_map(self) -> str:

        if len(self.current_location.pois) == 1:
            print("There are no other maps to travel to, yet...")
        else:
            print("What map do you want to move to?")
            for num, loc in enumerate(self.discovered_maps):
                print(f"{num + 1}). {loc.name}")
            destination_pick = self.request_input_int("Enter your number: ", len(self.discovered_maps))
            self.current_map = self.discovered_maps[destination_pick - 1]
            # We go to the first location of the new map as well
            self.current_location = self.current_map.locations[0]
            return f"You traveled to the map: {self.current_map.name}"

    def interact_with_poi(self):
        if len(self.current_location.pois) == 0:
            print("There seem to be no Points of Interest at this location.")

        if len(self.current_location.pois) == 1:
            return self.current_location.pois[0].interact(self.current_location, self.discovered_maps)

        else:
            poi_pick = self.request_input_int(
                "What point of interest do you want to interact with? (Pick the number): ",
                len(self.current_location.pois))
            return self.current_location.pois[poi_pick - 1].interact(self.current_location, self.discovered_maps)

    def interact_with_item(self):

        if len(self.player.inventory) == 0:
            return "You have no items to interact with. Find some first!"

        if len(self.player.inventory) == 1:
            return self.player.inventory[0].interact(self.current_location, self.discovered_maps)

        else:
            item_pick = self.request_input_int(
                "Which item from your inventory do you want to interact with? (Pick the number): ",
                len(self.player.inventory))
            return self.player.inventory[item_pick - 1].interact(self.current_location, self.discovered_maps)

    def log_ui(self, msg):
        self.game_message = msg

    def check_inventory_by_name(self, item_name) -> bool:
        for item in self.player.inventory:
            if item.name == item_name:
                return True
        return False

    def pick_up_item(self):
        # No items
        if len(self.current_location.items) == 0:
            return "There don't seem to be any items here..."

        # Remove item from location and add to inventory
        # Because there's only one item here, no need to ask the user which one
        if len(self.current_location.items) == 1:
            item = self.current_location.items.pop(0)
            self.player.inventory.append(item)
            return f"You picked up a [bold green]{item.name}[/bold green]!"

        # More than one option
        item_pick = self.request_input_int(
            "Which item do you want to pick up? (Pick the number): ",
            len(self.current_location.items))
        item = self.current_location.items.pop(item_pick - 1)
        self.player.inventory.append(item)
        return f"You picked up a [bold green]{item.name}[/bold green]!"
