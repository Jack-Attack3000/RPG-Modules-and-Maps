# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Functions for dealing with commands


def print_commands(command_list):
    """Prints available commands"""
    print("Available commands:")
    for command, command_desc in command_list.items():
        print(f"{command} - {command_desc}")


# List of commands
commands_list = {'up': 'move up',
                 'down': 'move down',
                 'right': 'move right',
                 'left': 'move left',
                 'pick up': 'pick up item',
                 'give': 'give item to nearby character',
                 'talk': 'talk to nearby character',
                 'follow': 'ask nearby character to follow',
                 'inventory': 'checks player inventory',
                 'quit': 'quit the game'
                 }

