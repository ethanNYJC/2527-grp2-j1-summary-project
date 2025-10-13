"""The main game logic."""

import random

import character
import items
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
        self.current_room = None

    def prompt_for_move(self) -> str:
        """Prompt the player to choose a direction to move in."""
        current_room = self.world.current_room
        direction_options = {
            direction: name
            for direction, name in current_room.get_connected_rooms().items()
            if name and not self.world.is_visited(name)
        }
        direction = text.prompt_valid_choice(
            preamble="Available exits:",
            options=direction_options,
            prompt="Where do you want to go: "
        )
        text.clear()
        return direction

    def move_in_direction(self, direction: str) -> None:
        """move in the specified direction"""
        current_room = self.world.current_room
        next_room = self.world.get_room(current_room.get_direction(direction))
        current_room.visit()  
        print(f"You move {direction}.\n")
        self.current_room = next_room

    def equip_item(self, item: items.Weapon):
        self.player.replace_weapon(item)
        print(f'you equipped {item.name}!')

    def consume_item(self, item: items.Consumable):
        self.player.heal(item.health_restore)
        print(f'you used {item.name} and gained {item.health_restore} health.')

    def transact(self, choice: str) -> None:
        """Handles the transaction of buying and using/equipping an item."""
        if not self.player.pay(self.shop.peek_item(choice).value):
            print("you don't have enough crumbs for this item.")
            return
        item = self.shop.pop_item(choice)
        if isinstance(item, items.Weapon):
            self.equip_item(item)
        elif isinstance(item, items.Consumable):
            self.consume_item(item)
    
    def visit_shop(self):
        """Handles the shop visit process."""
        self.shop.refresh()
        choice = None
        while choice != "exit":
            self.shop.display_items()
            choice = text.prompt_valid_choice(
                options=self.shop.get_options() + ["exit"],
                prompt="Choose an item to buy: "
            )
            text.clear()
            if choice != "exit":
                self.transact(choice)

    def single_attack(self,
                      attacker: character.Character,
                      defender: character.Character) -> dict:
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

    def fight(self, enemy: character.Enemy) -> bool:
        count = 0

        while True:
            text.clear()
            self.player.display_stats()
            text.divider()
            enemy.display_stats()
            text.divider()

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
                text.divider()

            
            self.player.health_bar.draw()
            enemy.health_bar.draw()
            text.prompt_continue('\t\t\b"press enter to attack"')
            count += 1

    def fight_room(self, room: room.Room) -> None:
        for i, enemy_name in enumerate(room.enemies, start=1):
            enemy = character.create_enemy(enemy_name)
            self.player.health_bar.update()
            self.fight(enemy)
            if i < len(room.enemies):
                print(f'\n{enemy.name} dropped {enemy.loot} crumbs!')
                self.player.take_crumbs(enemy.loot)
                text.prompt_continue('press enter to fight the next enemy')

    def victory_screen(self):
        print(text.victory_msg)

    def run(self) -> None:
        print(self.world.describe(self.current_room))
        while self.player.is_alive():
            current_room = self.current_room
            print(f'enemies in room: {", ".join(current_room.enemies)}\n')
            text.prompt_continue(
                f'press "Enter" to start your battle in {current_room}'
            )
            self.fight_room(self.world.get_room(current_room))
            direction = self.prompt_for_move()
            self.move_in_direction(direction)
            print(self.world.describe(self.current_room))
            self.visit_shop()
