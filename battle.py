from character import roll_dice, Character, Player, Enemy, player, ant, flying_cockroach, dustmite, jumping_spider, ladybug, toy_soldier, fat_rat 
from weapon import  Weapon, default, crayon, staple_bullet, sandpaper_scrap, slingshot, bubble_wrap, hand_sanitizer, chicken_bone, ketchup_gun, weapon_list
from room import Room, GameMap, world
import os

def single_attack(attacker: Character, defender: Character):
    """Apply a single attack from the player to the enemy.
    
    Assume: enemy is alive, player is alive.
    """
    result = {
        "attacker": "player",
        "defender": "enemy"
    }
    result["evade"] = roll_dice(defender.total_evade, 100)

    dmg = max(attacker.weapon.damage - defender.total_armor, 0)
    result["crit"] = roll_dice(attacker.total_crit, 100)

    if result["crit"]:
        dmg *= 2
    result["dmg"] = dmg
    if not result["evade"]:
        defender.take_damage(dmg)
    return result    


def fight(player, enemy):
    count = 0

    while True:
        os.system("clear")

        player.display_stats()
        print("Xx" + "-"*54 + "xX")

        enemy.display_stats()
        print("Xx" + "-"*54 + "xX")

        if count > 0:
            if player.is_alive():
                result = single_attack(player, enemy)
                if result["evade"]:
                    print(f"\t\t{enemy.name} dodged the attack!")
                else:
                    if result["crit"]:
                        print(f'\t\t{player.name} landed a CRITICAL HIT!')
                    print(f'\t\t{player.name} did {result["dmg"]} damage to {enemy.name}!')

                    if enemy.total_armor > 0:
                        print(f'\t\t{enemy.total_armor} damage blocked!')
            else:
                os.system("clear")
                print('Game Over! Thanks for playing.')
                exit(1)
            
            if enemy.is_alive():
                result = single_attack(enemy, player)
                if result["evade"]:
                    print(f"\n\t\t{player.name} dodged the attack!")
                else:
                    if result["crit"]:
                        print(f'\n\t\t{enemy.name} landed a CRITICAL HIT!')
                        print(f'\t\t{enemy.name} did {result["dmg"]} damage to {player.name}!')
                    else:
                        print(f'\n\t\t{enemy.name} did {result["dmg"]} damage to {player.name}!')

                    if player.total_armor > 0:
                        print(f'\t\t{player.total_armor} damage blocked!')
            else:
                os.system("clear")

                if enemy.name == "THE FAT RAT.":
                    victory_screen()
                    exit(1)

                player.crumbs += enemy.loot
                enemy.health = enemy.health_max
                enemy.health_bar.update()
                print('YOU WIN YIPPEE!')
                print(f'final health: {player.health}/{player.health_max}')
                print(f'no. of crumbs: {player.crumbs}')
                return True
            print("Xx" + "-"*54 + "xX")

        
        player.health_bar.draw()
        enemy.health_bar.draw()
        input(f'\t\t\b"press enter to attack"')
        count += 1

def fight_room(room: Room):
    for i, enemy in enumerate(room.enemies, start = 1):
        fight(player, enemy)
        if i < len(room.enemies):
            print(f'\n{enemy.name} dropped {enemy.loot} crumbs!')
            input(f'press enter to fight the next enemy')
    world.move()

def victory_screen():
    print("\n" + "=" * 60)
    print(" " * 15 + "🏆 CONGRATULATIONS, HERO! 🏆")
    print("=" * 60)
    print(r"""
__     ______  _    _        __          _______ _   _ 
\ \   / / __ \| |  | |       \ \        / /_   _| \ | |
 \ \_/ / |  | | |  | |        \ \  /\  / /  | | |  \| |
  \   /| |  | | |  | |         \ \/  \/ /   | | | . ` |
   | | | |__| | |__| |          \  /\  /   _| |_| |\  |
   |_|  \____/ \____/            \/  \/   |_____|_| \_|

    """)
    print("\nMummy and Daddy turned you back to your normal size!")
    print("Hopefully you clean your room next time...")
    print("\n" + "-" * 60)
    print("🎉 Thanks for playing! 🎉")
    print("=" * 60 + "\n")







    

    
        

        
        
        
