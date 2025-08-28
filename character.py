import random
import os
from health_bar import HealthBar
from weapon import Weapon, default, crayon, staple_bullet, sandpaper_scrap, slingshot, bubble_wrap, hand_sanitizer, chicken_bone, ketchup_gun, weapon_list

def roll_dice(num, denom) -> bool:
    """Simulates a dice roll where the chance is num / denom.
    Returns True if the roll succeeds, otherwise False.
    """
    roll = random.randint(1, denom)
    return roll <= num

class Character:
    def __init__(self, name, health, weapon: Weapon, evade_chance, crit_chance, armor) -> None:
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
        self.total_evade = evade_chance + weapon.evade_stat
        self.total_crit = crit_chance + weapon.crit_stat
        self.total_armor = armor + weapon.armor_stat

    def display_stats(self):
        print(f'Name: {self.name}')
        print(f'Damage = {self.weapon.damage_min}-{self.weapon.damage_max}')
        print(f"Evade Chance = {self.total_evade}%")

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
        print(f'Crit Chance = {self.total_crit}%')
        print(f'Armor: {self.total_armor}')
        
    def replace_weapon(self, new_weapon):
        old_weapon = self.weapon
        self.crumbs += old_weapon.value
        self.weapon = new_weapon
        
class Enemy(Character):
    def __init__(self, name, health, weapon, evade_chance, crit_chance= 0, armor= 0):
        super().__init__(name, health, weapon, evade_chance, crit_chance, armor)
        self.health_bar = HealthBar(self, color="red")

    def display_stats(self):
        super().display_stats()
        print(f'Crit Chance = {self.total_crit}%')


player = Player(name="ethan",
              health=50, 
              weapon=default, 
              evade_chance=10, 
              crit_chance=10,
              armor=0)

ant = Enemy(name="minhan", 
              health=10, 
              weapon=default,
              evade_chance=0,
              crit_chance=0,
              armor=0
            )
