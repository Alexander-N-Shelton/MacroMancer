# tests/test_device_manager.py
import pytest
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from unittest.mock import patch, mock_open
from macromancer.device_manager import DeviceManager

@pytest.mark.parametrize("config_path", ["macromancer/config/keyboard.yaml", "macromancer/config/mouse.yaml"])
@patch("builtins.open", new_callable=mock_open, read_data="Name: test_name\ncommand: test_command\ntrigger: test_trigger")
def test_load_config(mock_file, config_path):
    manager = DeviceManager(config_path)
    manager.load_config()
    assert manager.bindings["Name"] == "test_name"
    assert manager.bindings["trigger"] == "test_trigger"
    assert manager.bindings["command"] == "test_command"

@pytest.mark.parametrize("config_path", ["macromancer/config/keyboard.yaml", "macromancer/config/mouse.yaml"])
def test_return_bindings(config_path):
    manager = DeviceManager(config_path)
    manager.bindings = []
    returned = manager.return_bindings()
    assert returned == []

@pytest.mark.parametrize("config_path", ["macromancer/config/keyboard.yaml", "macromancer/config/mouse.yaml"])
def test_add_binding(config_path):
    manager = DeviceManager(config_path)
    manager.bindings = []  # Emulate having loaded an empty config
    updated = manager.add_binding("NewBind", "ls", "left")
    assert len(updated) == 1
    assert updated[0]["Name"] == "NewBind"
    assert updated[0]["command"] == "ls"
    assert updated[0]["trigger"] == "left"

@pytest.mark.parametrize("config_path", ["macromancer/config/keyboard.yaml", "macromancer/config/mouse.yaml"])
@patch.object(DeviceManager, 'load_config', return_value=None)
@patch("builtins.open", new_callable=mock_open)
def test_save_config(mock_file, _, config_path):
    manager = DeviceManager(config_path)
    manager.bindings = [{"Name": "SaveTest", "trigger": "left", "command": "echo test"}]
    manager.save_config()
    mock_file.assert_called_once_with(config_path, "w") # Make sure we opened the file for writing
    # Combine all writes into a single string
    written_data = ""
    for call_args in mock_file().write.call_args_list:
        written_data += call_args[0][0]

    assert "SaveTest" in written_data
