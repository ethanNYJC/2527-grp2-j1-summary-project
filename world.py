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

    def is_visited(self, name: str) -> bool:
        return self.rooms[name].entered

    def describe(self, room_name: str) -> str:
        """return description of current room and exits"""
        the_room = self.get_room(room_name)
        lines = [
            the_room.name,
            the_room.description,
            "Exits:",
        ]
        for direction, room in the_room.get_connected_rooms().items():
            if room is not None and not self.get_room(room).entered:
                lines.append(f"{direction} --> {room}")
        return "\n".join(lines)
