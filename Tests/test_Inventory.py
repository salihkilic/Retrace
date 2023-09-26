from unittest import TestCase
from GameLogic.Inventory import Inventory, Item


class TestInventory(TestCase):

    def setUp(self):
        self.inventory = Inventory()

    def test_can_deposit_items(self):
        knife = Item("Knife", "Beautiful knife")
        self.inventory.deposit_item(knife)

        # Test if inventory contains a knife, but not a fork
        self.assertTrue(self.inventory.find_item("Knife"))
        self.assertFalse(self.inventory.find_item("Fork"))

    def test_can_take_items(self):
        spoon = Item("Spoon", "Beautiful Spoon")
        spork = Item("Spork", "Beautiful Spork")

        self.inventory.deposit_item(spoon)
        self.inventory.deposit_item(spork)

        # Test if we correctly deposited
        self.assertTrue(self.inventory.find_item("Spoon"))
        self.assertTrue(self.inventory.find_item("Spork"))

        # Take the spoon out
        test_item = self.inventory.take_item(self.inventory.find_item("Spoon"))

        # Spoon should be in test_item, Spork should still be in inventory
        self.assertFalse(self.inventory.find_item("Spoon"))
        self.assertEqual(self.inventory.find_item("Spork"), spork)
