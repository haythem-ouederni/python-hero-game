from typing import Dict, List

import pygame

from hero_game.src.shared.constants import ASSETS_IMAGES_PATH

PLAYER_IMAGE_SIZE: int = 32

HEROES_IMAGES_PATH = f'{ASSETS_IMAGES_PATH}/heroes'

HEROES_SPRITE_SHEETS_PATHS: Dict[str, str] = {
    'hero1': f'{HEROES_IMAGES_PATH}/hero-1-sprite-sheet.png',
}

ENEMIES_IMAGES_PATH = f'{ASSETS_IMAGES_PATH}/enemies'

ENEMIES_SPRITE_SHEETS_PATHS: Dict[str, str] = {
    'enemy1': f'{ENEMIES_IMAGES_PATH}/enemy-1-sprite-sheet.png',
}

MOVE_DIRECTIONS: List[int] = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]
