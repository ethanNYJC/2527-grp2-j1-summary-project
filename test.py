from character import Player, Enemy
from weapon import fists
import os

hero = Player(name="ethan", 
              health=50, 
              weapon=fists, 
              evade_chance=10, 
              crit_chance=10,
              armor=1)

enemy = Enemy(name="minhan", 
              health=10, 
              evade_chance=10, 
              weapon=fists)

def run():
    count = 0
    while True:
        os.system("clear")
        if count >= 1:
            hero.attack(enemy)
            enemy.attack(hero)
        print("Xx--------------------------------------------------------------------xX")
        hero.health_bar.draw()
        enemy.health_bar.draw()

        input()
        count += 1
