class Poi:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

        """
        A point of interest is simply something to look at or interact with
        
        It can be a door that unlocks a location
        Or a nice statue to look at
        """


class Item:
    def __init__(self, name: str):
        self.name = name
