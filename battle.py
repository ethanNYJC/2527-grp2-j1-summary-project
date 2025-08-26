from character import Player, Enemy, roll_dice, player, ant 
from weapon import default
import os

def single_attack(attacker: Character, defender: Character):
    """Apply a single attack from the player to the enemy.
    
    Assume: enemy is alive, player is alive.
    """
    result = {
        "attacker": "player",
        "defender": "enemy"
    }
    result["evade"] = roll_dice(defender.evade_chance, 100)

    dmg = attacker.weapon.damage - defender.armor
    result["crit"] = roll_dice(attacker.crit_chance, 100)

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
                print('Game Over!')
                return False
            
            if enemy.is_alive():
                result = single_attack(enemy, player)
                if result["evade"]:
                    print(f"\t\t{player.name} dodged the attack!")
                else:
                    print(f'\t{enemy.name} did {result["dmg"]} damage to {player.name}! ({player.armor} damage blocked)')
            else:
                os.system("clear")
                print('\t\tYOU WIN YIPPEE!')
                print(f'\t\tfinal health: {player.health}/{player.health_max}')
                return True
            print("Xx" + "-"*54 + "xX")

        
        player.health_bar.draw()
        enemy.health_bar.draw()
        input(f'\t\t\b"press enter to attack"')
        count += 1
        

        
        
        
