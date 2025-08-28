import random
class Weapon:
    def __init__(self, name, description, weapon_type, damage, evade_stat, crit_stat, armor_stat, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage_min = max(damage - 1, 1)
        self.damage_max = damage + 1
        self.evade_stat = evade_stat
        self.crit_stat = crit_stat
        self.armor_stat = armor_stat
        self.value = value

    @property
    def damage(self):
        return random.randint(self.damage_min, self.damage_max)

default = Weapon(name= "fists",
                 description="your good old hands",
                 weapon_type="melee",
                 damage=2,
                 evade_stat=0,
                 crit_stat=0,
                 armor_stat=0,
                 value=0)

crayon = Weapon(name="crayon",
                description="a colorful addition to your arsenal",
                weapon_type="melee",
                damage=3,
                evade_stat=0,
                crit_stat=10,
                armor_stat=0,
                value=15)

staple_bullet = Weapon(name="staple bullet",
                       description="careful not to prick your fingers!",
                       weapon_type="ranged",
                       damage=3,
                       evade_stat=10,
                       crit_stat=0,
                       armor_stat=0,
                       value=15)

sandpaper_scrap = Weapon(name="sandpaper scrap",
                         description="maybe you can wrap it around your hands?",
                         weapon_type="melee",
                         damage=4,
                         evade_stat=0,
                         crit_stat=5,
                         armor_stat=1,
                         value=20)

slingshot = Weapon(name="slingshot",
                   description="reliable and sturdy.",
                   weapon_type="ranged",
                   damage=5,
                   evade_stat=5,
                   crit_stat=5,
                   armor_stat=0,
                   value=20)

bubble_wrap = Weapon(name="bubble wrap",
                     description="try not to pop this one, you need it to survive...",
                     weapon_type="special",
                     damage=2,
                     evade_stat=10,
                     crit_stat=-10,
                     armor_stat=2,
                     value=25)

hand_sanitizer = Weapon(name="hand sanitizer",
                        description="kills 99.9 percent of germs, or so it says...",
                        weapon_type="special",
                        damage=4,
                        evade_stat=-10,
                        crit_stat=30,
                        armor_stat=0,
                        value=30)

chicken_bone = Weapon(name="chicken bone",
                      description="rotten and teri-fryingly strong",
                      weapon_type="melee",
                      damage=5,
                      evade_stat=0,
                      crit_stat=30,
                      armor_stat=0,
                      value=40)

ketchup_gun = Weapon(name="ketchup gun",
                     description="ronald mcdonald would approve. ba-da-ba-ba-ba",
                     weapon_type="ranged",
                     damage=3,
                     evade_stat=40,
                     crit_stat=15,
                     armor_stat=0,
                     value=40)

weapon_list = [crayon, staple_bullet, sandpaper_scrap, slingshot, bubble_wrap, hand_sanitizer, chicken_bone, ketchup_gun]