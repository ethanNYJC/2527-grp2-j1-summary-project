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
