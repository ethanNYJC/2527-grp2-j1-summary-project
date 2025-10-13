import playroom
import text

intro_list = [
    ['Start Game'],
    ['Rules'],
    ['Quit']
]


def play():
    """Main game loop."""
    game = playroom.Game()
    game.run()


def main():
    text.clear()
    print(f'Welcome to {text.game_title}')
    text.linebreak()
    print(text.starting_desc)
    text.linebreak()

    user_choice = text.prompt_valid_choice(
        options=["Start Game", "Rules", "Quit"],
    )
    text.clear()
    if user_choice == 'Start Game':
        play()
    elif user_choice == 'Rules':
        print(text.game_rules)
        text.prompt_continue('Press "Enter" to return to home screen')
        main()
    elif user_choice == 'Quit':
        print('Thanks for playing')
        exit(1)
    else:
        print(text.error_msg)


if __name__ == "__main__":
    main()
