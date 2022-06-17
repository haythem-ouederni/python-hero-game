from typing import List

import pygame

from hero_game.src.dialog.dialog_box import DialogBox
from hero_game.src.game.constants import MOVEMENT_TRANSLATION_VECTORS_LINKS, MOVEMENT_KEYBOARD_KEYS
from hero_game.src.game.game_play import update_box_dialogs
from hero_game.src.player.enemy import Enemy
from hero_game.src.player.factories.enemy import reinit_enemy
from hero_game.src.player.factories.hero import reinit_hero
from hero_game.src.player.hero import Hero
from hero_game.src.player.player import Player
from hero_game.src.weapon.facotries import reinit_weapon
from hero_game.src.weapon.weapon import Weapon


def handle_input(hero: Hero, event, enemies: List[Enemy], weapons: List[Weapon], hero_dialog_box: DialogBox,
                 enemies_dialog_box: DialogBox, screen) -> bool:
    if hero.health_points < 1:
        return True
    if event.type == pygame.KEYDOWN and MOVEMENT_KEYBOARD_KEYS.__contains__(event.key):
        is_ok: bool = hero.move(MOVEMENT_TRANSLATION_VECTORS_LINKS[event.key])
        if is_ok: hero.increase_health(1)
        return is_ok
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        is_ok: bool = handle_seize_weapon(hero, weapons)
        if is_ok: hero.increase_health(1)
        return is_ok
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
        is_ok: bool = handle_attack(hero, enemies)
        if is_ok: hero.increase_health(1)
        return is_ok
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        return replay(hero, enemies, weapons, hero_dialog_box,
                      enemies_dialog_box, screen)
    update_box_dialogs(hero, enemies, hero_dialog_box,
                       enemies_dialog_box, screen)
    return False

def handle_attack(hero: Hero, enemies: List[Enemy]) -> bool:
    enemies_in_same_cell: List[Enemy] = list(filter(lambda enemy: enemy.is_in_same_cell(hero), enemies))
    # because we may have many enemies at the same cell and that they can attack back getting the health to 0
    is_attack_possible = len(enemies_in_same_cell) > 0
    i: int = 0
    while is_attack_possible and i < len(enemies_in_same_cell):
        enemy_in_same_cell: Enemy = enemies_in_same_cell[i]
        i += 1
        is_attack_possible = hero.attack(enemy_in_same_cell)

    return is_attack_possible


def replay(hero: Hero, enemies: List[Enemy], weapons: List[Weapon], hero_dialog_box: DialogBox,
           enemies_dialog_box: DialogBox, screen) -> bool:
    reinit_hero(hero)

    for enemy in enemies:
        reinit_enemy(enemy)

    for weapon in weapons:
        reinit_weapon(weapon)

    update_box_dialogs(hero, enemies, hero_dialog_box,
                       enemies_dialog_box, screen)

    return True


def handle_seize_weapon(hero: Hero, weapons: List[Weapon]) -> bool:
    weapons_in_same_cell: List[Enemy] = list(
        filter(lambda weapon: is_weapon_and_player_in_same_cell(weapon, hero), weapons))
    # because we may have many enemies at the same cell and that they can attack back getting the health to 0
    if len(weapons_in_same_cell) > 0:
        # get the fist weapon
        hero.seize_weapon(weapons_in_same_cell[0])
        return True
    return False


def is_weapon_and_player_in_same_cell(weapon: Weapon, player: Player) -> bool:
    return (player.current_cell_position.x == weapon.current_cell_position.x
            and player.current_cell_position.y == weapon.current_cell_position.y)
