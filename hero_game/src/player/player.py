from __future__ import annotations

from typing import Dict, Optional

import pygame

from hero_game.src.game.constants import MOVE_UP, MOVE_DOWN, MOVE_RIGHT, MOVE_LEFT, NB_HORIZONTAL_CELLS, \
    CELL_SIZE, INITIAL_HEALTH_POINTS
from hero_game.src.player.constants import PLAYER_IMAGE_SIZE
from hero_game.src.player.models import PlayerConfiguration
from hero_game.src.shared.models import Coordinates
from hero_game.src.weapon.models import WeaponCharacteristics
from hero_game.src.weapon.weapon import Weapon


class Player(pygame.sprite.Sprite):
    def __init__(self, player_config: PlayerConfiguration):
        super().__init__()
        self.id = player_config.id
        # image
        self.player_sprite_sheet = pygame.image.load(player_config.sprite_sheet_path)
        self.images = self.build_animation_images()
        # we begin by extracting the image at the top left of the sprite sheet
        self.image: pygame.Surface = self.get_player_image(0, 0)
        # self.rect will define the player's position
        self.rect: pygame.Rect = self.image.get_rect()

        # position
        self.current_cell_position: Coordinates = player_config.coordinates.cell_position
        self.position_within_cell: Coordinates = player_config.coordinates.position_within_cell

        # weapon
        self.weapon: Optional[WeaponCharacteristics] = player_config.weapon

        # health points
        self.health_points: int = player_config.health_points

    def change_animation(self, name) -> None:
        self.image = self.images.get(name, self.get_player_image(0, 0))

    def calculate_player_position(self) -> [int, int]:
        new_x = self.current_cell_position.x * CELL_SIZE + self.position_within_cell.x
        new_y = self.current_cell_position.y * CELL_SIZE + self.position_within_cell.y
        return [new_x, new_y]

    def update(self) -> None:
        self.rect.topleft = self.calculate_player_position()

    def move(self, movement_information: (Coordinates, str)) -> bool:
        new_cell_x: int = self.current_cell_position.x + movement_information[0].x
        new_cell_y: int = self.current_cell_position.y + movement_information[0].y

        if self._new_coordinates_in_boundaries(new_cell_x, new_cell_y):
            self.current_cell_position.x = new_cell_x
            self.current_cell_position.y = new_cell_y
            self.change_animation(movement_information[1])
            return True

        return False

    def seize_weapon(self, weapon: Weapon) -> bool:
        self.weapon = weapon.weapon_characteristics
        return True

    def build_animation_images(self) -> Dict[str, pygame.Surface]:
        return {
            MOVE_DOWN: self.get_player_image(0, 0),
            MOVE_LEFT: self.get_player_image(0, PLAYER_IMAGE_SIZE),
            MOVE_RIGHT: self.get_player_image(0, PLAYER_IMAGE_SIZE * 2),
            MOVE_UP: self.get_player_image(0, PLAYER_IMAGE_SIZE * 3),
        }

    def get_player_image(self, x, y) -> pygame.Surface:
        image: pygame.Surface = pygame.Surface([PLAYER_IMAGE_SIZE, PLAYER_IMAGE_SIZE]).convert_alpha()
        # remove the background color
        image.set_colorkey([0, 0, 0])
        # use blit to extract a piece of the sprite sheet to get our image
        image.blit(self.player_sprite_sheet, (0, 0), (x, y, PLAYER_IMAGE_SIZE, PLAYER_IMAGE_SIZE))
        return image

    def is_in_same_cell(self, other_player: Player) -> bool:
        return (other_player.current_cell_position.x == self.current_cell_position.x
                and other_player.current_cell_position.y == self.current_cell_position.y)

    def attack(self, other_player: Player) -> bool:
        if self.weapon and self.health_points > 0 and other_player.health_points > 0:
            other_player.decrease_health(self.weapon.attack_damage)
            if other_player.weapon is not None and other_player.weapon.defense_damage is not None:
                self.decrease_health(other_player.weapon.defense_damage)
            return True
        return False

    def increase_health(self, amount: int) -> None:
        if self.health_points + amount > INITIAL_HEALTH_POINTS:
            self.health_points = INITIAL_HEALTH_POINTS
        else:
            self.health_points += amount

    def decrease_health(self, amount: int) -> None:
        if self.health_points - amount < 0:
            self.health_points = 0
        else:
            self.health_points -= amount

    def _new_coordinates_in_boundaries(self, new_cell_x: int, new_cell_y: int) -> bool:
        return self._new_x_in_boundaries(new_cell_x) and self._new_y_in_boundaries(new_cell_y)

    @staticmethod
    def _new_y_in_boundaries(new_cell_x: int) -> bool :
        return 0 <= new_cell_x < NB_HORIZONTAL_CELLS

    @staticmethod
    def _new_x_in_boundaries(new_cell_x: int) -> bool :
        return 0 <= new_cell_x < NB_HORIZONTAL_CELLS
