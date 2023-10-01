from Engine.object import Item


class Player:
    name: str

    def __init__(self):
        self.inventory: list[Item] = []
