# tests/test_interactive_cli.py
import pytest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from unittest.mock import patch, MagicMock
from InquirerPy.base.control import Choice

from macromancer.interactive_cli import InteractiveCLI

@pytest.fixture
def mock_device_manager():
    """Mock DeviceManager so we don't deal with real YAML."""
    with patch("macromancer.interactive_cli.DeviceManager") as mock_mgr:
        # Each DeviceManager instance can have a mock bindings list
        instance = MagicMock()
        instance.bindings = []
        instance.get_binding_names.return_value = ["TestBinding"]
        mock_mgr.return_value = instance
        yield mock_mgr

@pytest.fixture
def mock_inquirer_select(monkeypatch):
    """
    A helper that lets us define what "inquirer.select(...).execute()" returns
    in a given test scenario.
    """
    def _set_return_value(value):
        # We'll patch inquirer.select() so .execute() returns 'value'
        def fake_select(*args, **kwargs):
            class FakeSelect:
                def execute(self):
                    return value
            return FakeSelect()
        monkeypatch.setattr("InquirerPy.inquirer.select", fake_select)
    return _set_return_value

def test_quit_at_welcome(monkeypatch):
    """
    The user types 'q' immediately at the welcome prompt, so we never reach the main menu.
    We expect the program to call quit(), which raises SystemExit in a test environment.
    """
    # Force input to be 'q' at the welcome prompt.
    monkeypatch.setattr("rich.console.Console.input", lambda *_: "q")

    with pytest.raises(SystemExit):
        InteractiveCLI()

def test_exit_from_main_menu(mock_device_manager, monkeypatch):
    """
    The user presses Enter at the welcome prompt (skipping 'q'),
    then chooses 'exit' from the main menu.
    We expect the program to call quit() and raise SystemExit.
    """
    # We'll simulate two user inputs:
    # 1) Press Enter at the welcome
    # 2) Then "exit" at the main menu (from inquirer.select)
    # 
    # The welcome prompt uses Console.input, so patch that to return "" (Enter).
    monkeypatch.setattr("rich.console.Console.input", lambda *args, **kwargs: "")

    # Then patch inquirer.select() so .execute() returns 'exit' when main_menu() is called.
    def fake_select(*args, **kwargs):
        class FakeSelect:
            def execute(self):
                return 'exit'
        return FakeSelect()

    monkeypatch.setattr("InquirerPy.inquirer.select", fake_select)

    with pytest.raises(SystemExit):
        InteractiveCLI()


def test_main_menu_show(mock_device_manager, monkeypatch):
    # 1) Press Enter at the welcome prompt (instead of typing 'q')
    monkeypatch.setattr("rich.console.Console.input", lambda *args, **kwargs: "")

    # We'll iterate over three responses for "inquirer.select().execute()":
    # 1) 'show' -> main_menu
    # 2) 'key'  -> ask_type inside show()
    # 3) 'exit' -> main_menu called again, to exit the loop
    select_responses = iter(["show", "key", "exit"])
   
    def fake_select(*args, **kwargs):
        class FakeSelect:
            def execute(_self):
                return next(select_responses)
        return FakeSelect()


    monkeypatch.setattr("InquirerPy.inquirer.select", fake_select)

    # Expect SystemExit after picking 'exit'
    with pytest.raises(SystemExit):
        InteractiveCLI()

    # If we got here without a KeyError or StopIteration,
    # it means we successfully handled 'show', then 'key', then 'exit'.

def test_add_binding(mock_device_manager, monkeypatch):
    # 1) Skip welcome screen by pressing Enter (empty string).
    monkeypatch.setattr("rich.console.Console.input", lambda *args, **kwargs: "")

    # 2) We'll need three returns from inquirer.select:
    #    - "add" (main menu choice)
    #    - "key" (which bind type)
    #    - "combo" (which recording mode)
    select_responses = iter(["add", "key", "combo", "exit"])

    def fake_select(*args, **kwargs):
        class FakeSelect:
            def execute(_self):
                return next(select_responses)
        return FakeSelect()

    # Patch inquirer.select so every time it's called, it returns 
    # a FakeSelect object whose execute() yields the next item above.
    monkeypatch.setattr("InquirerPy.inquirer.select", fake_select)

    # 3) For Prompt.ask calls (name, command), give "test_binding" and "ls".
    prompt_responses = iter(["test_binding", "ls"])
    def fake_prompt_ask(prompt_text):
        return next(prompt_responses)

    monkeypatch.setattr("rich.prompt.Prompt.ask", fake_prompt_ask)

    # 4) Finally, patch capture_keys so it returns "ctrl+a+esc".
    with patch("macromancer.interactive_cli.capture_keys", return_value="ctrl+a"):
        with pytest.raises(SystemExit):
            # The CLI will now:
            #  - Press Enter at welcome
            #  - main_menu() -> "add"
            #  - ask_type() -> "key"
            #  - Prompt.ask("Enter a name...") -> "test_binding"
            #  - Prompt.ask("Enter a command...") -> "ls"
            #  - ask_mode() -> "combo"
            #  - capture_keys() -> "ctrl+a+esc"
            #  - Then it finishes adding and goes back to the main menu loop.
            #  - Finally it exits the program.
            cli = InteractiveCLI()
            instance = mock_device_manager.return_value
            instance.add_binding.assert_called_once_with("test_binding", "ls", "ctrl+shift+a")