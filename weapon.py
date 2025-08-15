import random
class Weapon:
    def __init__(self, name , weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage_min = max(damage - 2, 1)
        self.damage_max = damage + 2
        self.value = value

    @property
    def damage(self):
        return self.damage_min
        # return random.randint(self.damage_min, self.damage_max)

fists = Weapon(name= "fists", 
               weapon_type="melee", 
               damage=3, 
               value=0)