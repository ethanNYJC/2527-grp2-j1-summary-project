import os
import random

import data
import text
import weapon


def _random_weapon() -> weapon.Weapon:
    weapon_name = random.choice(data.weapon_names)
    return weapon.create_weapon(weapon_name)


class Shop:
    def __init__(self, player):
        self.player = player
        self.items = {
            "slot1": _random_weapon(),
            "slot2": _random_weapon()
        }

    def display_cost(self, item: weapon.Weapon) -> None:
        print(f"1. {item.name} - {item.value} crumbs")
    
    def display_stats(self, weapon: weapon.Weapon) -> None:
        print(f'  [{weapon.damage_min}-{weapon.damage_max} damage]')
        if weapon.evade_stat != 0:
            print(f'  [{weapon.evade_stat}% evade chance]')
        if weapon.crit_stat != 0:
            print(f'  [{weapon.crit_stat}% crit chance]')
        if weapon.armor_stat != 0:
            print(f'  [+{weapon.armor_stat} armor]')

    def refresh_shop(self):
        self.items["slot1"] = _random_weapon()
        self.items["slot2"] = _random_weapon()

    def display_shop(self):
        print("\n=== 🛒 Welcome to the Shop ===")
        print(f'current health: {self.player.health}')
        print(f'current weapon: {self.player.weapon.name}')
        print(f"no. of crumbs: {self.player.crumbs}\n")
        print("\n-- Weapons --")

        self.display_cost(self.items['slot1'])
        self.display_stats(self.items['slot1'])
        self.display_cost(self.items['slot2'])
        self.display_stats(self.items['slot2'])
        print(f"3. fried egg - 3 crumbs")
        print(f'  [+10 health]')
        print("0. Exit Shop")

    def buy_item(self, choice: str):
        if choice == self.items["slot1"].name:
            if self.player.crumbs >= self.items["slot1"].value:
                self.player.crumbs -= self.items["slot1"].value
                self.player.replace_weapon(self.items["slot1"])
            else:
                print("you don't have enough crumbs for this item.")

        elif choice == self.items["slot2"].name:
            if self.player.crumbs >= self.items["slot2"].value:
                self.player.crumbs -= self.items["slot2"].value
                self.player.replace_weapon(self.items["slot2"])
            else:
                print("you don't have enough crumbs for this item.")

        elif choice == "fried egg":
            if self.player.crumbs >= 3:
                self.player.crumbs -= 3
                self.player.health = min(self.player.health + 10, 100)
                print(f'you used fried egg and gained 10 health.')
            else:
                print("you don't have enough crumbs for this item.")

        else:
            print("Invalid choice.")
            return
        
    def open(self):
        self.refresh_shop()
        choice = None
        while choice != "exit":
            self.display_shop()
            text.prompt_valid_choice(
                options=[
                    self.items["slot1"].name,
                    self.items["slot2"].name,
                    "fried egg",
                    "exit"
                ],
                prompt="Choose an item to buy: "
            )
            text.clear()
            self.buy_item(choice)
