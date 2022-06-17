from hero_game.src.game.constants import INITIAL_HEALTH_POINTS
from hero_game.src.player.models import PlayerConfiguration
from hero_game.src.player.player import Player
from hero_game.src.shared.models import Coordinates


class Hero(Player):
    def __init__(self, hero_config: PlayerConfiguration):
        super(Hero, self).__init__(hero_config)

    def revive(self, new_current_cell_position: Coordinates) -> None:
        self.health_points = INITIAL_HEALTH_POINTS
        self.weapon = None
        self.current_cell_position = new_current_cell_position
        self.update()
