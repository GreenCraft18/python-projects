import subprocess # Imports <subprocess> for command results.
import os # Imports <os> for OS commands.
import sys
from turtle import clear # idk.
sys.path

# Starting Code
print("Welcome to the custom Python teminal!")
print("Here, you can enter any command that the system or custom terminal supports!")
print("Have fun!")

# Custom Commands
def terminal_help():
    print("help - Show THIS help menu")
    print("clear - Clears the screen")
    print("exit - Exits the terminal")
    print("mkfile <file_name> - Makes a file in the current directory")
    print("mkdir <folder_name> - Makes a folder in the current directory")
    print("say <text> - Prints the text to the terminal")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def exit_terminal():
    print("Exiting terminal...")
    exit()
def custom_mkfile(name):
    if not name:  # Ensure a name is provided
        print("Usage: mkfile <file_name>")
        return
    try:
        with open(name, "x") as f:  # 'x' mode ensures file creation fails if it already exists
            print(f"File '{name}' created.")
    except FileExistsError:
        print(f"Error: File '{name}' already exists.")
    except Exception as e:
        print(f"Error creating file: {e}")
def say_text(text=None):
    if not text or text.strip() == "":
        print("Usage: say <text>")
        return
    else:
        print(text)

# Custom Command Dictionary
custom_commands = {
    "help": lambda: terminal_help(),
    "clear": lambda: clear_screen(),
    "exit": lambda: exit_terminal(),
    "mkfile": lambda name: custom_mkfile(name),
    "say": lambda text=None: say_text(text)
}

def execute_command(command):
    parts = command.split(maxsplit=1)
    base_cmd = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    if base_cmd in custom_commands:
        if arg:
            result = custom_commands[base_cmd](arg)
        else:
            result = custom_commands[base_cmd]() 

        if result:
            print(result)
    else:
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            print(result.stdout)
        except subprocess.CalledProcessError:
            print(f"'{command}' is not recognized as an internal or external command, operable program or batch file.")
        except Exception as e:
            print(f"Error: {e}")

while True:
    current_dir = os.getcwd()
    user_input = input(f"{current_dir}>")  
    
    if user_input.lower() in ["exit", "quit"]:
        break  # Only exit when explicitly commanded

    execute_command(user_input)
