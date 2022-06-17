from typing import Dict, List

from hero_game.src.shared.constants import ASSETS_IMAGES_PATH
from hero_game.src.weapon.models import WeaponCharacteristics

WEAPONS_IMAGES_PATH = f'{ASSETS_IMAGES_PATH}/weapons'

WEAPON_1: WeaponCharacteristics = WeaponCharacteristics(
    name='Arme 1',
    img_path=f'{WEAPONS_IMAGES_PATH}/weapon-1.png',
    attack_damage=5,
    defense_damage=1,
)

WEAPON_2: WeaponCharacteristics = WeaponCharacteristics(
    name='Arme 2',
    img_path=f'{WEAPONS_IMAGES_PATH}/weapon-2.png',
    attack_damage=4,
    defense_damage=0,
)

WEAPON_3: WeaponCharacteristics = WeaponCharacteristics(
    name='Arme 3',
    img_path=f'{WEAPONS_IMAGES_PATH}/weapon-3.png',
    attack_damage=8,
    defense_damage=3,
)

WEAPONS: List[str] = [WEAPON_1, WEAPON_2, WEAPON_3]

WEAPON_IMAGE_SIZE: int = 32
