import data

# Load room data from gamedata.json
_rooms_data = data.gamedata["rooms"]


def create_room(name: str) -> "Room":
    if name not in _rooms_data:
        raise ValueError(f"Room '{name}' not found in rooms_data.")
    return Room(
        name=name,
        description=_rooms_data[name]["description"],
        enemies=_rooms_data[name]["enemies"]
    )


class Room:
    def __init__(self,
                 name: str,
                 description: str,
                 enemies: list[str],
                 connected_rooms: dict[str, str] | None = None):
        self.name = name
        self.description = description
        self.enemies = enemies
        self.connected_rooms: dict[str, str | None] = {
            'north': None,
            'south': None,
            'east': None,
            'west': None
        }
        if connected_rooms:
            for direction in self.connected_rooms:
                self.connected_rooms[direction] = connected_rooms.get(direction)
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
