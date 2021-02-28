# Course: CS 30
# Period: 1
# Date Created: 21/02/28
# Date Last Modified: 21/02/28
# Name: Jack Anderson
# Description: Functions for dealing with characters


def print_chara_list(chara_list):
    """Prints list of characters and their info"""
    for characters, chara_info in chara_list.items():
        print(f"\n{characters.title()} is {chara_info['description']}.")
        save = f"{chara_info['how_to_save']}"
        print(f"\t{save.title()} to save them")


# Character list and info
chara = {'celine': {
          'description': 'the sister of damien',
          'how_to_save': 'bring her to damien'
        },
        'damien': {
          'description': 'the brother of celine',
          'how_to_save': 'bring celine to him'
        },
        'the hacker': {
          'description': 'a rude hacker who is good with computers',
          'how_to_save': 'give him the dented camera'
        },
        'the business man': {
          'description': 'a well-dressed business man',
          'how_to_save': 'give him the pretty cane'
        },
        'the crying spirit': {
          'description': 'a spirit with permanent tear streaks and a knack ' +
          'for music',
          'how_to_save': 'give him the pretty music box'
        }}

