#!/usr/bin/env python

shortcuts_file = 'config/shortcut_scheme.txt'
fhand = open(shortcuts_file, 'r')
lines = fhand.readlines()
commands = []
triggers = []
key_combos = {}
section_headers = []

def check_system_bindings():
    for line in lines:
        line = line.strip()
        if len(line) > 2:
            if line.startswith('['):
    #            section_headers.append(lines.index(line))
                print(line)
            else:
                line = line.split('=')
                command = line[0]
                trigger = line[1]
                if len(trigger) < 2:
                    continue
                else:
                    triggers.append(trigger)
                commands.append(command)
                key_combos[command] = trigger
    return triggers, commands, key_combos

t, c, kc = check_system_bindings()
