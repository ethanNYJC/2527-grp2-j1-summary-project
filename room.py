from character import player, ant 
import os

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
        direction = input('Where do you want to go: ')
        connected = self.current_room.get_connected()
        while direction not in connected:
            os.system('clear')
            print(connected)
            print('invalid direction')
            direction = input('Where do you want to go: ')
        os.system('clear')
        self.current_room = connected[direction]
        print(f"You move {direction}.\n{self.describe_current()}")


    def describe_current(self):
        """return description of current room and exits"""
        exits = []
        for key, value in self.current_room.get_connected().items():
            if value:
                exits.append(key)
                
        return f"{self.current_room.get_name()}: {self.current_room.get_description()}\nExits: {exits}"



room1 = Room('room1', 'This is the first room.', [ant, ant])
room2 = Room('room2', 'This is the second room.', [ant])
room3 = Room('room3', 'This is the third room.', [ant, ant, ant])
room4 = Room('room4', 'This is the fourth room.', [ant, ant, ant, ant])
room1.set_connected('east', room2)
room2.set_connected('west', room1)
room2.set_connected('east', room3)
room2.set_connected('north', room4)
room3.set_connected('west', room2)
room4.set_connected('south', room2)

world = GameMap()
world.add_room(room1)
world.add_room(room2)
world.add_room(room3)
world.add_room(room4)




