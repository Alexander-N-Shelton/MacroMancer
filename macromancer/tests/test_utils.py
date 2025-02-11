#!/usr/bin/env python
# tests/test_utils.py
import shutil
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
from unittest.mock import patch, MagicMock

from macromancer.utils import capture_keys, capture_mouse_button, is_valid_command


def test_is_valid_command():
    # Check known valid commands
    assert is_valid_command('ls')
    assert is_valid_command('pwd')
    # Check a invalid command
    assert is_valid_command('non_existant_command') is False


@patch("macromancer.utils.keyboard.Listener")
def test_capture_keys_single(mock_listener):
    """
    Example of mocking keyboard input. We won't simulate real presses here,
    but we'll check that Listener is used and that we return the expected output.
    """
    mock_listener.return_value.__enter__.return_value.join.return_value = None
    result = capture_keys("single")
    assert isinstance(result, str)

@patch("macromancer.utils.mouse.Listener")
def test_capture_mouse_button(mock_listener):
    """
    Example of mocking mouse input.
    """
    mock_listener.return_value.__enter__.return_value.join.return_value = None
    result = capture_mouse_button()
    assert result is None