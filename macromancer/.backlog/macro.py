#!/usr/bin/env python
# macro.py
import argparse
from macro_input import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mouse and Keyboard Recorder/Replayer')
    parser.add_argument('command', choices=['record', 'replay'], help='Choose command: record or replay')
    parser.add_argument('--file', default='mouse_keyboard_actions.json',
                        help='File to save mouse and keyboard actions (default: mouse_keyboard_actions.json)')
    args = parser.parse_args()

    if args.command == 'record':
        record(args.file)
    elif args.command == 'replay':
        replay(args.file)
