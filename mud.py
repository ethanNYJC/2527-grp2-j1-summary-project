import random


class Character:
    def __init__(self, name, health, weapon) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = weapon

    def alive(self):
        return self.health > 0
    
    def attack(self, target) -> None:
        if not self.alive():
            return 'game over youre ass'
        final_dmg = max(self.weapon.damage - target.armor, 0)
        target.get_damaged(final_dmg)
    
    def get_damaged(self,damage):
        self.health -= damage
        #prevent health from gg below 0
        self.health = max(self.health, 0)

        
class Player(Character):
    def __init__(self, name, health, weapon, evade_chance, crit_chance, armor):
        super().__init__(name, health, weapon)
        self.weapon = 'fists'

    def evade(self) -> bool:
        rolled_evade = random.randint(1,100)
        return rolled_evade <= self.evade_chance
    
    def crit(self, base_dmg) -> float:
        rolled_crit = random.randint(1,100)
        if rolled_crit <= self.crit_chance:
            print('CRITICAL HITTTTT GET FUCKED')
            return base_dmg * 2
        return base_dmg

        