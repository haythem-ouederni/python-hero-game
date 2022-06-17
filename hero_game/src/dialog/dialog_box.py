from typing import List

import pygame

from hero_game.src.dialog.constants import DIALOG_PATHS, DIALOG_WIDTH, DIALOG_HEIGHT, DIALOG_TEXT_VERTICAL_GAP, \
    DIALOG_FONT_SIZE, DIALOG_TEXT_HORIZONTAL_GAP
from hero_game.src.shared.constants import ASSETS_FONTS_PATH
from hero_game.src.shared.models import Coordinates


class DialogBox:

    def __init__(self, coordinates: Coordinates, text: List[str], is_Hero: bool):
        self.coordinates = coordinates
        # load the box image
        self.box = pygame.image.load(DIALOG_PATHS.get('dialog1'))
        # Set the size
        self.box = pygame.transform.scale(self.box, (DIALOG_WIDTH, DIALOG_HEIGHT))

        # set the text
        self.text: List[str] = text

        # set the font
        self.font = pygame.font.Font(f'{ASSETS_FONTS_PATH}/dialog_font.ttf', DIALOG_FONT_SIZE)

        self.is_Hero: bool = is_Hero

    def render(self, screen) -> None:
        if type(self.text) == str:
            self._render_for_from_string(screen)
        else:
            self._render_from_list(screen)

    def _render_for_from_string(self, screen) -> None:
        self._render_common(0, screen, self.text)

    def _render_from_list(self, screen) -> None:
        index: int = 0
        for text in self.text:
            self._render_common(index, screen, text)
            index += 1

    def _render_common(self, index, screen, text) -> None:
        screen.blit(self.box, (self.coordinates.x, self.coordinates.y - (index * DIALOG_HEIGHT)))
        text_with_font = self.font.render(text, False, (0, 0, 0))
        screen.blit(text_with_font,
                    (self.coordinates.x + DIALOG_TEXT_HORIZONTAL_GAP,
                     self.coordinates.y + DIALOG_TEXT_VERTICAL_GAP - (index * DIALOG_HEIGHT)))

    def update_text(self, new_text: List[str], screen) -> None:
        self.text = new_text
        self.render(screen)
