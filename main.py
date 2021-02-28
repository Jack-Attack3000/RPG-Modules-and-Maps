# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Making a RPG map with modules


# Importing functions
import characters
import commands
import inventory
import items
import locations
import g_map

# Set up game
game_map = g_map.load_map(locations.locations_list)

g_map.print_map(game_map)

# Main game input loop
message = ''
while message != 'quit':
    message = input('Enter a command (type ? for help): ')
    if message == '?':
        commands.print_commands(commands.commands_list)
    elif message == 'up':
        print("You go up")
    elif message == 'down':
        print("You go down")
    elif message == 'right':
        print("You go right")
    elif message == 'left':
        print("You go left")
    elif message == 'pick up':
        print("You pick up item")
    elif message == 'give':
        print("You give item to nearby character")
    elif message == 'talk':
        print("You talk to nearby character")
    elif message == 'follow':
        print("You ask nearby character to follow you")
    elif message == 'inventory':
        inventory.print_inv(inventory.player_inv)
    elif message == 'quit':
        print("Quitting game")
    else:
        print("Invalid Command")
