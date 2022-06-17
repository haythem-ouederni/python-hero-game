import random

from hero_game.src.game.constants import INITIAL_HEALTH_POINTS, MOVEMENT_TRANSLATION_VECTORS_LINKS
from hero_game.src.player.constants import MOVE_DIRECTIONS
from hero_game.src.player.models import PlayerConfiguration
from hero_game.src.player.player import Player
from hero_game.src.shared.models import Coordinates
from hero_game.src.weapon.models import WeaponCharacteristics


class Enemy(Player):
    def __init__(self, enemy_config: PlayerConfiguration):
        super(Enemy, self).__init__(enemy_config)

    def play(self, hero: Player) -> bool:
        if self.health_points < 1:
            return False
        elif self.is_in_same_cell(hero):
            self.increase_health(1)
            return self.attack(hero)
        else:
            self.increase_health(1)
            return self.move_randomly()

    def move_randomly(self) -> bool:
        has_moved: bool = False

        while not has_moved:
            random_direction: str = random.choice(MOVE_DIRECTIONS)
            has_moved = self.move(MOVEMENT_TRANSLATION_VECTORS_LINKS[random_direction])

    def revive(self, new_current_cell_position: Coordinates, new_weapon: WeaponCharacteristics) -> None:
        self.health_points = INITIAL_HEALTH_POINTS
        self.weapon = new_weapon
        self.current_cell_position = new_current_cell_position
        self.update()
