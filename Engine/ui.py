from rich.align import Align
from rich.layout import Layout
from rich.padding import Padding
from rich.panel import Panel
from rich import print

from Engine.location import Location
from Engine.object import Poi, Item


class GameUI:
    def __init__(self):
        self.layout = Layout(name="Retrace")

    def make_layout(self, location: Location, map_ascii, game_message, player):
        self.layout.split(Layout(name="header", size=5),
                          Layout(name="top", ratio=5),
                          Layout(name="bottom", ratio=2),
                          Layout(name="footer", size=10)
                          )

        # Split top into two columns
        self.layout["top"].split_row(
            Layout(self.create_location_panel(location.location_ascii), name="locationP"),
            Layout(self.create_map_panel(map_ascii), name="mapP"))

        # Split bottom into four columns
        (self.layout["bottom"].split_row(
            Layout(self.create_user_actions_panel(), name="useractionP"),
            Layout(self.create_poi_panel(location.pois), name="poiP"),
            Layout(self.create_item_panel(location.items), name="itemP"),
            Layout(self.create_inventory_panel(player.inventory), name="inventoryP")))

        self.layout["footer"].update(self.create_game_message_panel(game_message))
        self.layout["header"].update(self.create_header_panel())

    def update_layout(self, location, map_ascii, game_message, player):
        self.make_layout(location, map_ascii, game_message, player)
        print(self.layout)

    def create_location_panel(self, location_ascii) -> Panel:
        return Panel(Align(location_ascii, align="center", vertical="middle"), title="Location")

    def create_map_panel(self, map_ascii) -> Panel:
        return Panel(Align(map_ascii, align="center", vertical="middle"), title="Map")

    def create_game_message_panel(self, msg) -> Panel:
        return Panel(Align(f"[bold cyan]{msg}[/bold cyan]", align="center", vertical="middle"))

    def create_user_actions_panel(self) -> Panel:
        return Panel(Align("""
        1) Go to location on map
        2) Travel to different map
        3) Interact with an item
        4) Pick up an item
        5) Interact with a POI
        6) Exit Game
        """, align="left", vertical="middle"), title="Actions")

    def create_poi_panel(self, pois: list[Poi]) -> Panel:
        if pois:
            poi_string = ""
            for num, poi in enumerate(pois):
                poi_string += f"{num + 1}) {poi.name} \n"
        else:
            poi_string = "There are no points of interest at this location."
        return Panel(Align(poi_string, align="center", vertical="middle"), title="Points of Interest")

    def create_item_panel(self, items: list[Item]) -> Panel:
        if items:
            item_string = ""
            for num, item in enumerate(items):
                item_string += f"{num + 1}) {item.name} \n"
        else:
            item_string = "You haven't found any noteable items at this location."
        return Panel(Align(item_string, align="center", vertical="middle"), title="Location Items")

    def create_inventory_panel(self, inventory: list[Item]) -> Panel:
        if inventory:
            item_string = ""
            for num, item in enumerate(inventory):
                item_string += f"{num + 1}) {item.name} \n"
        else:
            item_string = "You don't have anything in your inventory yet."
        return Panel(Align(item_string, align="center", vertical="middle"), title="Inventory")


    def create_header_panel(self) -> Panel:
        header_logo = """[bold cyan]╦═╗┌─┐┌┬┐┬─┐┌─┐┌─┐┌─┐       ╔═╗┌─┐┬─┐┌─┐┌─┐┌┬┐┌┬┐┌─┐┌┐┌  ╔═╗┌─┐┌┬┐┬ ┬┌─┐
╠╦╝├┤  │ ├┬┘├─┤│  ├┤   ───  ╠╣ │ │├┬┘│ ┬│ │ │  │ ├┤ │││  ╠═╝├─┤ │ ├─┤└─┐
╩╚═└─┘ ┴ ┴└─┴ ┴└─┘└─┘       ╚  └─┘┴└─└─┘└─┘ ┴  ┴ └─┘┘└┘  ╩  ┴ ┴ ┴ ┴ ┴└─┘[/bold cyan]"""
        return Panel(Align(header_logo, align="center", vertical="middle"))



