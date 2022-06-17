from typing import List, Tuple

import pygame
import pyscroll
import pytmx

import hero_game.src.weapon.facotries as weapons_factory
from hero_game.src.dialog import factories as dialog_box_factory
from hero_game.src.game.constants import MAPS_PATHS, GAME_TITLE
from hero_game.src.game.game_play import play_enemies, calculate_is_game_over, update_box_dialogs
from hero_game.src.game.inputs_handler import handle_input, replay
from hero_game.src.game.models import GameConfiguration
from hero_game.src.player.enemy import Enemy
from hero_game.src.player.factories import hero as hero_factory, enemy as enemy_factory
from hero_game.src.player.hero import Hero
from hero_game.src.weapon.weapon import Weapon


class Game:

    def __init__(self, game_configuration: GameConfiguration):
        self.nb_characters = 0
        # Create the game window
        self.screen = pygame.display.set_mode((game_configuration.window_width,
                                               game_configuration.window_height))
        pygame.display.set_caption(GAME_TITLE)

        # Create the main map layers
        self.layers_group: pyscroll.group.PyscrollGroup = self._build_layers_group(self.screen.get_size())

        # generate the hero
        self.hero: Hero = hero_factory.generate_hero(self.nb_characters)
        self.nb_characters += 1

        # generate the enemies
        self.enemies: List[Enemy] = enemy_factory.generate_enemies(self.nb_characters, 2)
        self.nb_characters += len(self.enemies)

        # generate weapons
        self.weapons: List[Weapon] = weapons_factory.generate_weapons(6)

        # generate dialog boxes
        self.dialog_box_hero = dialog_box_factory.generate_hero_dialog_box(self.screen, self.hero)
        self.dialog_box_enemies = dialog_box_factory.generate_enemies_dialog_box(self.screen, self.enemies)

        self.layers_group.add(self.hero)
        self.layers_group.add(self.enemies)
        self.layers_group.add(self.weapons)

        self.is_player_turn: bool = True

    @staticmethod
    def _build_layers_group(screen_size: Tuple[int, int]) -> pyscroll.group.PyscrollGroup:
        # Load the map
        tmx_data: pytmx.TiledMap = pytmx.util_pygame.load_pygame(MAPS_PATHS.get('nature'))
        map_data: pyscroll.data.TiledMapData = pyscroll.data.TiledMapData(tmx_data)
        map_layer: pyscroll.orthographic.BufferedRenderer = pyscroll.orthographic.BufferedRenderer(
            map_data,
            screen_size
        )
        # Setup/init the layers group
        return pyscroll.group.PyscrollGroup(map_layer=map_layer, default_layer=3)

    def run(self):
        clock: pygame.time.Clock = pygame.time.Clock()

        # Keep the game window open
        is_game_running: bool = True

        is_game_over: bool = False

        while is_game_running:

            # Draw the layers group
            self.layers_group.update()
            self.layers_group.draw(self.screen)
            self.dialog_box_enemies.render(self.screen)
            self.dialog_box_hero.render(self.screen)
            pygame.display.flip()

            if not self.is_player_turn and not is_game_over:
                self.is_player_turn = play_enemies(self.enemies, self.hero, self.dialog_box_hero,
                                                   self.dialog_box_enemies, self.screen)
                is_game_over = calculate_is_game_over(self.enemies, self.hero)

            # Listen to events on the screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_running = False
                elif is_game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    is_game_over = not replay(self.hero, self.enemies, self.weapons, self.dialog_box_hero,
                                          self.dialog_box_enemies, self.screen)
                elif self.is_player_turn and not is_game_over:
                    self.is_player_turn = not handle_input(self.hero, event, self.enemies, self.weapons,
                                                           self.dialog_box_hero, self.dialog_box_enemies, self.screen)
                    is_game_over = calculate_is_game_over(self.enemies, self.hero)
                    if is_game_over: update_box_dialogs(self.hero, self.enemies, self.dialog_box_hero,
                       self.dialog_box_enemies, self.screen)

            clock.tick(60)

        pygame.quit()
