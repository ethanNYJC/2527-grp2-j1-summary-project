import random
import os
from health_bar import HealthBar
from weapon import default

def roll_dice(num, denom) -> bool:
    """Simulates a dice roll where the chance is num / denom.
    Returns True if the roll succeeds, otherwise False.
    """
    roll = random.randint(1, denom)
    return roll <= num

class Character:
    def __init__(self, name, health, weapon, evade_chance) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.evade_chance = evade_chance
        self.weapon = weapon

    def display_stats(self):
        print(f'Name: {self.name}')
        print(f'Damage = {self.weapon.damage_min}-{self.weapon.damage_max}')
        print(f"Evade Chance = {self.evade_chance}%")

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
    def __init__(self, name, health, weapon, evade_chance, crit_chance, armor):
        super().__init__(name, health, evade_chance, weapon)
        self.has_item = False
        self.evade_chance = evade_chance
        self.crit_chance = crit_chance
        self.armor = armor
        self.health_bar = HealthBar(self, color="green")
        self.weapon = default

    def display_stats(self):
        super().display_stats()
        print(f'Crit Chance = {self.crit_chance}%')
        print(f'Armor: {self.armor}')
        
        
class Enemy(Character):
    def __init__(self, name, health, weapon, evade_chance):
        super().__init__(name, health, weapon, evade_chance)
        self.health_bar = HealthBar(self, color="red")
        self.weapon = weapon

    def display_stats(self):
        super().display_stats()



player = Player(name="ethan", 
              health=20, 
              weapon=default, 
              evade_chance=10, 
              crit_chance=100,
              armor=0)

ant = Enemy(name="minhan", 
              health=20, 
              evade_chance=10,
              weapon=default
              )
