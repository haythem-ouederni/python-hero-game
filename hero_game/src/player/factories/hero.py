from hero_game.src.game.constants import INITIAL_HEALTH_POINTS
from hero_game.src.player.constants import HEROES_SPRITE_SHEETS_PATHS, ENEMIES_SPRITE_SHEETS_PATHS
from hero_game.src.player.hero import Hero
from hero_game.src.player.models import PlayerConfiguration
from hero_game.src.shared.models import Coordinates, ObjectCoordinates
from hero_game.src.shared.utils import generate_random_cell_coordinates_on_map


def generate_hero(id: int):
    hero_config: PlayerConfiguration = _build_configuration(id, generate_random_cell_coordinates_on_map())
    hero: Hero = Hero(hero_config)
    return hero


def _build_configuration(id: int, coordinates: Coordinates) -> PlayerConfiguration:
    cell_position: Coordinates = Coordinates(x=coordinates.x, y=coordinates.y)
    position_within_cell: Coordinates = Coordinates(x=10, y=30)
    hero_coordinates: ObjectCoordinates = ObjectCoordinates(
        cell_position=cell_position,
        position_within_cell=position_within_cell)
    return PlayerConfiguration(
        id=id, coordinates=hero_coordinates,
        sprite_sheet_path=HEROES_SPRITE_SHEETS_PATHS.get('hero1'),
        health_points=INITIAL_HEALTH_POINTS,
        weapon=None)


def reinit_hero(hero: Hero) -> None:
    new_cell: Coordinates = generate_random_cell_coordinates_on_map()
    hero.revive(new_cell)
