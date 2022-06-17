from typing import Dict, List

import pygame

from hero_game.src.shared.constants import ASSETS_IMAGES_PATH
from hero_game.src.shared.models import Coordinates

MAPS_PATH = f'{ASSETS_IMAGES_PATH}/maps'

MAPS_PATHS: Dict[str, str] = {
    'nature': f'{MAPS_PATH}/map_nature.tmx',
}

MOVEMENT_KEYBOARD_KEYS: List[int] = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]

GAME_TITLE: str = 'HERO GAME'

MOVE_UP: str = 'up'

MOVE_DOWN: str = 'down'

MOVE_RIGHT: str = 'right'

MOVE_LEFT: str = 'left'

NB_HORIZONTAL_CELLS: int = 12

NB_VERTICAL_CELLS: int = 12

CELL_SIZE: int = 64

INITIAL_HEALTH_POINTS: int = 100

MOVEMENT_TRANSLATION_VECTORS_LINKS: dict = {
    pygame.K_UP: (Coordinates(0, -1), MOVE_UP),
    pygame.K_DOWN: (Coordinates(0, 1), MOVE_DOWN),
    pygame.K_RIGHT: (Coordinates(1, 0), MOVE_RIGHT),
    pygame.K_LEFT: (Coordinates(-1, 0), MOVE_LEFT),
}
