import pygame
from hero_game.src.game.models import GameConfiguration
from hero_game.src.game.game import Game


def launch_game() -> None:
    pygame.init()

    # set the game configuration
    game_configuration: GameConfiguration = GameConfiguration(window_height=800, window_width=800)

    # create the game instance
    newGame: Game = Game(game_configuration)

    # launch the game
    newGame.run()


if __name__ == '__main__':
    launch_game()
