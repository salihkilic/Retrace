import unittest
from GameLogic.GameManager import Manager
from Scenes.StartScene import StartScene


class GameManagerIntegrations(unittest.TestCase):

    manager: Manager

    def test_if_game_manager_exists(self):
        self.manager = Manager()
        self.assertIsInstance(self.manager, Manager)


"""
What we should test:

PAY ATTENTION, We test INTEGRATION here. That means how different objects interact with EACH OTHER. 
Test every object and its functions in its own test file.

# Location
- GameManager exists
- Can load a location
- Can get its basic description
- Can get a full description, based on a secondary and tertiary object
- Can get a list of actions to be performed at the location

# Player
- Can get a list of locations the player can move to
- Can retrieve and item from the location and give it to the player

"""

if __name__ == '__main__':
    unittest.main()
