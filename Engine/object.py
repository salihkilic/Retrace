from abc import ABC, abstractmethod


class Interactable(ABC):
    def __init__(self, name: str,
                 description: str,
                 hidden_item=None,
                 hidden_map=None):
        self.hidden_item = hidden_item
        self.hidden_map = hidden_map
        self.name = name
        self.description = description

    @abstractmethod
    def interact(self, location, discovered_maps: list) -> str:
        pass


class Item(Interactable):

    def __init__(self, name: str,
                 description: str,
                 hidden_item=None,
                 hidden_map=None):
        super().__init__(name, description, hidden_item, hidden_map)

    def interact(self, location, discovered_maps: list) -> str:
        if self.hidden_item:
            location.items.append(self.hidden_item)
            response_string = (f"You check the [bold green]{self.name}:[/bold green] {self.description}"
                               f" [bold green]a [bold green]{self.hidden_item.name}[/bold green] falls on the ground!")
            self.hidden_item = None
        elif self.hidden_map:
            discovered_maps.append(self.hidden_map)
            response_string = (f"You check the [bold green]{self.name}:[/bold green] {self.description} "
                               f"You found a map to: [bold green]{self.hidden_map.name}! [/bold green]")
            self.hidden_map = None
        else:
            response_string = (f"You check the [bold green]{self.name}[/bold green], {self.description}. "
                               f"[bold red]It doesn't seem like you can do anything else with it.[/bold red]")
        return response_string


class Poi(Interactable):
    def __init__(self, name: str,
                 description: str,
                 hidden_item=None,
                 hidden_map=None):
        super().__init__(name, description, hidden_item, hidden_map)

    def interact(self, location, discovered_maps: list) -> str:
        if self.hidden_item:
            location.items.append(self.hidden_item)
            response_string = (f"{self.description}. You also notice a[bold green] {self.hidden_item.name}! ["
                               f"/bold green] close to it!")
            self.hidden_item = None
        elif self.hidden_map:
            discovered_maps.append(self.hidden_map)
            response_string = (f"{self.description}."
                               f"[bold green] You also found a map to: {self.hidden_map.name}! [/bold green]")
        else:
            response_string = (f"{self.description}\n[bold red]It doesn't seem like you can do anything else with it.["
                               f"bold red]")
        return response_string
