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

    def move(self, direction: str):
        """move to connected room"""

        connected = self.current_room.get_connected()
        if connected[direction]:
            self.current_room = connected[direction]
            return f"You move {direction} and enter {self.describe_current()}"
        return "You can't go that way."

    def describe_current(self):
        """return description of current room and exits"""
        exits = []
        for key, value in self.current_room.get_connected().items():
            if value:
                exits.append(key)
                
        return f"{self.current_room.get_name()}: {self.current_room.get_description()}\nExits: {exits}"



room1 = Room('room1', 'This is the first room.', ['enemy1', 'enemy2'])
room2 = Room('room2', 'This is the second room.', ['enemy3', 'enemy4'])
room3 = Room('room3', 'This is the third room.', ['enemy5'])
room4 = Room('room4', 'This is the fourth room.', ['enemy6'])
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
print(world.describe_current())
print(world.move('east'))
print(world.move('north'))
print(world.move('north'))



