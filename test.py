from character import Player, Enemy
from weapon import fists
import os

hero = Player(name="ethan", 
              health=50, 
              weapon=fists, 
              evade_chance=10, 
              crit_chance=10,
              armor=0)

enemy = Enemy(name="minhan", 
              health=20, 
              weapon=fists,
              evade_chance=10
              )

def run():
    count = 0
    while True:
        os.system("clear")
        hero.display_stats()
        print("Xx---------------------------------------------------------xX")
        enemy.display_stats()
        print("Xx---------------------------------------------------------xX")
        if count >= 1:
            hero.attack(enemy)
            enemy.attack(hero)
        print("Xx---------------------------------------------------------xX")
        hero.health_bar.draw()
        enemy.health_bar.draw()
        input(f'\t\t\b"press enter to attack"')
        count += 1
