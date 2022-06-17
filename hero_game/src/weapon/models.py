from dataclasses import dataclass


@dataclass
class WeaponCharacteristics:
    name: str
    img_path: str
    attack_damage: int
    defense_damage: int
