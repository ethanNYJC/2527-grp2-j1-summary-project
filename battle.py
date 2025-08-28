from character import Character, roll_dice, player, ant 
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
            else:
                os.system("clear")
                print('Game Over! Thanks for playing.')
                exit(1)
            
            if enemy.is_alive():
                result = single_attack(enemy, player)
                if result["evade"]:
                    print(f"\t\t{player.name} dodged the attack!")
                else:
                    print(f'\t\t{enemy.name} did {result["dmg"]} damage to {player.name}!')
                    if player.total_armor > 0:
                        print(f'\t\t{player.total_armor} damage blocked!')
            else:
                os.system("clear")
                enemy.health = enemy.health_max
                enemy.health_bar.update()
                print('YOU WIN YIPPEE!')
                print(f'final health: {player.health}/{player.health_max}')
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
            input(f'\npress enter to fight the next enemy')
    world.move()




    

    
        

        
        
        
