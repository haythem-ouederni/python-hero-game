import random
from typing import List

from hero_game.src.shared.models import Coordinates, ObjectCoordinates
from hero_game.src.shared.utils import generate_random_cell_coordinates_on_map
from hero_game.src.weapon.constants import WEAPONS
from hero_game.src.weapon.models import WeaponCharacteristics
from hero_game.src.weapon.weapon import Weapon


def generate_weapons(number_weapons: int = 3) -> List[Weapon]:
    return [generate_weapon(generate_random_cell_coordinates_on_map()) for n in range(number_weapons)]


def generate_weapon(coordinates: Coordinates) -> Weapon:
    weapon_config: WeaponCharacteristics = get_random_weapon_characteristics()
    weapon_position: ObjectCoordinates = _generate_weapon_coordinates(coordinates)
    weapon: Weapon = Weapon(weapon_config, weapon_position)
    return weapon


def _generate_weapon_coordinates(coordinates: Coordinates) -> ObjectCoordinates:
    cell_position: Coordinates = Coordinates(x=coordinates.x, y=coordinates.y)
    position_within_cell: Coordinates = Coordinates(x=15, y=15)
    return ObjectCoordinates(
        cell_position=cell_position,
        position_within_cell=position_within_cell)


def get_random_weapon_characteristics() -> WeaponCharacteristics:
    return random.choice(WEAPONS)


def reinit_weapon(weapon: Weapon) -> None:
    new_coordinates: Coordinates = generate_random_cell_coordinates_on_map()
    new_weapon_config: WeaponCharacteristics = get_random_weapon_characteristics()
    new_weapon_position: ObjectCoordinates = _generate_weapon_coordinates(new_coordinates)
    weapon.regenerate(new_weapon_config, new_weapon_position)
