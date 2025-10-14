"""The main game logic."""

import random
from typing import Any

import character
import config
import items
import room
import shop
import text
import world

BOSS_NAME = "THE FAT RAT."


def roll_dice(num: int, denom: int) -> bool:
    """Simulates a dice roll where the chance is num / denom.
    Returns True if the roll succeeds, otherwise False.
    """
    roll = random.randint(1, denom)
    return roll <= num


def roll_damage(damage: int) -> int:
    """Simulates rolling for damage.
    Damage is a random integer between damage - 1 and damage + 1, inclusive.
    Minimum damage is 1.
    """
    return random.randint(max(damage - 1, 1), damage + 1)


class Game:
    def __init__(self):
        self.player = character.create_player()
        self.shop = shop.Shop(self.player)
        self.world = world.create_world()
        self.current_room = self.world.get_room(config.START_ROOM)

    def prompt_for_move(self) -> str:
        """Prompt the player to choose a direction to move in."""
        current_room = self.current_room
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
        current_room = self.current_room
        room_name = current_room.get_direction(direction)
        if not room_name:
            raise ValueError(
                f"Cannot move in direction {direction} from {current_room}"
            )
        next_room = self.world.get_room(room_name)
        self.current_room = next_room
        current_room.visit()
        print(f"You move {direction}.")

    def equip_item(self, item: items.Weapon):
        self.player.replace_weapon(item)
        print(f'you equipped {item.name}!')

    def consume_item(self, item: items.Consumable):
        self.player.heal(item.health_restore)
        print(f'you used {item.name} and gained {item.health_restore} health.')

    def transact(self, choice: str) -> None:
        """Handles the transaction of buying and using/equipping an item."""
        peeked_item = self.shop.peek_item(choice)
        if peeked_item is None:
            print("Sorry, that item is not available.")
            return
        if not self.player.pay(peeked_item.value):
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

    def lose_game(self) -> None:
        text.clear()
        print('Game Over! Thanks for playing.')
        exit(1)

    def win_game(self) -> None:
        print(text.victory_msg)
        exit(1)

    def single_attack(self,
                      attacker: character.Character,
                      defender: character.Character) -> dict:
        """Apply a single attack from the player to the enemy.
        
        Assume: enemy is alive, player is alive.
        """
        result: dict[str, Any] = {
            "attacker": attacker.name,
            "defender": defender.name
        }
        result["evade"] = roll_dice(defender.calculate_evade(), 100)

        result["attacker_damage"] = roll_damage(attacker.calculate_damage())
        result["defender_armor"] = defender.calculate_armor()
        if not result["evade"]:
            result["crit"] = roll_dice(attacker.calculate_crit(), 100)
            if result["attacker_damage"] > result["defender_armor"]:
                result["damage_dealt"] = result["attacker_damage"] - result["defender_armor"]
                if result["crit"]:
                    result["damage_dealt"] *= 2
                defender.take_damage(result["damage_dealt"])
            else:
                result["damage_blocked"] = result["attacker_damage"]
        return result

    def attack_report(self, result: dict) -> None:
        """Prints the result of an attack."""
        if result["evade"]:
            print(f"\t\t{result['defender']} dodged the attack!")
            return
        if "damage_blocked" in result:
            print(f'\t\t{result["damage_blocked"]} damage blocked!')
            return
        if result["crit"]:
            print(f'\t\t{result["attacker"]} landed a CRITICAL HIT!')
        print(f'\t\t{result["attacker"]} did {result["damage_dealt"]} damage to {result["defender"]}!')

    def fight(self, enemy: character.Enemy) -> bool:
        """Handles the fight between the player and a single enemy.

        Fight ends when either the player or the enemy is defeated.
        Returns True if the player wins, otherwise False.
        """
        def show_status() -> None:
            self.player.health_bar.draw()
            enemy.health_bar.draw()
            text.prompt_continue('\t\t\b"press enter to attack"')

        while True:
            text.clear()
            self.player.display_stats()
            text.divider()
            enemy.display_stats()
            text.divider()

            show_status()
            result = self.single_attack(self.player, enemy)
            self.attack_report(result)
            if not self.player.is_alive():
                self.lose_game()
                return False
            
            if enemy.is_alive():
                result = self.single_attack(enemy, self.player)
                self.attack_report(result)
            else:
                if enemy.name == BOSS_NAME:
                    self.win_game()
                self.player.take_crumbs(enemy.loot)
                print('YOU WIN YIPPEE!')
                print(f'final health: {self.player.health}/{self.player.health_max}')
                print(f'no. of crumbs: {self.player.crumbs}')
                return True
            text.divider()

    def fight_room(self, room: room.Room) -> None:
        """Fight all enemies in the room"""
        for i, enemy_name in enumerate(room.enemies, start=1):
            enemy = character.create_enemy(enemy_name)
            self.player.health_bar.update()
            self.fight(enemy)
            if i < len(room.enemies):
                print(f'\n{enemy.name} dropped {enemy.loot} crumbs!')
                self.player.take_crumbs(enemy.loot)
                text.prompt_continue('press enter to fight the next enemy')

    def run(self) -> None:
        print(self.world.describe(self.current_room.name))
        while self.player.is_alive():
            current_room = self.current_room
            print(f'enemies in room: {", ".join(current_room.enemies)}\n')
            text.prompt_continue(
                f'press "Enter" to start your battle in {current_room}'
            )
            self.fight_room(current_room)
            direction = self.prompt_for_move()
            self.move_in_direction(direction)
            print(self.world.describe(self.current_room.name))
            self.visit_shop()
