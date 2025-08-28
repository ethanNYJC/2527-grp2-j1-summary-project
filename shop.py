from character import Character, Player, player
from weapon import Weapon, weapon_list
import random
import os

class Shop:
    def __init__(self, player):
        self.player = player
        self.weapons = weapon_list
    
    def display_stats(self, weapon: Weapon):
        print(f'  [{weapon.damage_min}-{weapon.damage_max} damage]')
        if weapon.evade_stat != 0:
            print(f'  [{weapon.evade_stat}% evade chance]')
        if weapon.crit_stat != 0:
            print(f'  [{weapon.crit_stat}% crit chance]')
        if weapon.armor_stat != 0:
            print(f'  [+{weapon.armor_stat} armor]')

    def refresh_shop(self):
        global weapon_slot1
        weapon_slot1 = random.choice(weapon_list)

        global weapon_slot2
        weapon_slot2 = random.choice(weapon_list)

    def display_shop(self):
        os.system("clear")
        print("\n=== 🛒 Welcome to the Shop ===")
        print(f'current health: {player.health}')
        print(f"no. of crumbs: {player.crumbs}\n")
        print("\n-- Weapons --")

        
        print(f"1. {weapon_slot1.name} - {weapon_slot1.value} crumbs")
        self.display_stats(weapon_slot1)

        print(f"2. {weapon_slot2.name} - {weapon_slot2.value} crumbs")
        self.display_stats(weapon_slot2)

        print(f"3. fried egg - 3 crumbs")
        print(f'  [+10 health]')
        print("0. Exit Shop")

    def buy_item(self, choice):
        if choice == "1":
            if player.crumbs >= weapon_slot1.value: 
                player.crumbs -= weapon_slot1.value
                player.replace_weapon(weapon_slot1)
            else:
                print("you don't have enough crumbs for this item.")

        elif choice == "2":
            if player.crumbs >= weapon_slot2.value:
                player.crumbs -= weapon_slot2.value
                player.replace_weapon(weapon_slot2)
            print("you don't have enough crumbs for this item.")

        elif choice == "3":
            if player.crumbs >= 3:
                player.crumbs -= 3
                player.health = min(player.health + 10, 100)
                print(f'you used fried egg and gained 10 health.')
            else:
                print("you don't have enough crumbs for this item.")

        else:
            print("Invalid choice.")
            return
        
    def open(self):
        self.refresh_shop()
        while True:
            self.display_shop()
            choice = input("Choose an item to buy (0 to exit): ")
            if choice == "0":
                print("Leaving the shop.")
                break
            self.buy_item(choice)



shop = Shop(player)
