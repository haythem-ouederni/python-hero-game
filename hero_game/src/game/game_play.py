import functools
from typing import List

from hero_game.src.dialog.dialog_box import DialogBox
from hero_game.src.dialog.factories import build_dialog_text_for_player, build_dialog_text_for_enemies
from hero_game.src.player.enemy import Enemy
from hero_game.src.player.hero import Hero


def play_enemies(enemies: List[Enemy], hero: Hero, hero_dialog_box: DialogBox, enemies_dialog_box: DialogBox,
                 screen) -> bool:
    for enemy in enemies:
        enemy.play(hero)
        update_box_dialogs(hero, enemies, hero_dialog_box,
                           enemies_dialog_box, screen)
    return True


def calculate_is_game_over(enemies: List[Enemy], hero: Hero) -> bool:
    return hero.health_points < 1 or is_game_over_for_all_enemies(enemies)


def is_game_over_for_all_enemies(enemies: List[Enemy]) -> bool:
    enemies_health = [enemy.health_points for enemy in enemies]
    return functools.reduce(lambda total_health, current_enemy_health: total_health + current_enemy_health,
                            enemies_health) < 1


def update_box_dialogs(hero: Hero, enemies: List[Enemy], hero_dialog_box: DialogBox,
                       enemies_dialog_box: DialogBox, screen) -> None:
    if hero.health_points < 1 and not is_game_over_for_all_enemies(enemies):
        hero_dialog_box.update_text('Hero lost', screen)
        enemies_dialog_box.update_text('Enemies win', screen)
    elif hero.health_points > 0 and is_game_over_for_all_enemies(enemies):
        hero_dialog_box.update_text('Hero wins', screen)
        enemies_dialog_box.update_text('Enemies lost', screen)
    else:
        hero_dialog_box.update_text(build_dialog_text_for_player('Hero', hero), screen)
        enemies_dialog_box.update_text(build_dialog_text_for_enemies('Enemies', enemies), screen)
