from typing import Dict

from hero_game.src.shared.constants import ASSETS_IMAGES_PATH


DIALOG_IMAGES_PATH = f'{ASSETS_IMAGES_PATH}/dialog'

DIALOG_PATHS: Dict[str, str] = {
    'dialog1': f'{DIALOG_IMAGES_PATH}/dialog-box-1.png',
}

DIALOG_WIDTH: int = 415

DIALOG_HEIGHT: int = 20


DIALOG_FONT_SIZE: int = 8

DIALOG_TEXT_HORIZONTAL_GAP: int = 25

DIALOG_TEXT_VERTICAL_GAP: int = 5
