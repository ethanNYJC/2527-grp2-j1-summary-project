from battle import fight, fight_room
from room import world
from character import Character, Player, Enemy, player, ant, flying_cockroach, dustmite, jumping_spider, ladybug, toy_soldier, fat_rat 
from shop import shop
import text

intro_list = [
    ['Start Game'],
    ['Rules'],
    ['Quit']
]


def main():
    """main game loop"""
    text.clear()
    print(f'Welcome to {text.game_title}')
    text.linebreak()
    print(text.starting_desc)
    text.linebreak()

    for i, item in enumerate(intro_list, start=1):
        print(f'{i}: {item}')
    user_choice = input('Choose: ')

    if user_choice == '1':
        while player.is_alive():
            text.clear()
            print(world.describe_current())
            print(f'enemies in room: {[enemy.name for enemy in world.current_room.enemies]}\n')
            input(f'press "Enter" to start your battle in {world.current_room.get_name()}')
            fight_room(world.current_room)
            shop.open()

    elif user_choice == '2':
        text.clear()
        print(text.game_rules)
        input('Press "Enter" to return to home screen')

        main()
    elif user_choice == '3':
        text.clear()
        print('Thanks for playing')
        exit(1)
    else:
        text.clear()
        print(text.error_msg)


if __name__ == "__main__":
    main()
