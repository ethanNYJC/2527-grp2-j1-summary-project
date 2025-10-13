"""Game text and functions for handling text."""

import os


game_title = "Playroom"

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

victory_msg = """
==========================================================
               🏆 CONGRATULATIONS, HERO! 🏆
==========================================================
__     ______  _    _        __          _______ _   _ 
\ \   / / __ \| |  | |       \ \        / /_   _| \ | |
 \ \_/ / |  | | |  | |        \ \  /\  / /  | | |  \| |
  \   /| |  | | |  | |         \ \/  \/ /   | | | . ` |
  | | | |__| | |__| |          \  /\  /   _| |_| |\  |
  |_|  \____/ \____/            \/  \/   |_____|_| \_|


  Mummy and Daddy turned you back to your normal size!
  Hopefully you clean your room next time...
==========================================================

                🎉 Thanks for playing! 🎉
==========================================================
"""

error_msg = "Sorry, I dont understand the command"


# clear terminal
def clear():
    os.system('clear')

def linebreak():
    print()
