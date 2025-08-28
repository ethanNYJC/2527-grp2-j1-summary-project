from character import Character, Player, Enemy, player, ant, flying_cockroach, dustmite, jumping_spider, ladybug, toy_soldier, fat_rat, enemy_list
import os
import random

def create_enemies():
    num_enemies = random.randint(2,3)
    enemy_list_copy = enemy_list.copy()
    enemies = []
    for i in range(num_enemies):
        choice = random.choice(enemy_list_copy)
        enemies.append(choice)
        enemy_list_copy.remove(choice)

    return enemies

class Room:
    def __init__(self, name: str, description: str, enemies: list):
        self.name = name
        self.description = description
        self.enemies = enemies
        self.connected_rooms = {'north': None, 'south': None, 'east': None, 'west': None}
        self.entered = False  

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def set_connected(self, direction: str, room):
        self.connected_rooms[direction] = room

    def get_connected(self):
        return self.connected_rooms
    
    def set_entered(self):
        self.entered = True

class GameMap:
    def __init__(self):
        self.rooms = {}      
        self.current_room = None

    def add_room(self, room: Room):
        """adds a room to the map, sets current room if not set"""
        self.rooms[room.get_name()] = room
        if self.current_room is None:
            self.current_room = room
            self.current_room.set_entered()  

    def move(self):
        """move to connected room"""
        connected_rooms = []
        connected = self.current_room.get_connected()
        for key, value in connected.items():
            if value is not None and not value.entered:
                connected_rooms.append(f'{key} --> {value.name}')

        print(f'\navailable exits:{connected_rooms}')

        direction = input(f'\nWhere do you want to go?')

        while direction not in connected:
            os.system('clear')
            print('invalid direction')
            print(f'\navailable exits:{connected_rooms}')
            direction = input(f'\nWhere do you want to go: ')
        os.system('clear')
        self.current_room = connected[direction]
        self.current_room.set_entered()  
        print(f"You move {direction}.\n")
        print(self.describe_current())


    def describe_current(self):
        """return description of current room and exits"""
        exits = []
        connected = self.current_room.get_connected()
        for key, value in connected.items():
            if value is not None and not value.entered:
                exits.append(f'{key} --> {value.name}')
                
        return f"{self.current_room.get_name()}: {self.current_room.get_description()}\nExits: {exits}"
    
room_descriptions = {
    "bed": "Soft, comfy, bouncy, white. NO TIME TO SLEEP, get up and fight!",
    "dollhouse": "You were a dirty, messy person living your best life! Randomly got shrunk down overnight! Now you gotta use items to go out and fight! So much to learn and see!",
    "bookshelf": "Did you even read any of these?", 
    "under_bed": "Its dark and creepy and also wet, enemies or coming! Time to work up a sweat!",
    "rc_car": "Speed, you are speed, you show speed, if you don’t you might die!",
    "dirty_clothes_mountain": "Peeyew! What’s that smell? Vermin coming, i wish you well!",
    "gundam": "Suit up! The evil villians have taken control of the faithful hero suit! Fight them off to save gundam!",
    "lego_castle": "Up in the castle with their new family, Insects saying they’re royalty, How was this disgusting world just waiting for me, I’m so excited to be, BIG",
    "toy_train": "ChoooChooo Chugga Chugga Chugga Chugga ChoooChooo, make sure you dont get runover by the erratic villains of the big thunder mountain railroad!",
    "piggy_bank": "This little piggy went to the market… this little piggy stayed at home… this little piggy had roast beef… this little piggy had none… and  this little piggy is  full of soooooooo many enemies…yayyy!",
    "dustbin": "The bright red dust bin erupts with scraps, Watch your step, dodge those attacks!",
    "pantry": "All enemies here are well fed and slaying them will feel extra rewarding. But beware! To them you look like a tasty treat to satisfy their hunger!"
}

bed = Room('Bed', room_descriptions["bed"], [ant, ant])
dollhouse = Room('Dollhouse', room_descriptions["dollhouse"], create_enemies())
bookshelf = Room('Bookshelf', room_descriptions["bookshelf"], create_enemies())
under_bed = Room('Under the Bed', room_descriptions["under_bed"], create_enemies())
rc_car = Room('RC Car', room_descriptions["rc_car"], create_enemies())
dirty_clothes_mountain = Room('Dirty Clothes Mountain', room_descriptions["dirty_clothes_mountain"], create_enemies())
gundam = Room('Gundam', room_descriptions["gundam"], create_enemies())
lego_castle = Room('Lego Castle', room_descriptions["lego_castle"], create_enemies())
toy_train = Room('Toy Train', room_descriptions["toy_train"], create_enemies())
piggy_bank = Room('Piggy Bank', room_descriptions["piggy_bank"], create_enemies())
dustbin = Room('Dustbin', room_descriptions["dustbin"], create_enemies())
pantry = Room('Pantry', room_descriptions["pantry"], [fat_rat])

room_list = [bed, dollhouse, bookshelf, under_bed, rc_car, dirty_clothes_mountain, gundam, lego_castle, toy_train, piggy_bank, dustbin, pantry]

# bed connected rooms
bed.set_connected('east', under_bed)
bed.set_connected('south', dollhouse)

# dollhouse connected rooms
dollhouse.set_connected('north', bed)
dollhouse.set_connected('east', gundam)
dollhouse.set_connected('south', piggy_bank)

# under_bed connected rooms
under_bed.set_connected('west', bed)
under_bed.set_connected('east', dirty_clothes_mountain)

# dirty_clothes_mountain connected rooms
dirty_clothes_mountain.set_connected('west', under_bed)
dirty_clothes_mountain.set_connected('east', dustbin)

# dustbin connected rooms
dustbin.set_connected('west', dirty_clothes_mountain)
dustbin.set_connected('south', pantry)

# pantry connected rooms
pantry.set_connected('north', dustbin)
pantry.set_connected('west', lego_castle)
pantry.set_connected('south', bookshelf)

# lego_castle connected rooms
lego_castle.set_connected('east', pantry)
lego_castle.set_connected('west', gundam)

# gundam connected rooms
gundam.set_connected('east', lego_castle)
gundam.set_connected('west', dollhouse)

# piggy_bank connected rooms
piggy_bank.set_connected('north', dollhouse)
piggy_bank.set_connected('east', rc_car)

# rc_car connected rooms
rc_car.set_connected('west', piggy_bank)
rc_car.set_connected('east', bookshelf)

# bookshelf connected rooms
bookshelf.set_connected('west', rc_car)
bookshelf.set_connected('north', pantry)


world = GameMap()
for room in room_list:
    world.add_room(room)

print(world.describe_current())


