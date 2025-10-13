import random

import data

_weapons_data = data.gamedata["weapons"]


def create_weapon(name: str) -> "Weapon":
    if name not in data.weapon_names:
        raise ValueError(f"Weapon '{name}' not found in weapons_data.")
    return Weapon(
        name=data["name"],
        description=data["description"],
        weapon_type=data["weapon_type"],
        damage=data["damage"],
        evade_stat=data["evade_stat"],
        crit_stat=data["crit_stat"],
        armor_stat=data["armor_stat"],
        value=data["value"]
    )


class Weapon:
    def __init__(self, name, description, weapon_type, damage, evade_stat, crit_stat, armor_stat, value):
        self.name = name
        self.description = description
        self.weapon_type = weapon_type
        self.damage_min = max(damage - 1, 1)
        self.damage_max = damage + 1
        self.evade_stat = evade_stat
        self.crit_stat = crit_stat
        self.armor_stat = armor_stat
        self.value = value

    @property
    def damage(self):
        return random.randint(self.damage_min, self.damage_max)
