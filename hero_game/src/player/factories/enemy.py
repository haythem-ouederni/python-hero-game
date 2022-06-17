from typing import List

from hero_game.src.game.constants import INITIAL_HEALTH_POINTS
from hero_game.src.player.constants import ENEMIES_SPRITE_SHEETS_PATHS
from hero_game.src.player.enemy import Enemy
from hero_game.src.player.models import PlayerConfiguration
from hero_game.src.shared.models import Coordinates, ObjectCoordinates
from hero_game.src.shared.utils import generate_random_cell_coordinates_on_map
from hero_game.src.weapon.facotries import get_random_weapon_characteristics
from hero_game.src.weapon.models import WeaponCharacteristics


def generate_enemies(id_index: int, number_enemies: int = 3) -> List[Enemy]:
    return [generate_enemy(id_index + n, generate_random_cell_coordinates_on_map()) for n in range(number_enemies)]


def generate_enemy(id: int, coordinates: Coordinates) -> Enemy:
    enemy_config: PlayerConfiguration = _build_configuration(id, coordinates)
    enemy: Enemy = Enemy(enemy_config)
    return enemy


def _build_configuration(id: int, coordinates: Coordinates) -> PlayerConfiguration:
    cell_position: Coordinates = Coordinates(x=coordinates.x, y=coordinates.y)
    position_within_cell: Coordinates = Coordinates(x=30, y=5)
    enemy_coordinates: ObjectCoordinates = ObjectCoordinates(
        cell_position=cell_position,
        position_within_cell=position_within_cell)
    return PlayerConfiguration(
        id=id, coordinates=enemy_coordinates,
        sprite_sheet_path=ENEMIES_SPRITE_SHEETS_PATHS.get('enemy1'),
        health_points=INITIAL_HEALTH_POINTS,
        weapon=get_random_weapon_characteristics())


def reinit_enemy(enemy: Enemy) -> None:
    new_cell: Coordinates = generate_random_cell_coordinates_on_map()
    new_weapon: WeaponCharacteristics = get_random_weapon_characteristics()
    enemy.revive(new_cell, new_weapon)
