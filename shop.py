import random

import character
import data
import text
import items


def _random_weapon() -> items.Weapon:
    weapon_name = random.choice(data.weapon_names)
    return items.create_weapon(weapon_name)


class Shop:
    def __init__(self, player: character.Player):
        self.player = player
        self.items: dict[str, items.Item] = {
            "slot1": _random_weapon(),
            "slot2": _random_weapon(),
            "slot3": items.create_consumable("fried egg")
        }

    def display_cost(self, item: items.Item) -> None:
        print(f"1. {item.name} - {item.value} crumbs")

    def display_stats(self, item: items.Item) -> None:
        print(item.get_stats_string())

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

    def buy_item(self, choice: str) -> None:
        if choice == self.items["slot1"].name:
            item = self.items["slot1"]
        elif choice == self.items["slot2"].name:
            item = self.items["slot2"]
        elif choice == "fried egg":
            item = items.create_consumable("fried egg")
        else:
            print("Invalid choice.")
            return

        if not self.player.pay(item.value):
            print("you don't have enough crumbs for this item.")
            return
        if isinstance(item, items.Weapon):
            self.player.replace_weapon(item)
        elif isinstance(item, items.Consumable):
            self.player.heal(item.health_restore)
            print(
                f"you used {item.name} and gained {item.health_restore} health."
            )
        
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
