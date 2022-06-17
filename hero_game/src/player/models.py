from dataclasses import dataclass
from typing import Optional

from hero_game.src.shared.models import ObjectCoordinates
from hero_game.src.weapon.models import WeaponCharacteristics


@dataclass
class PlayerConfiguration:
    coordinates: ObjectCoordinates
    sprite_sheet_path: str
    health_points: int
    weapon: Optional[WeaponCharacteristics]
    id: int
