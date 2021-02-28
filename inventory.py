# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Functions for dealing with inventory


def print_inv(inv_list):
    if inv_list != []:
        for inv_item in inv_list.items():
            print(f"{inv_item}")
    else:
        print("You don't have anything")


# Inventory list
player_inv = []
