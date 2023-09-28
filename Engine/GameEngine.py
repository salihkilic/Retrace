import time
import os
import sys
from Engine.locations import map1, map2


class GameEngine:

    def __init__(self):
        self.running = False
        self.discovered_maps = [map1, map2]
        self.current_map = map1
        self.current_location = map1.locations[0]
        self.game_message = None

    def run(self):
        self.running = True
        while self.running:
            self.clear_screen()
            self.draw_map()
            self.draw_location()
            # TODO Print out points of interest at this location
            player_action = self.request_input()
            self.handle_commands(player_action)

    def request_input(self):
        print(f'\n  {"--------- Last Action: " + self.game_message + " --------- " if self.game_message else " "}  ')
        print("What do you want to do: \n"
              "1) Go to location on map\n"
              "2) Travel to different map\n"
              "3) Pick up an item\n"
              "4) Interact with a point of interest\n"
              "5) Exit Game\n")
        time.sleep(0.5)
        return int(input("Please enter your number: "))

    def handle_commands(self, player_action):
        match player_action:
            case 1:
                self.goto_location()
                pass
            case 2:
                self.goto_map()
                pass
            case 3:
                # TODO Pick up an item at location (first display them etc)
                pass
            case 4:
                # TODO Interact with POI
                pass
            case 5:
                quit("\n ---------------------"
                     "\n Player exit from game"
                     "\n ---------------------")
            case _:
                self.game_message = "[ERROR] Something went wrong, try again..."

    def draw_location(self):
        pass

    def draw_map(self):
        print(self.current_map.ascii)
        print(self.current_location.location_ascii)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.2)

    def goto_location(self):
        print("What location do you want to move to on this map?")
        for num, loc in enumerate(self.current_map.locations):
            print(f"{num + 1}). {loc.name}")
        destination_pick = int(input("Enter your number: "))
        self.current_location = self.current_map.locations[destination_pick - 1]
        self.game_message = f"You traveled to the location: {self.current_location.name}"
        self.clear_screen()

    def goto_map(self):
        print("What map do you want to move to?")
        for num, loc in enumerate(self.discovered_maps):
            print(f"{num + 1}). {loc.name}")
        destination_pick = int(input("Enter your number: "))
        self.current_map = self.discovered_maps[destination_pick - 1]
        # We go to the first location of the new map as well
        self.current_location = self.current_map.locations[0]
        self.game_message = f"You traveled to the map: {self.current_map.name}"
        self.clear_screen()

