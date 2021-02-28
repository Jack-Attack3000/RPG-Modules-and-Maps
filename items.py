# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Functions for dealing with items


def print_item_list(item_list):
    """Prints list of items and their info"""
    for item_name, item_info in item_list.items():
        print(f"\nInventory Item: {item_name.title()}")
        print(f"\tDescription: {item_info['description']}")
        print(f"\tOwner: {item_info['owner']}")


# Item list
inv_items = {'dented camera': {
              'description': 'a dented video camera,' +
              ' looks like it has been through a lot of use',
              'owner': 'the hacker'
            },
            'pretty cane': {
              'description': 'an ornate pretty cane with a claw ' +
              'holding a glass ball on the top',
              'owner': 'the business man'
            },
            'pretty music box': {
              'description': 'a small white box with ' +
              'a red stripe going up each side and' +
              'small metal crank on the one side',
              'owner': 'the crying spirit'
            }}
