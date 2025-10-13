import data
from health_bar import HealthBar
from weapon import Weapon, default, crayon, staple_bullet, sandpaper_scrap, slingshot, bubble_wrap, hand_sanitizer, chicken_bone, ketchup_gun, weapon_list
import weapon

_player_data = data.gamedata["player"]
_enemies_data = data.gamedata["enemies"]


def create_player() -> "Player":
    player = Player(
        name=_player_data["name"],
        health=_player_data["health"],
        weapon=globals()[_player_data["weapon"].replace(" ", "_").lower()],
        evade_chance=_player_data["evade_chance"],
        crit_chance=_player_data["crit_chance"],
        armor=_player_data["armor"]
    )
    return player

def create_enemy(name: str) -> "Enemy":
    if name not in data.enemy_names:
        raise ValueError(f"Enemy '{name}' not found in enemies_data.")
    return Enemy(
        name=data["name"],
        health=data["health"],
        weapon=weapon.create_weapon(data["weapon"]),
        evade_chance=data["evade_chance"],
        crit_chance=data["crit_chance"],
        armor=data["armor"],
        loot=data["loot"]
    )


class Character:
    def __init__(self, name, health, weapon, evade_chance, crit_chance, armor) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.evade_chance = evade_chance
        self.crit_chance = crit_chance
        self.armor = armor

        self.weapon = weapon
        self.weapon_evade = weapon.evade_stat
        self.weapon_crit = weapon.crit_stat
        self.weapon_armor = weapon.armor_stat

        self.total_evade = (self.evade_chance + self.weapon.evade_stat)
        self.total_crit = (self.crit_chance + self.weapon.crit_stat)
        self.total_armor = (self.armor + self.weapon.armor_stat)

    def display_stats(self):
        print(f'Name: {self.name}')
        print(f'Damage = {self.weapon.damage_min}-{self.weapon.damage_max}')
        print(f"Evade Chance = {self.total_evade}%")
        print(f'Crit Chance = {self.total_crit}%')
        if self.total_armor > 0:
            print(f'Armor: {self.total_armor}')

    def is_alive(self):
        return self.health > 0
   
    def take_damage(self, dmg: int):
        """Apply dmg to the character's health.
        Character's health cannot fall below 0.
        """
        self.health -= dmg
        self.health = max(self.health, 0)
        self.health_bar.update()

        
class Player(Character):
    def __init__(self, name, health, weapon: Weapon, evade_chance, crit_chance, armor):
        super().__init__(name, health, weapon, evade_chance, crit_chance, armor)
        self.health_bar = HealthBar(self, color="green")
        self.crumbs = 0

    def display_stats(self):
        super().display_stats()
        print(f'Crumbs: {self.crumbs}')
    
    def set_weapon(self, new_weapon):
        self.weapon = new_weapon

    def replace_weapon(self, new_weapon):
        old_weapon = self.weapon
        self.weapon = new_weapon
        self.total_evade = self.evade_chance + self.weapon.evade_stat
        self.total_crit = self.crit_chance + self.weapon.crit_stat
        self.total_armor = self.armor + self.weapon.armor_stat

        print(f'you replaced {old_weapon.name} with {new_weapon.name}!')


class Enemy(Character):
    def __init__(self, name, health, weapon, evade_chance, crit_chance, armor, loot):
        super().__init__(name, health, weapon, evade_chance, crit_chance, armor)
        self.loot = loot
        self.health_bar = HealthBar(self, color="red")

    def display_stats(self):
        super().display_stats()
