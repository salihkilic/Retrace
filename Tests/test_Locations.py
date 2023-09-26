from unittest import TestCase

from GameLogic.Inventory import Item
from GameLogic.Locations import BaseLocation


class MockLocation(BaseLocation):

    def room_description(self):
        return "Mock Basic Description"

    def background_image(self):
        return "Mock Image Path"

    def background_music(self):
        return "Mock Music Path"


class TestLocation(TestCase):

    def setUp(self):
        self.location = MockLocation()
        self.inventory = self.location.location_inventory

    def test_has_basic_description(self):
        self.assertEqual(self.location.room_description(), "Mock Basic Description")

    def test_has_background_music_path(self):
        self.assertEqual(self.location.background_music(), "Mock Music Path")

    def test_has_background_image_path(self):
        self.assertEqual(self.location.background_image(), "Mock Image Path")

    def test_can_build_complex_description_with_one_item(self):
        self.inventory.deposit_item(Item("Item1", "desc 1"))
        complex_description = "You see a desc 1"
        self.assertEqual(complex_description, self.location.item_descriptions())

    def test_can_build_complex_description_with_two_items(self):
        self.inventory.deposit_item(Item("Item1", "desc 1"))
        self.inventory.deposit_item(Item("Item2", "desc 2"))
        complex_description = "You see a desc 1 and a desc 2"
        self.assertEqual(complex_description, self.location.item_descriptions())

    def test_can_build_complex_description_with_three_items(self):
        self.inventory.deposit_item(Item("Item1", "desc 1"))
        self.inventory.deposit_item(Item("Item2", "desc 2"))
        self.inventory.deposit_item(Item("Item2", "desc 3"))
        complex_description = "You see a desc 1, a desc 2 and a desc 3"
        self.assertEqual(complex_description, self.location.item_descriptions())

    def test_can_build_complex_description_with_four_items(self):
        self.inventory.deposit_item(Item("Item1", "desc 1"))
        self.inventory.deposit_item(Item("Item2", "desc 2"))
        self.inventory.deposit_item(Item("Item2", "desc 3"))
        self.inventory.deposit_item(Item("Item2", "desc 4"))
        complex_description = "You see a desc 1, a desc 2, a desc 3 and a desc 4"
        self.assertEqual(complex_description, self.location.item_descriptions())

    # TODO Describe sublocations in complex description
