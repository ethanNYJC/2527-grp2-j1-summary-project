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
        
    def replace_weapon(self, new_weapon):
        old_weapon = self.weapon
        self.weapon = new_weapon
        print(f'you replaced {old_weapon.name} with {new_weapon.name}!')
        
class Enemy(Character):
    def __init__(self, name, health, weapon, evade_chance, crit_chance, armor, loot):
        super().__init__(name, health, weapon, evade_chance, crit_chance, armor)
        self.loot = loot
        self.health_bar = HealthBar(self, color="red")

    def display_stats(self):
        super().display_stats()
        


player = Player(name="ethan",
              health=100, 
              weapon=default, 
              evade_chance=10, 
              crit_chance=10,
              armor=0)

ant = Enemy(name="ant", 
              health=10, 
              weapon=default,
              evade_chance=0,
              crit_chance=0,
              armor=0,
              loot=5)

flying_cockroach = Enemy(name="flying cockroach",
                         health=10,
                         weapon=staple_bullet,
                         evade_chance=30,
                         crit_chance=5,
                         armor=0,
                         loot=7)

dustmite = Enemy(name="dustmite",
                 health=15,
                 weapon=crayon,
                 evade_chance=0,
                 crit_chance=5,
                 armor=0,
                 loot=8)

jumping_spider = Enemy(name="jumping spider",
                       health=12,
                       weapon=sandpaper_scrap,
                       evade_chance=10,
                       crit_chance=-5,
                       armor=0,
                       loot=10)

centipede = Enemy(name="centipede",
                  health=35,
                  weapon=default,
                  evade_chance=10,
                  crit_chance=10,
                  armor=0,
                  loot=14)

ladybug = Enemy(name="ladybug",
                health=13,
                weapon=hand_sanitizer,
                evade_chance=0,
                crit_chance=10,
                armor=0,
                loot=20)

toy_soldier = Enemy(name="toy soldier",
                    health=20,
                    weapon=bubble_wrap,
                    evade_chance=-10,
                    crit_chance=20,
                    armor=0,
                    loot=22)

fat_rat = Enemy(name="THE FAT RAT.",
                health=60,
                weapon=slingshot,
                evade_chance=-5,
                crit_chance=5,
                armor=1,
                loot=0)

enemy_list = [ant, ant, ant, ant, 
              flying_cockroach, flying_cockroach, flying_cockroach, 
              dustmite, dustmite, dustmite,
              jumping_spider, jumping_spider,
              centipede, centipede,
              ladybug, 
              toy_soldier]