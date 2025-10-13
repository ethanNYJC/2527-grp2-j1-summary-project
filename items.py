import random

import data

_weapons_data = data.gamedata["weapons"]


def create_consumable(name: str) -> "Consumable":
    if name not in data.consumable_names:
        raise ValueError(f"Consumable '{name}' not found in consumables_data.")
    consumable_data = data.gamedata["consumables"][name]
    return Consumable(
        name=consumable_data["name"],
        description=consumable_data["description"],
        health_restore=consumable_data["health_restore"],
        value=consumable_data["value"]
    )


def create_weapon(name: str) -> "Weapon":
    if name not in data.weapon_names:
        raise ValueError(f"Weapon '{name}' not found in weapons_data.")
    weapon_data = data.gamedata["weapons"][name]
    return Weapon(
        name=weapon_data["name"],
        description=weapon_data["description"],
        weapon_type=weapon_data["weapon_type"],
        damage=weapon_data["damage"],
        evade_stat=weapon_data["evade_stat"],
        crit_stat=weapon_data["crit_stat"],
        armor_stat=weapon_data["armor_stat"],
        value=weapon_data["value"]
    )


class Item:
    """Base class for all items."""

    def __init__(self, name: str, description: str, value: int):
        self.name = name
        self.description = description
        self.value = value

    def get_stats_string(self) -> str:
        raise NotImplementedError("This method should be implemented by subclasses.")


class Consumable(Item):
    def __init__(self,
                 name: str,
                 description: str,
                 health_restore: int,
                 value: int):
        super().__init__(name, description, value)
        self.health_restore = health_restore

    def get_stats_string(self) -> str:
        return f"Restores {self.health_restore} health"


class Weapon(Item):
    def __init__(self,
                 name: str,
                 description: str,
                 weapon_type: str,
                 damage: int,
                 evade_stat: int,
                 crit_stat: int,
                 armor_stat: int,
                 value: int):
        super().__init__(name, description, value)
        self.weapon_type = weapon_type
        self.damage_min = max(damage - 1, 1)
        self.damage_max = damage + 1
        self.evade_stat = evade_stat
        self.crit_stat = crit_stat
        self.armor_stat = armor_stat

    def get_stats_string(self) -> str:
        stats = []
        stats.append(f"Damage: {self.damage_min}-{self.damage_max}")
        if self.evade_stat != 0:
            stats.append(f"Evade Chance: {self.evade_stat}%")
        if self.crit_stat != 0:
            stats.append(f"Crit Chance: {self.crit_stat}%")
        if self.armor_stat != 0:
            stats.append(f"Armor: {self.armor_stat}")
        return "\n".join(stats)

    @property
    def damage(self):
        return random.randint(self.damage_min, self.damage_max)
