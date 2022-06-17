import random

from hero_game.src.game.constants import NB_HORIZONTAL_CELLS, NB_VERTICAL_CELLS
from hero_game.src.shared.models import Coordinates


def generate_random_cell_coordinates_on_map() -> Coordinates:
    max_x: int = NB_HORIZONTAL_CELLS - 1
    max_y: int = NB_VERTICAL_CELLS - 1
    return Coordinates(x=generate_random_number(max_x), y=generate_random_number(max_y))


def generate_random_number(max: int) -> int:
    """Return random integer in range [0, max], including both end points.
    """
    return random.randint(0, max)
