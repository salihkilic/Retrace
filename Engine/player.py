from Engine.object import Item


class Player:
    def __init__(self):
        self.inventory: list[Item] = []