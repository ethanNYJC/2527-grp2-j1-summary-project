"""Functions for working with game data."""

import json

import config


def load_json(file_path) -> dict:
    """Load JSON data from a file."""
    with open(file_path, "r") as f:
        return json.load(f)

def load_gamedata() -> dict:
    """Load game data from gamedata.json."""
    return load_json(config.DATA_FILEPATH)


gamedata = load_gamedata()
room_names = list(gamedata["rooms"])
consumable_names = [consumable["name"] for consumable in gamedata["items"]["consumables"]]
weapon_names = [weapon["name"] for weapon in gamedata["items"]["weapons"]]
enemy_names = [enemy["name"] for enemy in gamedata["enemies"]]
