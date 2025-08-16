import random
class Weapon:
    def __init__(self, name , weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage_min = max(damage - 1, 1)
        self.damage_max = damage + 1
        self.value = value

    @property
    def damage(self):
        return random.randint(self.damage_min, self.damage_max)

fists = Weapon(name= "fists", 
               weapon_type="melee", 
               damage=2, 
               value=0)