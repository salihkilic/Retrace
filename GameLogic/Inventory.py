class Item:
    name: str

    def __init__(self, name, description: str):
        self.description = description
        self.name = name


class Inventory:
    def __init__(self):
        self.items: list[Item] = []

    def take_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            raise Exception

    def deposit_item(self, item):
        if item not in self.items:
            self.items.append(item)
        else:
            raise Exception

    def find_item(self, item_name: str):
        for item in self.items:
            if item.name == item_name:
                return item
        else:
            return False
