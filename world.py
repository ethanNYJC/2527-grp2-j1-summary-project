"""The World class"""

import data
import room
import text


def create_world() -> "World":
    world = World()
    for name in data.room_names:
        world.add_room(room.create_room(name))
    return world


class World:
    def __init__(self):
        self.rooms: dict[str, room.Room] = {}
        self.current_room = None

    def add_room(self, room: room.Room):
        """adds a room to the map, sets current room if not set"""
        self.rooms[room.get_name()] = room
        if self.current_room is None:
            self.current_room = room
            self.current_room.set_entered()

    def get_room(self, name: str) -> room.Room:
        return self.rooms[name]

    def move(self):
        """move to connected room"""
        connected_rooms = []
        connected = self.current_room.get_connected()
        for key, value in connected.items():
            if value is not None and not value.entered:
                connected_rooms.append(f'{key} --> {value.name}')

        print(f'\navailable exits:{connected_rooms}')

        direction = text.prompt_valid_choice(
            options=f"available exits:{connected_rooms}",
            prompt="Where do you want to go: "
        )
        text.clear()
        self.current_room = self.get_room(connected[direction])
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
