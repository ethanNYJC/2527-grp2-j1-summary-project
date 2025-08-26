import os
from battle import fight, fight_room
from room import room1, world
from character import player, ant 

intro_list = [
    ['Start Game'],
    ['Rules'],
    ['Quit']
]

# global variables
game_rules = "rules and rules and rules"

starting_desc = "In this game, you are a child who didn't clean your room. \n" \
"To teach you a lesson, your parents shrunk you down to the\n" \
"size of an ant to let you experience how dirty your room was.\n" \
"During your journey to the door, you encounter many gargantuan\n" \
"beasts that were once tiny compared to you, now posing a real\n" \
"threat. As you continue on your adventure, level up your gear\n" \
"to defeat stronger and stronger foes, up until the final boss... "

error_msg = "Sorry, I dont understand the command"

info = {
    'title': "Playroom",
    'intro': intro_list,
    "desc": starting_desc, 
    "rules": game_rules,
    "error": error_msg
}

# clear terminal
@staticmethod
def clear():
    os.system('clear')

def main():
    """main game loop"""
    clear()
    
    print(f'Welcome to {info['title']}\n')
    print(f'{info['desc']}\n')

    for i, item in enumerate(info['intro'], start=1):
        print(f'{i}: {item}')
    user_choice = input('Choose: ')

    if user_choice == '1':
        while player.is_alive():
            clear()
            input(f'press enter to start your battle in {world.current_room.get_name()}\nenemies in room: {[enemy.name for enemy in world.current_room.enemies]}')
            fight_room(world.current_room)
    elif user_choice == '2':
        clear()
        print(info['rules'])
    elif user_choice == '3':
        clear()
        print('Thanks for playing')
        exit(1)
    else:
        clear()
        print(info['error'])


if __name__ == "__main__":
    main()
