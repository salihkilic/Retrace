from unittest import TestCase

from GameLogic.Inventory import Item
from GameLogic.Location import BaseLocation, LocationAction
from _Old.GameLogic.Player import Player


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


class TestLocationAction(TestCase):
    def setUp(self):
        self.player = Player()
        self.player.inventory.deposit_item(Item("Stick", "A stick"))
        self.player.inventory.deposit_item(Item("Spear", "A spear"))

    def test_can_create_action_without_conditions(self):
        action = LocationAction("Action without condition")
        self.assertTrue(action.player_can_perform(self.player))

    def test_can_confirm_action_with_single_condition(self):
        action = LocationAction("Action with one condition",
                                [lambda player: self.player.has_item_by_str("Stick")])
        self.assertTrue(action.player_can_perform(self.player))

    def test_can_fail_action_with_single_condition(self):
        action = LocationAction("Failing action with one condition",
                                [lambda player: self.player.has_item_by_str("Shoe")])
        self.assertFalse(action.player_can_perform(self.player))

    def test_can_confirm_action_with_multiple_conditions(self):
        action = LocationAction("Action with one condition",
                                [lambda player: self.player.has_item_by_str("Stick"),
                                 lambda player: self.player.has_item_by_str("Spear")])
        self.assertTrue(action.player_can_perform(self.player))

    def test_can_fail_action_with_multiple_conditions(self):
        action = LocationAction("Failing action with one condition",
                                [lambda player: self.player.has_item_by_str("Shoe"),
                                 lambda player: self.player.has_item_by_str("Hat")])
        self.assertFalse(action.player_can_perform(self.player))

    def test_has_explored_location_condition(self):
        self.player.visit_location("Earth")
        action = LocationAction("Action based on visited location",
                                [lambda player: self.player.has_visited_location("Earth")])
        failing_action = LocationAction("Action based on visited location",
                                        [lambda player: self.player.has_visited_location("Moon")])
        self.assertTrue(action.player_can_perform(self.player))
        self.assertFalse(failing_action.player_can_perform(self.player))
