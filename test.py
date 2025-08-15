from character import Player, Enemy
from weapon import fists
import os

hero = Player("ethan", 50, fists, 10, 10, 0)
enemy = Enemy("minhan", 10, fists)

while True:
    os.system("clear")

    
    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    input()

