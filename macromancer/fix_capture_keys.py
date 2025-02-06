#!/usr/bin/env python
import os
import shutil
import subprocess
import yaml

from pynput import mouse
from pynput import keyboard

from rich.console import Console

console = Console()

def capture_keys(mode:str) -> str:
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
    return key_codes

if __name__ == "__main__":
    kc = capture_keys('combo')
    print(f"You typed: {kc}")