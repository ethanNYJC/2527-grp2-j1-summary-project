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

    def refresh(self):
        self.items["slot1"] = _random_weapon()
        self.items["slot2"] = _random_weapon()

    def display_items(self):
        print("\n=== 🛒 Welcome to the Shop ===")
        print(f'current health: {self.player.health}')
        print(f'current weapon: {self.player.weapon.name}')
        print(f"no. of crumbs: {self.player.crumbs}\n")
        print("\n-- Weapons --")

        if self.items["slot1"] is not None:
            self.display_cost(self.items['slot1'])
            self.display_stats(self.items['slot1'])
        if self.items["slot2"] is not None:
            self.display_cost(self.items['slot2'])
            self.display_stats(self.items['slot2'])
        print(f"3. fried egg - 3 crumbs")
        print(f'  [+10 health]')
        print("0. Exit Shop")

    def get_options(self) -> list[str]:
        return [
            self.items["slot1"].name,
            self.items["slot2"].name,
            "fried egg",
        ]

    def peek_item(self, choice: str) -> items.Item | None:
        """Returns the item corresponding to the choice without removing it from the shop."""
        if choice == self.items["slot1"].name:
            return self.items["slot1"]
        elif choice == self.items["slot2"].name:
            return self.items["slot2"]
        elif choice == "fried egg":
            return items.create_consumable("fried egg")
        else:
            print("Invalid choice.")
            return None

    def pop_item(self, choice: str) -> items.Item:
        """Returns and removes the item corresponding to the choice from the shop."""
        if choice == self.items["slot1"].name:
            item = self.items["slot1"]
            self.items["slot1"] = None
        elif choice == self.items["slot2"].name:
            item = self.items["slot2"]
            self.items["slot2"] = None
        elif choice == "fried egg":
            item = items.create_consumable("fried egg")
        else:
            raise ValueError("Invalid choice.")
        return item
