# MacroMancer

## A Linux CLI application for Keyboard and Mouse Customization.


## System Dependencies

Before installing MacroMancer, please ensure that the following system packages are installed:

- **xbindkeys**
- **xdotool**
- **x11-utils**
- **xev**

## Python Dependencies

- **pyfiglet==1.0.2**
- **inquirerpy==0.3.4**
- **PyYAML==6.0.2**
- **rich==13.9.4**
- **prompt_toolkit==3.0.50**
- **pynput==1.7.7**

### Installation
*Arch Linux / Manjaro*
```bash
sudo pacman -S xbindkeys xorg-xev xdotool
```

*Debian-based*
```bash
sudo apt install xbindkeys x11-utils xdotool python3.12-venv python3-dev build-essential
```

*Fedora*
```bash
sudo dnf install xbindkeys xev xdotool gcc python3.12-devel
```

*openSUSE*
```bash
sudo zypper install xbindkeys xev xdotool
```

---
Depending on your distro, you may have to download a few additonal python packages, if not already installed.
Debian/Ubuntu:
```bash
sudo apt install 
```
Download the 
After installing the necessary system dependencies:
1. Create a virtual environment using python:
```bash
python -m venv .venv
```
2. Activate the virtual environment:
```bash
source .venv/bin/activate
```
Pip:
```bash
cd dist/
pip install MacroMancer
```

### Usage
>WARNING! If you have not followed the instructions up to this point, the program will most likely not work.
> Be sure to complete all the above steps before trying to proceed to running the application. 

Run `macromancer` from the command line.
You'll be presented with the Welcome Screen, press *Enter* to continue to the Main Menu.
The Main Menu has a list of different options:
- **Show**: Display current bindings.
- **Add**: Create a new binding.
- **Update**: Modify an existing binding.
- **Delete**: Remove a binding.
- **Save**: Persist changes to the configuration.
- **Apply**: Activate the saved configurations.
- **Help**: Display this help information.
- **License**: View licensing details.
- **Exit**: Quit the application.

### Testing
Tests must be run from the root directory to be able to follow the correct file paths.
