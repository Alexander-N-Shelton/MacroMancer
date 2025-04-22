# macromancer/device_manager.py

import yaml
import os

from rich.table import Table

from macromancer.utils import console, update_xbindkeys, apply_xbindkeys

class DeviceManager:
    """
    Manages device bindings configuration.

    Loads, saves, and updates binding configurations stored in a YAML file,
    and provides methods to display and apply these bindings.
    """
    def __init__(self, file_path: str):  # Initializes the DeviceManager.
        """
        Initializes the DeviceManager.

        Args:
            file_path (str): Path to the YAML configuration file.
        """
        path = os.path.abspath(os.path.dirname(__file__))
        config_path = os.path.join(path, 'config')
        self.file_path = os.path.join(config_path, file_path)
        self.bindings: list
        self.load_config()

    def load_config(self) -> None:  # Loads the configuration file.
        """Loads the configuration file and initializes bindings."""
        stream = open(self.file_path, 'r')
        self.bindings = yaml.safe_load(stream)
        stream.close()

    def return_bindings(self) -> list[dict]:  # Returns the bindings for the selected DeviceManager.
        """
        Returns the bindings for the selected DeviceManager.

        Returns:
            list[dict]: a list with each dict representing a separate binding.
        """
        return self.bindings
    
    def get_binding_names(self) -> list:  # Retrieves the names of all currently saved bindings.
        """
        Retrieves the names of all currently saved bindings.

        Returns:
            list: A list of binding names, or a string message if none exist.
        """
        if self.bindings is not None:
            names = []
            for bind in self.bindings:
                name = bind['Name']
                names.append(name)
            return names
        else:
            return "There are no saved bindings."

    def add_binding(self, name: str, command: str, trigger: str) -> list[dict]:  # Adds a new binding.
        """
        Adds a new binding.

        Args:
            name (str): The binding's name.
            command (str): The binding command (validated beforehand).
            trigger (str): The sequence of key or button presses.

        Returns:
            list[dict]: Updated list of bindings with the new binding added.
        """
        if self.bindings is None:
            self.bindings = []
        new_binding = {'Name': name, 'command': command, 'trigger': trigger}
        self.bindings.append(new_binding)
        return self.bindings
    
    def update_binding(self, name:str, command=None, trigger=None) -> list[dict]:  # Updates an existing binding.
        """
        Updates an existing binding.

        Args:
            name (str): The binding's name.
            command (str, optional): New command for the binding.
                Defaults to None (leaving the original command unchanged).
            trigger (str, optional): New trigger sequence.
                Defaults to None (leaving the original trigger unchanged).

        Returns:
            list[dict]: The list of bindings with the updated binding.
        """
        if self.bindings is not None:
            for binding in self.bindings:
                if binding['Name'] == name:
                    if trigger is None:
                        trigger = binding['trigger'] 
                    else:
                        binding['trigger'] = trigger
                    if command is None:
                        command = binding['command']
                    else:
                        binding['command'] = command
                    return self.bindings
        else:
            console.print("There are no saved bindings.")                

    def delete_binding(self, name: str) -> list[dict]:  # Delete an existing binding.
        """
        Deletes an existing binding.

        Args:
            name (str): The binding's name to delete.

        Returns:
            list[dict]: The list of bindings after deletion.
        """
        if self.bindings is not None:
            try:
                for i, binding in enumerate(self.bindings):
                    if binding['Name'] == name:
                        del self.bindings[i]
                        return self.bindings
            except KeyError as ke:
                print("There is no binding by that name")
        else:
            console.print("There are no saved bindings.")

    def display_bindings(self, bind_type:str) -> None:  # Displays current bindings in a formatted table.
        """
        Displays current bindings in a formatted table.

        Args:
            bind_type (str): The type of bindings (e.g., 'key' or 'mouse') to display.
        """
        if self.bindings is not None:
            table = Table(title=f'{bind_type} Bindings', title_justify='center', title_style='cyan', expand=True, show_header=True)
            table.add_column("Name", header_style='cyan', justify='left', style='cyan')
            table.add_column("Command", justify='center', style='green')
            table.add_column("Trigger", justify='center', style='green')
            for binding in self.bindings:
                table.add_row(f"{binding['Name']}", f"{binding['command']}", f"{binding['trigger']}")
                table.add_section()
            console.print(table)
        else:
            console.print("There are no saved bindings.", style='cyan')

    def save_config(self) -> None:  # Saves the current bindings to the configuration file.
        """
        Saves the current bindings to the configuration file.

        Writes the updated bindings list back to the YAML file specified by file_path.
        """
        file = open(self.file_path, 'w')
        print("Saving to file...")
        print(self.bindings)
        yaml.dump(self.bindings, file)
        file.close()
    
    @staticmethod
    def apply_config():  # Applies the system configuration changes.
        """
        Applies the system configuration changes.

        Calls the functions to update and apply the xbindkeys configuration.
        """
        update_xbindkeys()
        apply_xbindkeys()