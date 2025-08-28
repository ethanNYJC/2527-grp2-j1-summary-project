import os
from battle import fight, fight_room
from room import world
from character import Character, Player, Enemy, player, ant, flying_cockroach, dustmite, jumping_spider, ladybug, toy_soldier, fat_rat 
from shop import shop

intro_list = [
    ['Start Game'],
    ['Rules'],
    ['Quit']
]

# global variables
game_rules = """
- Player (Hero) will start with 50 health and base attack, evade chance, crit chance and 0 armor. 
- Each Room will have a random number of enemies spawned (2-3). Each enemy will drop money (crumbs)
- Battle is automated with each turn trading attacks until one wins.

- After every Room, a Shop with 2 randomly generated weapons and a consumable to recover health will
be made available in exchange for crumbs

After the Shop, a choice can be made to go to the next Room depending on which direction you choose.

GOOD LUCK!
"""

starting_desc = """
    In this game, you are a child who didn't clean your room. To teach you a lesson, your parents shrunk you down
to the size of an ant to let you experience how dirty your room was. During your journey to the door, you encounter
many gargantuan beasts that were once tiny compared to you, now posing a real threat. As you continue on your
adventure, level up your gear to defeat stronger and stronger foes, up until the final boss... 
"""

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
            print(world.describe_current())
            print(f'enemies in room: {[enemy.name for enemy in world.current_room.enemies]}\n')
            input(f'press "Enter" to start your battle in {world.current_room.get_name()}')
            fight_room(world.current_room)
            shop.open()
            
    elif user_choice == '2':
        clear()
        print(info['rules'])
        input('Press "Enter" to return to home screen')

        main()
    elif user_choice == '3':
        clear()
        print('Thanks for playing')
        exit(1)
    else:
        clear()
        print(info['error'])


if __name__ == "__main__":
    main()
