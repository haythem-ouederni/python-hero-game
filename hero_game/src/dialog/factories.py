import functools
from typing import List

from hero_game.src.dialog.constants import DIALOG_HEIGHT, DIALOG_WIDTH
from hero_game.src.dialog.dialog_box import DialogBox
from hero_game.src.game.constants import INITIAL_HEALTH_POINTS
from hero_game.src.player.enemy import Enemy
from hero_game.src.player.hero import Hero
from hero_game.src.player.player import Player
from hero_game.src.shared.models import Coordinates


def generate_hero_dialog_box(screen, hero: Hero) -> DialogBox:
    y: int = screen.get_size()[1] - DIALOG_HEIGHT
    hero_dialog_box_coordinate: Coordinates = Coordinates(x=0, y=y)
    text_for_hero: str = build_dialog_text_for_player('Hero', hero)
    return generate_dialog_box(hero_dialog_box_coordinate, text_for_hero, True)


def generate_enemies_dialog_box(screen, enemies: List[Enemy]) -> DialogBox:
    x: int = screen.get_size()[0] - DIALOG_WIDTH
    y: int = screen.get_size()[1] - DIALOG_HEIGHT
    enemies_dialog_box_coordinate: Coordinates = Coordinates(x=x, y=y)
    text_for_enemies: List[str] = build_dialog_text_for_enemies('Enemies', enemies)
    return generate_dialog_box(enemies_dialog_box_coordinate, text_for_enemies)


def generate_dialog_box(coordinates: Coordinates, text: List[str], is_hero: bool = False) -> DialogBox:
    return DialogBox(coordinates, text, is_hero)


def build_dialog_text_for_enemies(label: str, enemies: List[Enemy]) -> List[str]:
    return [label + ' ' + build_dialog_text_for_player(enemy.id, enemy) for enemy in enemies]


def build_dialog_text_for_player(label: str, player: Player) -> str:
    text_for_player: str = f'{label}: - Health {player.health_points}/{INITIAL_HEALTH_POINTS}'
    weapon = player.weapon
    if weapon:
        text_for_player += f'- Weapon: {weapon.name} - Attack: {weapon.attack_damage} - Defense: {weapon.defense_damage or 0}'
    return text_for_player
