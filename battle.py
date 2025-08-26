from character import Player, Enemy, roll_dice, player, ant 
from weapon import default
from room import Room, GameMap, world
import os

def player_attack_enemy(player: Player, enemy: Enemy):
    """Apply a single attack from the player to the enemy.
    
    Assume: enemy is alive, player is alive.
    """
    result = {
        "attacker": "player",
        "defender": "enemy"
    }
    result["evade"] = roll_dice(enemy.evade_chance, 100)

    dmg = player.weapon.damage
    result["crit"] = roll_dice(player.crit_chance, 100)

    if result["crit"]:
        dmg *= 2
    result["dmg"] = dmg
    if not result["evade"]:
        enemy.take_damage(dmg)
    return result    


def enemy_attack_player(enemy: Enemy, player: Player):
    """Apply a single attack from the enemy to the player.
    
    Assume: enemy is alive, player is alive.
    """
    result = {
        "attacker": "player",
        "defender": "enemy"
    }
    result["evade"] = roll_dice(player.evade_chance, 100)

    dmg = enemy.weapon.damage - player.armor
    result["dmg"] = dmg
    if not result["evade"]:
        player.take_damage(dmg)
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
                result = player_attack_enemy(player, enemy)
                if result["evade"]:
                    print(f"\t\t{enemy.name} dodged the attack!")
                else:
                    if result["crit"]:
                        print(f'\t\t{player.name} landed a CRITICAL HIT!')
                    print(f'\t\t{player.name} did {result["dmg"]} damage to {enemy.name}!')
            else:
                os.system("clear")
                print('Game Over! youre ass')
                exit(1)
            
            if enemy.is_alive():
                result = enemy_attack_player(enemy, player)
                if result["evade"]:
                    print(f"\t\t{player.name} dodged the attack!")
                else:
                    print(f'\t{enemy.name} did {result["dmg"]} damage to {player.name}! ({player.armor} damage blocked)')
            else:
                os.system("clear")
                enemy.health = enemy.health_max
                print('\t\tYOU WIN YIPPEE!')
                print(f'\t\tfinal health: {player.health}/{player.health_max}')
                return
            print("Xx" + "-"*54 + "xX")

        
        player.health_bar.draw()
        enemy.health_bar.draw()
        input(f'\t\t\b"press enter to attack"')
        count += 1

def fight_room(room: Room):
    for i, enemy in enumerate(room.enemies, start = 1):
        fight(player, enemy)
        if i < len(room.enemies):
            input(f'\t\t\b"press enter to fight the next enemy"')
    print(world.describe_current())
    world.move()




    

    
        

        
        
        
