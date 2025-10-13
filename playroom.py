"""The main game logic."""

import random

import character
import room
import shop
import text
import world


def roll_dice(num: int, denom: int) -> bool:
    """Simulates a dice roll where the chance is num / denom.
    Returns True if the roll succeeds, otherwise False.
    """
    roll = random.randint(1, denom)
    return roll <= num


class Game:
    def __init__(self):
        self.player = character.create_player()
        self.shop = shop.Shop(self.player)
        self.world = world.create_world()

    def single_attack(self,
                      attacker: character.Character,
                      defender: character.Character):
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

    def fight(self, enemy: character.Enemy):
        count = 0

        while True:
            text.clear()
            self.player.display_stats()
            print("Xx" + "-"*54 + "xX")

            enemy.display_stats()
            print("Xx" + "-"*54 + "xX")

            if count > 0:
                if self.player.is_alive():
                    result = self.single_attack(self.player, enemy)
                    if result["evade"]:
                        print(f"\t\t{enemy.name} dodged the attack!")
                    else:
                        if result["crit"]:
                            print(f'\t\t{self.player.name} landed a CRITICAL HIT!')
                        print(f'\t\t{self.player.name} did {result["dmg"]} damage to {enemy.name}!')

                        if enemy.total_armor > 0:
                            print(f'\t\t{enemy.total_armor} damage blocked!')
                else:
                    text.clear()
                    print('Game Over! Thanks for playing.')
                    exit(1)
                
                if enemy.is_alive():
                    result = self.single_attack(enemy, self.player)
                    if result["evade"]:
                        print(f"\n\t\t{self.player.name} dodged the attack!")
                    else:
                        if result["crit"]:
                            print(f'\n\t\t{enemy.name} landed a CRITICAL HIT!')
                            print(f'\t\t{enemy.name} did {result["dmg"]} damage to {self.player.name}!')
                        else:
                            print(f'\n\t\t{enemy.name} did {result["dmg"]} damage to {self.player.name}!')

                        if self.player.total_armor > 0:
                            print(f'\t\t{self.player.total_armor} damage blocked!')
                else:
                    text.clear()

                    if enemy.name == "THE FAT RAT.":
                        self.victory_screen()
                        exit(1)

                    self.player.crumbs += enemy.loot
                    enemy.health = enemy.health_max
                    enemy.health_bar.update()
                    print('YOU WIN YIPPEE!')
                    print(f'final health: {self.player.health}/{self.player.health_max}')
                    print(f'no. of crumbs: {self.player.crumbs}')
                    return True
                print("Xx" + "-"*54 + "xX")

            
            self.player.health_bar.draw()
            enemy.health_bar.draw()
            input(f'\t\t\b"press enter to attack"')
            count += 1

    def fight_room(self, room: room.Room):
        for i, enemy in enumerate(room.enemies, start=1):
            self.player.health_bar.update()
            self.fight(enemy)
            if i < len(room.enemies):
                print(f'\n{enemy.name} dropped {enemy.loot} crumbs!')
                input(f'press enter to fight the next enemy')
        self.world.move()

    def victory_screen(self):
        print(text.victory_msg)

    def run(self) -> None:
        while self.player.is_alive():
            print(self.world.describe_current())
            print(f'enemies in room: {[enemy.name for enemy in self.world.current_room.enemies]}\n')
            input(f'press "Enter" to start your battle in {self.world.current_room.get_name()}')
            self.fight_room(self.world.current_room)
            self.shop.open()
