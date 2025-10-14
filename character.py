import data
from health_bar import HealthBar
import items

_player_data = data.gamedata["player"]
_enemies_data = data.gamedata["enemies"]


def create_player() -> "Player":
    player = Player(
        name=_player_data["name"],
        health=_player_data["health"],
        weapon=_player_data["starting_weapon"],
        evade_chance=_player_data["evade_chance"],
        crit_chance=_player_data["crit_chance"],
        armor=_player_data["armor"]
    )
    return player

def create_enemy(name: str) -> "Enemy":
    if name not in data.enemy_names:
        raise ValueError(f"Enemy '{name}' not found in enemies_data.")
    enemy_data = data.gamedata["enemies"][name]
    return Enemy(
        name=enemy_data["name"],
        health=enemy_data["health"],
        weapon=enemy_data["weapon"],
        evade_chance=enemy_data["evade_chance"],
        crit_chance=enemy_data["crit_chance"],
        armor=enemy_data["armor"],
        loot=enemy_data["loot"]
    )


class Character:
    def __init__(self,
                 name: str,
                 health: int,
                 weapon: str,
                 evade_chance: int,
                 crit_chance: int,
                 armor: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.evade_chance = evade_chance
        self.crit_chance = crit_chance
        self.armor = armor

        self.weapon = items.create_weapon(weapon)

    def calculate_damage(self) -> int:
        return self.weapon.damage

    def calculate_evade(self) -> int:
        return self.evade_chance + self.weapon.evade_stat

    def calculate_crit(self) -> int:
        return self.crit_chance + self.weapon.crit_stat

    def calculate_armor(self) -> int:
        return self.armor + self.weapon.armor_stat

    def display_stats(self):
        print(f'Name: {self.name}')
        print(f'Damage = {self.calculate_damage()}')
        print(f"Evade Chance = {self.calculate_evade()}%")
        print(f'Crit Chance = {self.calculate_crit()}%')
        if self.calculate_armor() > 0:
            print(f'Armor: {self.calculate_armor()}')

    def is_alive(self):
        return self.health > 0
   
    def take_damage(self, dmg: int):
        """Apply dmg to the character's health.
        Character's health cannot fall below 0.
        """
        self.health -= dmg
        self.health = max(self.health, 0)

        
class Player(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon: str,
                 evade_chance: int,
                 crit_chance: int,
                 armor: int):
        super().__init__(name, health, weapon, evade_chance, crit_chance, armor)
        self.health_bar = HealthBar(self, color="green")
        self.crumbs = 0

    def display_stats(self):
        super().display_stats()
        print(f'Crumbs: {self.crumbs}')

    def pay(self, amount: int) -> bool:
        """Attempt to pay the specified amount of crumbs.
        Returns True if the payment was successful, otherwise False.
        """
        if self.crumbs >= amount:
            self.crumbs -= amount
            return True
        else:
            print("Not enough crumbs!")
            return False

    def take_crumbs(self, amount: int) -> None:
        """Add the specified amount of crumbs to the player's total."""
        self.crumbs += amount

    def take_damage(self, dmg: int) -> None:
        """Apply dmg to the player's health.
        Player's health cannot fall below 0.
        Update the health bar after taking damage.
        """
        super().take_damage(dmg)
        self.health_bar.update()

    def heal(self, amount: int) -> None:
        """Heal the player by the specified amount.
        Player's health cannot exceed health_max.
        """
        self.health += amount
        self.health = min(self.health, self.health_max)
        self.health_bar.update()

    def set_weapon(self, new_weapon):
        self.weapon = new_weapon

    def replace_weapon(self, new_weapon):
        old_weapon = self.weapon
        self.weapon = new_weapon
        self.total_evade = self.evade_chance + self.weapon.evade_stat
        self.total_crit = self.crit_chance + self.weapon.crit_stat
        self.total_armor = self.armor + self.weapon.armor_stat

        print(f'you replaced {old_weapon.name} with {new_weapon.name}!')


class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon: str,
                 evade_chance: int,
                 crit_chance: int,
                 armor: int,
                 loot: int):
        super().__init__(name, health, weapon, evade_chance, crit_chance, armor)
        self.health_bar = HealthBar(self, color="red")
        self.loot = loot

    def take_damage(self, dmg: int) -> None:
        """Apply dmg to the enemy's health.
        Enemy's health cannot fall below 0.
        Update the health bar after taking damage.
        """
        super().take_damage(dmg)
        self.health_bar.update()

    def display_stats(self):
        super().display_stats()
