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

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def set_connected(self, direction: str, room):
        self.connected_rooms[direction] = room

    def get_connected(self):
        return self.connected_rooms

class GameMap:
    def __init__(self):
        self.rooms = {}      
        self.current_room = None

    def add_room(self, room: Room):
        """adds a room to the map, sets current room if not set"""
        self.rooms[room.get_name()] = room
        if self.current_room is None:
            self.current_room = room  

    def move(self):
        """move to connected room"""
        connected_rooms = []
        connected = self.current_room.get_connected()
        for key, value in connected.items():
            if value is not None:
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
        print(f"You move {direction}.\n")
        print(self.describe_current())


    def describe_current(self):
        """return description of current room and exits"""
        exits = []
        connected = self.current_room.get_connected()
        for key, value in connected.items():
            if value is not None:
                exits.append(f'{key} --> {value.name}')
                
        return f"{self.current_room.get_name()}: {self.current_room.get_description()}\nExits: {exits}"


room1 = Room('room1', 'This is the first room.', [ladybug, toy_soldier])
room2 = Room('room2', 'This is the second room.', create_enemies())
room3 = Room('room3', 'This is the third room.', create_enemies())
room4 = Room('room4', 'This is the fourth room.', create_enemies())
room1.set_connected('east', room2)
room2.set_connected('west', room1)
room2.set_connected('east', room3)
room2.set_connected('north', room4)
room3.set_connected('west', room2)
room4.set_connected('south', room2)

room_list = [room1, room2, room3, room4]

world = GameMap()
for room in room_list:
    world.add_room(room)
