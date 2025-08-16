import random
import os
from health_bar import HealthBar
from weapon import fists

class Character:
    def __init__(self, name, health, evade_chance, weapon) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.evade_chance = evade_chance
        self.weapon = weapon

    def display_stats(self):
        print(f'Name: {self.name}')
        print(f'Damage = {(self.weapon.damage_max + self.weapon.damage_min) / 2}')
        print(f"Evade Chance = {self.evade_chance}%")

    @property
    def alive(self):
        return self.health > 0
    
    def attack(self, target) -> None:
        dmg = self.weapon.damage
        target.get_damaged(dmg, self)

    def evade(self) -> bool:
        rolled_evade = random.randint(1,100)
        return rolled_evade <= self.evade_chance
    
    def get_damaged(self, dmg, attacker):
        if not self.alive:
            os.system("clear")
            print('\t\tYOU WIN YIPPEE!')
            print(f'\t\tfinal health: {attacker.health}/{attacker.health_max}')
            exit(1)

        if self.evade():
            print(f"\t\t{self.name} dodged the attack!")
            return
        
        self.health -= dmg
        #prevent health from gg below 0
        self.health = max(self.health, 0)
        self.health_bar.update()
        print(f'\t\t{attacker.name} did {dmg} damage to {self.name}!')

        
class Player(Character):
    def __init__(self, name, health, weapon, evade_chance, crit_chance, armor):
        super().__init__(name, health, evade_chance, weapon)
        self.evade_chance = evade_chance
        self.crit_chance = crit_chance
        self.armor = armor
        self.health_bar = HealthBar(self, color="green")
        self.weapon = fists

    def display_stats(self):
        super().display_stats()
        print(f'Crit Chance = {self.crit_chance}%')
        print(f'Armor: {self.armor}')

    def crit(self, base_dmg) -> int:
        rolled_crit = random.randint(1,100)
        if rolled_crit <= self.crit_chance:
            print(f'\t\t{self.name} landed a CRITICAL HIT!')
            return base_dmg * 2
        return base_dmg
    
    def attack(self, target) -> None:
        dmg = self.weapon.damage
        crit_dmg = self.crit(dmg)
        target.get_damaged(crit_dmg, self)
        
    def get_damaged(self, damage, attacker):
        if not self.alive:
            os.system("clear")
            print('Game Over! youre ass')
            exit(1)

        if self.evade():
            print(f"\t\t{self.name} dodged the attack!")
            return
        
        self.health -= (damage - self.armor)
        #prevent health from gg below 0
        self.health = max(self.health, 0)
        self.health_bar.update()
        print(f'\t\b{attacker.name} did {damage - self.armor} damage to {self.name}! ({self.armor} damage blocked)')
        
        

class Enemy(Character):
    def __init__(self, name, health, evade_chance, weapon):
        super().__init__(name, health, evade_chance, weapon)
        self.health_bar = HealthBar(self, color="red")
        self.weapon = weapon

    def evade(self) -> bool:
        rolled_evade = random.randint(1,100)
        return rolled_evade <= self.evade_chance
    
    def attack(self, target) -> None:
        super().attack(target)
    
    def get_damaged(self, damage, attacker):
        super().get_damaged(damage, attacker)
