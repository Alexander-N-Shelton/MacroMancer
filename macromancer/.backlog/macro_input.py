#!/usr/bin/env python
# macro_input.py
# Requires root privelages to run, so will not include it in project
# Search for another way to capture and record all input without root level access.

import time
import json
import pynput.mouse as pynput_mouse
import pyautogui
import keyboard

# Get screen resolution
screen_width, screen_height = pyautogui.size()
    
def record(filename):
    print("Recording started. Move the mouse around, perform actions, and type on the keyboard. Press Ctrl + C to stop.")
    actions = []
    previous_time = time.time()  # Initialize previous_time

    # Initialize the mouse listener for scroll and press events
    def on_move(x, y):
        if 0 <= x < screen_width and 0 <= y < screen_height:
            actions.append({
                "action": "move",
                "position": (x, y),
                "time_diff": time_diff
            })

    def on_click(x, y, button, pressed):
        if 0 <= x < screen_width and 0 <= y < screen_height:
            actions.append({
                "action": "press" if pressed else "release",
                "button": str(button),
                "position": (x, y),
                "time_diff": time_diff
            })

    def on_scroll(x, y, dx, dy):
        if 0 <= x < screen_width and 0 <= y < screen_height:
            actions.append({
                "action": "scroll",
                "position": (x, y),
                "scroll": dy,
                "time_diff": time_diff
            })

    def on_key_event(event):
        actions.append({
            "action": "key",
            "key": event.name,
            "event_type": event.event_type,
            "time_diff": time_diff
        })

    listener = pynput_mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    listener.start()

    keyboard.hook(on_key_event)

    try:
        while True:
            current_time = time.time()
            time_diff = current_time - previous_time

            # Get the current mouse position
            x, y = pyautogui.position()

            # Keep the mouse within the screen boundaries
            x = max(0, min(x, screen_width - 1))
            y = max(0, min(y, screen_height - 1))


            time.sleep(0.05)  # Adjusted sleep time for smoother recordings


    except KeyboardInterrupt:
        print("Recording stopped.")
        listener.stop()
        keyboard.unhook_all()

        with open(filename, 'w') as file:
            json.dump(actions, file)


# Function to replay mouse and keyboard actions
def replay(filename, key_delay=0.1):
    with open(filename, 'r') as file:
        actions = json.load(file)
        print("Replaying mouse movements and keyboard inputs...")

        # Variables for double click detection
        last_click_time = 0
        double_click_threshold = 0.3  # Adjust this threshold as needed for your scenario

        for i in range(len(actions)):
            action = actions[i]
            if action["action"] == "move":
                # Use mouse.move for smooth movement at normal speed
                pyautogui.move(action["position"][0], action["position"][1], duration=0.00001)
            elif action["action"] == "press":
                current_time = action["time_diff"]

                # Check for double click
                if current_time - last_click_time <= double_click_threshold:
                    if action["button"] == "Button.left":
                        pyautogui.mouseDown(button='left')
                        print("double click")
                    elif action["button"] == "Button.right":
                        pyautogui.mouseDown(button='right')
                        print("double right click")
                else:
                    if action["button"] == "Button.left":
                        pyautogui.mouseDown(button='left')
                        print("holding mode")
                    elif action["button"] == "Button.right":
                        pyautogui.mouseDown(button='right')
                        print("holding right mode")

                last_click_time = current_time

            elif action["action"] == "release":
                if action["button"] == "Button.left":
                    pyautogui.mouseUp(button='left')
                    print("normal click")
                elif action["button"] == "Button.right":
                    pyautogui.mouseUp(button='right')
                    print("normal right click")

            elif action["action"] == "scroll":
                # Adjust the sleep time based on the duration of the scroll action
                time.sleep(0.01)
                pyautogui.scroll(action['scroll'])

            elif action["action"] == "key":
                if action["event_type"] == "down":
                    keyboard.press(action["key"])
                    print(f"Key pressed: {action['key']}")
                elif action["event_type"] == "up":
                    keyboard.release(action["key"])
                    print(f"Key released: {action['key']}")

                # Introduce a delay between key presses
                time.sleep(key_delay)

        print("Replay complete.")
