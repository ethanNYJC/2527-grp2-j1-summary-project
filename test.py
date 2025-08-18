from character import Player, Enemy
from weapon import default
import os

player = Player(name="ethan", 
              health=50, 
              weapon=default, 
              evade_chance=10, 
              crit_chance=0,
              armor=0)

ant = Enemy(name="minhan", 
              health=50, 
              evade_chance=10,
              weapon=default
              )

def fight(enemy):
    count = 0
    while True:
        os.system("clear")

        player.display_stats()
        print("Xx" + "-"*54 + "xX")

        enemy.display_stats()
        print("Xx" + "-"*54 + "xX")

        if count > 0:
            enemy.attack(player)
            player.attack(enemy)
            print("Xx" + "-"*54 + "xX")

        player.health_bar.draw()
        enemy.health_bar.draw()
        input(f'\t\t\b"press enter to attack"')
        count += 1
        

        
        
        
