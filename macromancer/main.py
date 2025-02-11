#!/usr/bin/env python
# main.py
'''    
    MacroMancer. A CLI application for binding keys and buttons.
    Copyright (C) 2025 Alexander N. Shelton

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
'''
def main():
    from macromancer.interactive_cli import InteractiveCLI
    app = InteractiveCLI()

if __name__ == "__main__":
    main()