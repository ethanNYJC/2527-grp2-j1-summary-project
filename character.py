import random
from health_bar import HealthBar
from weapon import fists

class Character:
    def __init__(self, name, health, weapon) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon

    # @property
    def alive(self):
        return self.health > 0
    
    def attack(self, target) -> None:
        if not self.alive():
            return 'game over youre ass'
        dmg = self.weapon.damage
        target.get_damaged(dmg, target)
    
    def get_damaged(self, dmg, target):
        self.health -= dmg
        #prevent health from gg below 0
        self.health = max(self.health, 0)
        self.health_bar.update()
        print(f'{self.name} did {self.weapon.damage} damage to {target.name}')

        
class Player(Character):
    def __init__(self, name, health, weapon, evade_chance, crit_chance, armor):
        super().__init__(name, health, weapon)
        self.evade_chance = evade_chance
        self.crit_chance = crit_chance
        self.armor = armor
        self.health_bar = HealthBar(self, color="green")
        self.weapon = fists

    def evade(self) -> bool:
        rolled_evade = random.randint(1,100)
        return rolled_evade <= self.evade_chance
    
    def crit(self, base_dmg) -> int:
        rolled_crit = random.randint(1,100)
        if rolled_crit <= self.crit_chance:
            print('CRITICAL HIT!')
            return base_dmg * 2
        return base_dmg
    
    def attack(self, target) -> None:
        if not self.alive():
            return 'game over youre ass'
        dmg = self.weapon.damage
        crit_dmg = self.crit(dmg)
        target.get_damaged(crit_dmg, target)
        
    def get_damaged(self, damage, target):
        self.health -= (damage - self.armor)
        #prevent health from gg below 0
        self.health = max(self.health, 0)
        print(f'{self.name} did {self.weapon.damage} damage to {target.name}')

class Enemy(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health, weapon)
        self.health_bar = HealthBar(self, color="red")
        self.weapon = weapon

    def attack(self, target) -> None:
        super().attack(target)
    
    def get_damaged(self, damage, target):
        super().get_damaged(damage, target)
