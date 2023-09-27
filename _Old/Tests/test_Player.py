from unittest import TestCase

from GameLogic.Inventory import Inventory
from _Old.GameLogic.Player import Player


class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player()
        self.player.name_player("TestName")

    def test_can_create_player(self):
        self.assertIsInstance(self.player, Player)

    def test_has_inventory(self):
        self.assertIsInstance(self.player.inventory, Inventory)

    def test_has_name(self):
        self.assertEqual(self.player.name, "TestName")

    def test_has_correct_name(self):
        self.assertNotEqual(self.player.name, "Wrong Name")

    def test_can_change_player_name(self):
        self.assertEqual(self.player.name, "TestName")
        self.player.name_player("TestName2")
        self.assertNotEqual(self.player.name, "TestName")
        self.assertEqual(self.player.name, "TestName2")

    def test_player_has_visited_location(self):
        self.assertFalse(self.player.has_visited_location("Mountain"))
        self.player.visit_location("Mountain")
        self.assertTrue(self.player.has_visited_location("Mountain"))
