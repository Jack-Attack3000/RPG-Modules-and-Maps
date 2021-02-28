# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Functions for dealing wiht locations


def print_loc_list(loc_list):
    """Prints list of locations and their info"""
    for loc_name, loc_info in loc_list.items():
        print(f"\nThe {loc_name.title()} is {loc_info['description']}.")


# Location list
locations_list = {'library': {
              'description': 'all the bookshelves had been push to the walls' +
              ' to make room for a small pentagram in the middle',
              'item_inside': 'no item',
              'character_inside': 'celine'
            },
            'science lab': {
              'description': 'an old lab with rotting tables and ' +
              'shelves full of broken empty bottles',
              'item_inside': 'dented camera',
              'character_inside': 'no character'
            },
            'music room': {
              'description': 'a room with a couple of chairs and ' +
              'filled with multiple different kinds of instruments',
              'item_inside': 'no item',
              'character_inside': 'the crying spirit'
            },
            'cafeteria': {
              'description': 'a broken-down cafeteria with ' +
              'rotting tables and chairs',
              'item_inside': 'pretty cane',
              'character_inside': 'no character'
            },
            'security office': {
              'description': 'a dark office with a desk, ' +
              '9 computer monitors sat on the desk in a ' +
              '3x3 stack showing static',
              'item_inside': 'no item',
              'character_inside': 'the hacker'
            },
            'office': {
              'description': 'an office with a nice desk and ' +
              'a couple of bookshelves and filing cabinets',
              'item_inside': 'no item',
              'character_inside': 'the ' +
              'business man'
            },
            'empty room': {
              'description': 'an empty room with nothing in it ' +
              'but dust and two doors',
              'item_inside': 'no item',
              'character_inside': 'player'
            },
            'gym': {
              'description': 'a large gym with ' +
              'multiple dust-covered bleachers',
              'item_inside': 'pretty music box',
              'character_inside': 'no character'
            },
            'classroom': {
              'description': 'a room with one large desk and ' +
              'multiple smaller desks facing a chalk board and ' +
              'covered in dust',
              'item_inside': 'no item',
              'character_inside': 'damien'
            }}
