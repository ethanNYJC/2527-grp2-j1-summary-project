import os

intro_list = [
    ['Start Game'],
    ['Rules'],
    ['Quit']
]

# global variables
game_rules = "rules and rules and rules"
starting_desc = "wowzas this game is so fun "
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
    clear()
    
    print(f'Welcome to {info['title']}')
    print(info['desc'])

    while True:
        for i, item in enumerate(info['intro'], start=1):
            print(f'{i}: {item}')
        user_choice = input('Choose: ')

        if user_choice == '1':
            # go into starting room
            clear()
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
