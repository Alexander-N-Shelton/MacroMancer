# MacroMancer

## A CLI application.


## System Dependencies

Before installing MacroMancer, please ensure that the following system packages are installed:

- **xbindkeys**
- **xdotool**
- **x11-utils**

## Python Dependencies

- **pyfiglet==1.0.2**
- **inquirerpy==0.3.4**
- **PyYAML==6.0.2**
- **rich==13.9.4**
- **prompt_toolkit==3.0.50**
- **pynput==1.7.7**

### Installation
*Arch Linux / Manjaro*
`sudo pacman -S xbindkeys xorg-xev xdotool`

*Debian-based*
`sudo apt install xbindkeys x11-utils xdotool`

*Fedora*
`sudo dnf install xbindkeys xorg-x11-utils xdotool`

*openSUSE*
`sudo zypper install xbindkeys xev xdotool`

---
After installing the necessary system dependencies, create a virtual environment using python:
`python -m venv .venv`
Activate the virtual environment:
Linux:
`source .venv/bin/activate`
Windows:
`.venv/Scripts/activate`

Pip:
`cd dist/`
`pip install MacroMancer`


### Usage


### Testing
Tests must be run from the root directory to be able to follow the correct file paths.
