#!/usr/bin/env python
import logging

from pyfiglet import Figlet
from rich.prompt import Prompt, Confirm
from rich.console import Console
from rich.markdown import Markdown
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from macromancer.device_manager import DeviceManager
from macromancer.utils import capture_keys, capture_mouse_button, is_valid_command

logger = logging.getLogger(__name__)
logging.basicConfig(filename="macromancer_error.log", level=logging.ERROR)
# =========================================================================== #
class InteractiveCLI:
    """
    InteractiveCLI provides a simple command-line interface that welcomes the user,
    displays licensing information, and navigates to the main menu or exits.
    """
    def __init__(self):  # Initializes the InteractiveCLI instance.
        """
        Initializes the InteractiveCLI instance.

        - Sets the application version.
        - Loads license information.
        - Configures the console and banner using Figlet.
        - Initializes device managers for keyboard and mouse.
        - Displays the welcome message.
        """
        self.__version__ = '0.0.1'
        self.license_info = '''
            MacroMacner  Copyright (C) 2025  Alexander N. Shelton
    This program comes with ABSOLUTELY NO WARRANTY;
    for details view `License` in the Main Menu.
    This is free software, and you are welcome to redistribute it
    under certain conditions; view `License` for details.
        '''
        self.f = Figlet()
        self.console = Console(style='blue')
        self.managers = {
            'key': DeviceManager('macromancer/config/keyboard.yaml'),
            'mouse': DeviceManager('macromancer/config/mouse.yaml')
        }
        self.display_welcome_message()

    def display_welcome_message(self):  # Displays the welcome message with license info.
        """
        Displays the welcome message along with licensing info.

        Clears the console, prints the banner, license information, and a welcome message.
        Waits for the user to press Enter to proceed to the main menu or type 'q' to exit.
        """
        self.console.clear()
        self.console.print(self.f.renderText("MacroMancer"))
        self.console.print(f"[italic white]{self.license_info}[/italic white]")
        self.console.print("[bold]Welcome to the MacroMancer.[/bold]\n")
        self.console.print("[bold yellow]You can exit the program anytime by pressing 'Ctrl-Z'[/bold yellow]\n")
        self.console.rule(f"[bold yellow] Press `Enter` to go to the main menu or type q to exit [/bold yellow]", align='left')
        start = self.console.input("")
        if start == 'q':
            self.console.print("\n[bold yellow]Exiting the program...")
            self.console.print(self.f.renderText("Good Bye"))
            quit()
        else:
            self.run()
        
    def main_menu(self) -> str:  # Displays the main menu.
        """
        Displays the main menu and returns the selected option.

        Returns:
            str: The user's menu selection.
        """
        self.console.print(self.f.renderText("MacroMancer"))
        self.console.rule("[bold yellow] Main Menu [/bold yellow]")
        choices = [
            Choice('show', name="Show"),
            Choice('add', name="Add"),
            Choice('update', name="Update"),
            Choice('delete', name="Delete"),
            Choice('save', name="Save"),
            Choice('apply', name="Apply"),
            Choice ('help', name='Help'),
            Choice('license', name='License'),
            Choice('exit', name="Exit")
        ]
        result = inquirer.select(
            message="Select an option: ",
            choices=choices,
            multiselect=False,
            border=True,
        ).execute() 
        return result

    def ask_type(self) -> str:  # Prompts the user to select a binding type.
        """
        Prompts the user to select a binding type.

        Returns:
            str: The selected binding type.
        """
        bind_choices = [manager for manager in self.managers.keys()]
        bind_type = inquirer.select(message="What type of binding?", choices=bind_choices, multiselect=False, border=True).execute()
        return bind_type

    def ask_name(self, manager: DeviceManager):  # Prompts the user to select a binding name.
        """
        Prompts the user to select a binding name from the given manager.

        Args:
            manager (DeviceManager): The manager instance to retrieve binding names.

        Returns:
            str or None: The selected binding name or None if unavailable.
        """
        names = manager.get_binding_names()
        if type(names) == list:
            name_choices = [name for name in names]
            name = inquirer.select(message="Select the binding name: ", choices=name_choices, multiselect=False, border=True).execute()
            return name
        else:
            self.console.print(names)
            return None
    
    def ask_mode(self) -> str:  # Prompts the user to select a key recording mode.
        """
        Prompts the user to select a key recording mode.

        Returns:
            str: The chosen recording mode ('single' or 'combo').
        """
        mode_choices = [
            Choice('single', name='Single'),
            Choice('combo', name='Combo'),
        ]
        mode = inquirer.select(message="Select a key recording mode: ", choices=mode_choices, multiselect=False, border=True).execute()
        return mode

    def record_input(self, bind_type) -> str | int:  # Captures input based on the binding type.
        """
        Captures input based on the binding type.

        For 'key', it prompts for the recording mode and captures key input.
        For 'mouse', it captures mouse button input.

        Args:
            bind_type (str): The type of binding ('key' or 'mouse').

        Returns:
            The captured trigger input.
            list : keyboard keys captured
            int : button press captured
        """
        if bind_type == 'key':
            mode = self.ask_mode()
            trigger = capture_keys(mode)
        elif bind_type == 'mouse':
            trigger = capture_mouse_button()
        return trigger

    def return_to_menu(self) -> None:  # Prompt user to return to main menu.
        """
        Waits for the user to press Enter before returning to the main menu.
        """
        self.console.rule(f"[bold yellow] Press `Enter` to return to the main menu [/bold yellow]", align='left')
        self.console.input("")

    def show(self) -> None:  # Displays the bindings for a selected type.
        """
        Clears the console and displays the bindings for a selected binding type.
        """
        self.console.clear()
        self.console.rule(f"[bold yellow] Show Bindings [/bold yellow]")
        bind_type = self.ask_type()
        manager = self.managers[bind_type]
        manager.display_bindings(bind_type)
        self.return_to_menu()
    
    def update(self) -> None:  # Updates an existing binding.
        """
        Updates an existing binding.

        Prompts the user to select a binding and optionally update its trigger and command.
        """
        self.console.clear()
        self.console.rule(f"[bold yellow] Update Bindings [/bold yellow]")
        bind_type = self.ask_type()
        manager = self.managers[bind_type]
        name = self.ask_name(manager)
        if name is not None:
            if Confirm.ask(f"Change Trigger for {name}?", default=True):
                new_trigger = self.record_input(bind_type)
            else:
                new_trigger = None
            if Confirm.ask(f"Change Command for {name}?", default=True):
                while True:
                    new_command = Prompt.ask("Enter a new command: ")
                    if is_valid_command(new_command):
                        break
            else:
                new_command = None
            manager.update_binding(name, new_command, new_trigger)
            self.console.print(f"Updated binding: {name}")
        self.return_to_menu()

    def add(self) -> None:  # Adds a new binding.
        """
        Adds a new binding.

        Prompts the user for a binding name, command, and trigger input, then adds the binding.
        """
        self.console.clear()
        self.console.rule(f"[bold yellow] Add Bindings [/bold yellow]")
        bind_type = self.ask_type()
        manager = self.managers[bind_type]
        while True:
            name = Prompt.ask("Enter a name for your binding ")
            if len(name) <=1:
                self.console.print("You must enter at least 1 character for the name...")
            else:
                break
        while True:
            command = Prompt.ask("Enter a command for your binding ")
            if is_valid_command(command):
                break
        trigger = self.record_input(bind_type)
        manager.add_binding(name, command, trigger)
        self.console.print(f"Adding {bind_type} binding:\nName: {name}\nCommand: {command}\nTrigger: {trigger}.")
        self.return_to_menu()

    def delete(self) -> None:  # Deletes a binding.
        """
        Deletes a binding.

        Prompts the user to select a binding to delete and confirms the deletion.
        """
        self.console.clear()
        self.console.rule(f"[bold yellow] Delete Bindings [/bold yellow]")
        bind_type = self.ask_type()
        manager = self.managers[bind_type]
        name = self.ask_name(manager)
        if name is not None:
            if Confirm.ask(f"Delete binding {name}?", default=True):
                manager.delete_binding(name)
                self.console.print(f"Binding {name} was deleted successfully.")
            else:
                self.console.print("No bindings were deleted.")
        else:
            self
        self.return_to_menu()
    
    def save(self) -> None: # Saves the configured bindings.
        """
        Saves the configured bindings.

        Clears the console and, upon user confirmation, saves changes for both key and mouse bindings.
        """
        self.console.clear()
        self.console.rule(f"[bold yellow] Save Bindings [/bold yellow]")
        if Confirm.ask("Save Changes?", default=True):
            self.managers['key'].save_config()
            self.managers['mouse'].save_config()
            self.console.print("Changes saved.\nTo apply these changes select `Apply` from the main menu.")
        else:
            self.console.print("[bold yellow] No changes have been saved.[/bold yellow]")
        self.return_to_menu()

    def apply(self) -> None:  # Applies the configured bindings.
        """
        Applies the configured bindings.

        Clears the console, applies the configuration, and waits for user input to return to the main menu.
        """
        self.console.clear()
        DeviceManager.apply_config()
        self.console.rule(f"[bold yellow] Apply Bindings [/bold yellow]")
        self.console.print("Your configurations have been applied.")
        self.return_to_menu()

    def help(self) -> None:  # Displays help documentation.
        """
        Displays help documentation.

        Reads and renders the help markdown from 'docs/help.md' and waits for user input to return to the main menu.
        """
        with open("docs/help.md") as readme:
            markdown = Markdown(readme.read())
            self.console.print(markdown)
        self.return_to_menu()

    def license_menu(self) -> None:  # Displays licensing information.
        """
        Displays licensing information.

        Allows the user to view either the warranty disclaimer or copyright conditions.
        """

        license_warranty = '''
   Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
'''
        copyright_conditions = '''
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

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''
        self.console.clear()
        self.console.rule(f"[bold yellow] Licensing Information [/bold yellow]")
        choices = [
            Choice('w', name='Warranty'),
            Choice('c', name='Conditions'),
        ]
        license_section = inquirer.select(message="Select an option to view the corresponding section of the license: ", choices=choices, multiselect=False).execute()
        if license_section == 'w':
            self.console.print(license_warranty)
            self.return_to_menu()
        elif license_section == 'c':
            self.console.print(copyright_conditions)
            self.return_to_menu()
        
    def exit(self) -> None:  # Exits the application.
        """
        Exits the application.

        Clears the console, optionally saves changes, and then terminates the program.
        """
        self.console.clear()
        self.console.rule(f"[bold yellow] Save Bindings [/bold yellow]")
        if Confirm.ask("Save Changes?", default=True):
            self.managers['key'].save_config()
            self.managers['mouse'].save_config()
            self.console.print("Changes saved.\nTo apply these changes select `Apply` from the main menu.")
        else:
            self.console.print("[bold yellow] No changes have been saved.[/bold yellow]")
        self.console.print(self.f.renderText("Good Bye"), style='cyan')
        quit(code=0)

    def run(self) -> None:  # Runs the main CLI loop.
        """
        Runs the main CLI loop.

        Continuously displays the main menu and processes the user's selections.
        """
        while True:
            self.console.clear()
            result = self.main_menu()
            if result == 'show':
                self.show()
            elif result == 'add':
                self.add()
            elif result == 'update':
                self.update()
            elif result == 'delete':
                self.delete()
            elif result == 'save':
                self.save()
            elif result == 'apply':
                self.apply()
            elif result == 'help':
                self.help()
            elif result == 'license':
                self.license_menu()
            elif result == 'exit':
                self.exit()
