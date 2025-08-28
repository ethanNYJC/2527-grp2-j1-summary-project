from character import Character, Player, player
from weapon import weapon_list
import random

class Shop:
    def __init__(self, player):
        self.player = player
        self.weapons = weapon_list
    
    def display_shop(self):
        print("\n=== 🛒 Welcome to the Shop ===")
        print(f"no. of crumbs: {player.crumbs}\n")
        print("\n-- Weapons --")

        global weapon_slot1
        weapon_slot1 = random.choice(weapon_list)
        print(f"1. {weapon_slot1.name} - {weapon_slot1.value} crumbs")

        global weapon_slot2
        weapon_slot2 = random.choice(weapon_list)
        print(f"2. {weapon_slot2.name} - {weapon_slot2.value} crumbs")

        print(f"3. fried egg - 6 crumbs")
        print("0. Exit Shop")

    def buy_item(self, choice):
        if choice == "1":
            if player.crumbs >= weapon_slot1.value: 
                player.replace_weapon(weapon_slot1)
            else:
                print("you don't have enough crumbs for this item.")

        elif choice == "2":
            if player.crumbs >= weapon_slot2.value:
                player.replace_weapon(weapon_slot2)
            print("you don't have enough crumbs for this item.")

        elif choice == "3":
            if player.crumbs >= 6:
                player.health = max(player.health + 10, 50)
                print(f'you used fried egg and gained 10 health.')
            else:
                print("you don't have enough crumbs for this item.")

        else:
            print("Invalid choice.")
            return
        
    def open(self):
        while True:
            self.display_shop()
            choice = input("Choose an item to buy (0 to exit): ")
            if choice == "0":
                print("Leaving the shop.")
                break
            self.buy_item(choice)



shop = Shop(player)
