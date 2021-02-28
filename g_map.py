# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Functions for the map

import locations


def load_map(location_list):
    game_map = [[[] for r in range(3)] for c in range(3)]
    row = 0
    column = 0
    for location in locations.locations_list.items():
        game_map[row][column] = location
        column = column + 1
        if column > 2:
            row = row + 1
            column = 0
    return game_map


def print_map(game_map):
    print("Map of school")
    for row in range(0, 3):
        for column in range(0, 3):
            [name, data] = game_map[row][column]
            print(f"{name}", end="\t\t")
        print("\n")
