import pytest
from unittest.mock import MagicMock
from user_interface import UserInterface
from input_manager import InputManager

def test_display_menu():
    ui = UserInterface()
    ui.display_menu()

def test_display_message():
    ui = UserInterface()
    ui.display_message("Test message")

def test_get_user_input():
    input_manager = InputManager()
    input_manager.get_user_input = MagicMock(return_value="1")
    assert input_manager.get_user_input("Въведете своя избор: ") == "1"
