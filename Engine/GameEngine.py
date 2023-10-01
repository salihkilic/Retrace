import time
import os
import random

import simpleaudio
from rich import print
from Assets import items, locations
from Engine.player import Player
from Engine.game_ui import GameUI
from Engine.start_screen_ui import StartScreenUI
from Engine.end_screen_ui import EndScreenUI


class GameEngine:

    def __init__(self):
        self.running = False
        self.populate_hidden_items_and_maps()
        self.set_locations_needed_items_for_visit()
        self.discovered_maps = [locations.earth]
        self.current_map = locations.earth
        self.current_location = locations.earth.locations[0]
        self.game_message = "Welcome to Retrace: Forgotten Paths. Please select your first action..."
        self.start_screen = StartScreenUI()
        self.end_screen = EndScreenUI()
        self.ui = GameUI()
        self.player = Player()
        self.background_music = [simpleaudio.WaveObject.from_wave_file("Assets/music.wav"),
                                 simpleaudio.WaveObject.from_wave_file("Assets/music2.wav"),
                                 simpleaudio.WaveObject.from_wave_file("Assets/music3.wav"),
                                 simpleaudio.WaveObject.from_wave_file("Assets/music4.wav"),
                                 simpleaudio.WaveObject.from_wave_file("Assets/music5.wav")]
        self.music_player = None

    def run(self):
        self.running = True
        self.music_player = self.background_music[0].play()
        self.show_start_screen()
        self.ui = GameUI()
        while self.running:
            # Check if we reached end-game
            if items.memory_extractor in self.player.inventory:
                self.draw_end_scene()
            # Check if we are still playing music
            if not self.music_player.is_playing():
                # We grab a random song to play
                self.music_player = random.choice(self.background_music).play()
            self.draw_ui()
            player_action = self.request_input_int("Please enter your action (number): ", 6)
            self.handle_commands(player_action)

    def show_start_screen(self):
        self.clear_screen()
        self.start_screen.update_layout()
        input("Press enter to continue...")

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
                self.game_message = "[ERROR] You shouldn't have been able to pick this option. Blame the dev."

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
            return self.describe_location(
                f"You used the [bold green]{target_location.needs_item_name}[/bold green] and "
                f"traveled to the location: [bold green]"
                f"{self.current_location.name}[/bold green]")
        # If no item needed, let's just go!
        self.current_location = target_location
        return self.describe_location(f"You traveled to the location: {self.current_location.name}")

    def describe_location(self, header_msg: str):
        return f"{header_msg}\n\n{self.current_location.description}"

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
        # TODO If inventory contains the game winning item (memory core), go to end screen!
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

    def populate_hidden_items_and_maps(self):
        # We can only do this after imports and init because of circular imports otherwise.
        # TODO This is very ugly and hard-coded but to change this requires a quite drastic refactor later.

        # Earth
        # Office keycard earth->house->desk poi
        locations.earth.locations[0].pois[3].hidden_item = items.office_keycard
        # Spaceship keycard -> office -> office rooms poi
        locations.earth.locations[1].pois[1].hidden_item = items.spaceship_keycard
        # Moon MAP -> spaceport -> personal spaceship poi
        locations.earth.locations[3].pois[0].hidden_map = locations.moon
        # Memory Extractor -> office -> office rooms poi
        locations.earth.locations[2].pois[0].hidden_item = items.memory_extractor

        # Moon
        # Crowbar -> spaceport -> Utilities center poi
        locations.moon.locations[0].pois[1].hidden_item = items.crowbar
        # Military Base Keycard -> cafe -> backdoor
        locations.moon.locations[1].pois[2].hidden_item = items.military_keycard
        # Mars map on Military keycard item
        items.military_keycard.hidden_map = locations.mars

        # Mars
        # TODO Robot Remote -> Robot Center
        locations.mars.locations[1].pois[2].hidden_item = items.robot_remote
        # TODO Labs skeleton key -> forget labs
        locations.mars.locations[2].pois[1].hidden_item = items.labs_keycard

    def set_locations_needed_items_for_visit(self):
        # TODO This is very ugly and hard-coded but to change this requires a quite drastic refactor later.
        # Earth
        # Office -> Office key
        locations.earth.locations[1].needs_item_name = items.office_keycard.name
        locations.earth.locations[1].locked_reason = ("[bold red]The elevator to the offices does not respond to "
                                                      "your commands and you need a keycard.[/bold red]")
        # Lab -> Lab key
        locations.earth.locations[2].needs_item_name = items.labs_keycard.name
        locations.earth.locations[2].locked_reason = ("[bold red]The door does not open. It seems like it's locked "
                                                      "and you need a keycard.[/bold red]")
        # Spaceport -> Spaceship keycard
        locations.earth.locations[3].needs_item_name = items.spaceship_keycard.name
        locations.earth.locations[3].locked_reason = ("[bold red]The spaceport entrance has a keycard reader. It "
                                                      "seems like you need to own a spaceship to be able to enter.["
                                                      "/bold red]")

        # Moon
        # Cafe -> crowbar
        locations.moon.locations[1].needs_item_name = items.crowbar.name
        locations.moon.locations[1].locked_reason = ("[bold red]The door is boarded up. You probably need a tool to "
                                                     "open it back up.[/bold red]")
        # Mars
        # Military Base -> Mil base keycard
        locations.mars.locations[1].needs_item_name = items.military_keycard.name
        locations.mars.locations[1].locked_reason = ("[bold red]The military base has a secured entrance. You will "
                                                     "need [/bold red]")
        # TODO Forget Inc -> Robot remote
        locations.mars.locations[2].needs_item_name = items.robot_remote.name
        locations.mars.locations[2].locked_reason = ("[bold red]A robot is defending the entrance and attacking "
                                                     "anyone that comes closeby and you narrowly escape! You will "
                                                     "need some way of disableing or destroying the robot.[/bold red]")

    def draw_end_scene(self):
        self.clear_screen()
        self.end_screen.update_layout()
        input("Press enter to continue...")
        quit("\n ---------------------"
             "\n Player exit from game"
             "\n  Thanks for playing! "
             "\n ---------------------")

# TODO Do location items stick around when you move?
# TODO It would be really neat to have a game-start screen
# TODO Music? Based on location even?!?!
