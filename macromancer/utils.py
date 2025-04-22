# macromancer/utils.py

import os
import shutil
import subprocess
import yaml

from pynput import mouse
from pynput import keyboard

from rich.console import Console

console = Console()

def capture_keys(mode:str) -> str:  # Captures the keycode(s) for keys pressed.
    """Captures the keycode(s) for keys pressed by the user.

    Args:
        mode (str): Capture mode. 'single' captures one key; 'combo' captures up to 4 keys.

    Returns:
        str: The captured keycodes joined by '+'.
    """
    keys_captured = []
    console.rule("[bold yellow] Press a key to capture their keycodes... [/bold yellow]")
    console.print("Press 'ESC' to exit capture.", justify='center', style='red')
    
    def on_press(key):
        try:
            key = key.char
        except AttributeError:
            key = str(key)
        if key != keyboard.Key.esc:
            keys_captured.append(key)
        if mode == 'single':
            if len(keys_captured) >= 1:
                return False
        elif mode == 'combo':
            if len(keys_captured) >= 4:
                return False
        elif mode == 'm':
            print(key)
        else:
            print("Not a valid mode.")
    
    def on_release(key):
        if key == keyboard.Key.esc:
            keys_captured.pop()
            return False
        
    with keyboard.Listener(
        on_press=on_press, 
        on_release=on_release) as listener:
        listener.join()
    key_codes = []

    for key_code in keys_captured:
        key = key_code.split('.')
        if len(key) > 1:
            key = key[1]
        else:
            key = key[0]
        key_codes.append(key)
    key_codes = '+'.join(key_codes)
    if '+esc' == key_codes[-4:]:
        key_codes = key_codes[:-4]
    return key_codes

def capture_mouse_button() -> int:  # Captures a single mouse button press.
    """
    Listens for a single mouse button press and returns its mapped code.
    
    Returns:
        int: The captured mouse button code.
    """
    console.rule("[bold yellow] Press a mouse button to capture it's code keycodes... [/bold yellow]")
    # Map mouse.Button objects to numeric codes
    MOUSE_BUTTON_MAPPING = {
        mouse.Button.left:          1,
        mouse.Button.middle:        2,
        mouse.Button.right:         3,
        mouse.Button.button8:       8,
        mouse.Button.button9:       9
    }

    clicked_button_code = [None]

    def on_click(x, y, button, pressed):
        if pressed:
            # If button is recognized in our mapping, store its code
            clicked_button_code[0] = MOUSE_BUTTON_MAPPING.get(button, None)
            # Stop listener as soon as one button press is captured
            return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
        
    return clicked_button_code[0]

def is_valid_command(command: str) -> bool:  # Checks if a command is valid.
    """
    Tests if a command is valid.

    Args:
        command (str): The command to be tested.

    Returns:
        bool: true or false indicating if the command is valid.
    """
    return shutil.which(command) is not None

def keyboard_config() -> list:  # Configures saved keyboard configurations formatted for xbindkeys.
    """
    Configures saved keyboard configurations formatted for xbindkeys.
    
    Returns:
        list: The formatted binding strings.
    """
    path = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(path, 'config')
    file_path = os.path.join(config_path, "keyboard.yaml")
    key_map = build_keycode_map()
    stream = open(file_path, 'r')
    bindings = yaml.safe_load(stream)
    stream.close()
    new_bindings = []
    if bindings is not None:
        for binding in bindings:
            name = binding['Name']
            command = binding['command']
            trigger = binding['trigger']
            keycodes = []
            keys = trigger.split('+')
            for key in keys:
                key_code = key_map.get(key)
                if key_code is None:
                    key_code = key_map.get(key.lower())
                key_code = str(key_code)
                keycodes.append(key_code)
            codes = "+".join(keycodes)
            cmd = f"\"{command}\""
            trig = f"  {codes}"
            new_binding = f"""# {name}
{cmd}
{trig}
\n"""
            new_bindings.append(new_binding)
    return new_bindings

def mouse_config() -> list:  # Configures saved mouse configurations formatted for xbindkeys.
    """
    Configures the saved mouse configurations by formatting
    them in a way that can be used by `xbindkeys` including
    both trigger and command.
    
    Returns:
        list: The formatted bindings.
    """
    path = os.path.abspath(os.path.dirname(__file__))
    config_path = os.path.join(path, 'config')
    file_path = os.path.join(config_path, "mouse.yaml")
    stream = open(file_path, 'r')
    bindings = yaml.safe_load(stream)
    stream.close()
    new_bindings = []
    if bindings is not None:
        for binding in bindings:
            name = binding['Name']
            command = binding['command']
            trigger = binding['trigger']
            cmd = f"\"{command}\""
            button_code = f"  b:{trigger}"
            new_binding = f"""# {name}
{cmd}
{button_code}\n"""
            new_bindings.append(new_binding)
    return new_bindings

# Special key mappings for keys that are represented
# differently in xmodmap than in pynput.
special_keys = {
    "!": "exclam",
    "@": "at",
    "$": "dollar",
    "#": "numbersign",
    "%": "percent",
    "^": "asciicircum",
    "&": "ampersand",
    "*": "asterisk",
    "(": "parenleft",
    ")": "parenright",
    "-": "minus",
    "_": "underscore",
    "=": "equal",
    "+": "plus",
    "{": "bracketleft",
    "}": "bracketright",
    ";": "semicolon",
    ":": "colon",
    "'": "apostrophe",
    "\"": "quotedbl",
    "`": "grave",
    "~": "aciitilde",
    "\\": "backslash",
    "|": "bar",
    ",": "comma",
    "<": "less",
    ".": "period",
    "/": "slash",
    "?": "question",
    'alt': "Alt",
    'alt_gr': 'Alt',
    'cmd': "Mod4",
    'cmd_r': "Mod4",
    'ctrl': "Control",
    'ctrl_r': "Control",
    'enter': 'Return',
    'esc': 'Escape',
    'f13': None,
    'f14': None,
    'f15': None,
    'f16': None,
    'f17': None,
    'f18': None,
    'f19': None,
    'f20': None,
    'page_down': "Prior",
    'page_up': "Next",
    'shift': "Shift",
    'media_play_pause': "XF86AudioPlay",
    'media_volume_mute': "XF86AudioMute",
    'media_volume_down': "XF86AudioLowerVolume",
    'media_volume_up': "XF86AudioRaiseVolume",
    'media_previous': "XF86AudioPrev", 
    'media_next': "XF86AudioNext",
    'print_screen': "Print",
}

def build_keycode_map() -> dict:  # Maps pynput keys to xmodmap.
    """
    Maps pynput keys to xmodmap by parsing `xmodmap -pke` output.
    
    Returns:
        dict: The keycode map.
    """
    output = subprocess.check_output(["xmodmap", "-pke"], text=True)

    key_map = {}
    for key, code in special_keys.items():
        key_map[key] = code
    for line in output.splitlines():
        # Each line looks like: "keycode  24 = q Q q Q"
        if not line.startswith("keycode"):
            continue

        # Split into "keycode 24" and "q Q q Q"
        line = line.split(" = ", 1)
        try:
            left, right = line[0], line[1]
        except IndexError as IE:
            continue

        # The right side has one or more names, e.g. "q Q q Q" or "Escape NoSymbol Escape"
        names = right.strip().split()
        for name in names:
            # Skip 'NoSymbol'
            if name == "NoSymbol":
                continue
            # Store a mapping in lowercase    
            key_map[name.lower()] = name

    return key_map

def update_xbindkeys() -> None:
    """
    Writes the current configurations to `~/.xbindkeysrc`.
    """
    path = os.path.join(os.path.expanduser("~"), ".xbindkeysrc")
    kc = keyboard_config()
    mc = mouse_config()
    marker_start = "### MacroMancer Start ###"
    marker_end   = "### MacroMancer End ###"

    # Build new MacroMancer block
    custom_config = [f"{marker_start}\n"]
    custom_config.extend(kc)
    custom_config.extend(mc)
    custom_config.append(f"{marker_end}\n")

    # Read current config
    try:
        with open(path, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    # Strip out old MacroMancer block
    updated_lines = []
    in_block = False
    for line in lines:
        if marker_start in line:
            in_block = True
            continue
        if marker_end in line:
            in_block = False
            continue
        if not in_block:
            updated_lines.append(line)

    # Insert the new block at the end
    updated_lines.append("\n")  # Optional: ensure spacing
    updated_lines.extend(custom_config)

    # Write the new config
    with open(path, "w") as f:
        f.writelines(updated_lines)

def apply_xbindkeys() -> None:  # Kills and then restarts xbindkeys.
    """Kills and then restarts xbindkeys."""
    subprocess.run(['killall', 'xbindkeys'], stdout=False)
    subprocess.run(['xbindkeys'])

kc_map = build_keycode_map()
print(kc_map.get('i'))