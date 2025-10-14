"""The World class"""

import data
import room


def create_world() -> "World":
    rooms = [
        room.create_room(name)
        for name in data.room_names
    ]
    world = World(rooms)
    return world


class World:
    def __init__(self, rooms: list[room.Room] | None = None):
        self.rooms: dict[str, room.Room] = {}
        if rooms:
            for room_ in rooms:
                self.add_room(room_)

    def add_room(self, room_: room.Room):
        """adds a room to the map, sets current room if not set"""
        self.rooms[room_.get_name()] = room_

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
