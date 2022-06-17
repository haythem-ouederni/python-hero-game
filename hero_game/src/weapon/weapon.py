import pygame

from hero_game.src.game.constants import CELL_SIZE
from hero_game.src.shared.models import ObjectCoordinates, Coordinates
from hero_game.src.weapon.constants import WEAPON_IMAGE_SIZE
from hero_game.src.weapon.models import WeaponCharacteristics


class Weapon(pygame.sprite.Sprite):

    def __init__(self, weapon_characteristics: WeaponCharacteristics, position: ObjectCoordinates):
        super().__init__()

        self.weapon_characteristics = weapon_characteristics

        # image
        self.weapon_sprite_sheet = pygame.image.load(weapon_characteristics.img_path)
        # we begin by extracting the image at the top left of the sprite sheet
        self.image: pygame.Surface = self.get_weapon_image(0, 0)
        # self.rect will define the weapon's position
        self.rect: pygame.Rect = self.image.get_rect()

        # position
        self.current_cell_position: Coordinates = position.cell_position
        self.position_within_cell: Coordinates = position.position_within_cell

    def get_weapon_image(self, x, y) -> pygame.Surface:
        image: pygame.Surface = pygame.Surface([WEAPON_IMAGE_SIZE, WEAPON_IMAGE_SIZE]).convert_alpha()
        # remove the background color
        image.set_colorkey([0, 0, 0])
        # use blit to extract a piece of the sprite sheet to get our image
        image.blit(self.weapon_sprite_sheet, (0, 0), (x, y, WEAPON_IMAGE_SIZE, WEAPON_IMAGE_SIZE))
        return image

    def calculate_weapon_position(self) -> [int, int]:
        new_x = self.current_cell_position.x * CELL_SIZE + self.position_within_cell.x
        new_y = self.current_cell_position.y * CELL_SIZE + self.position_within_cell.y
        return [new_x, new_y]

    def update(self) -> None:
        self.rect.topleft = self.calculate_weapon_position()

    def regenerate(self, new_weapon_characteristics: WeaponCharacteristics, new_position: ObjectCoordinates) -> None:
        self.__init__(new_weapon_characteristics, new_position)
        self.update()
