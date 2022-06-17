from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class ObjectCoordinates:
    cell_position: Coordinates
    position_within_cell: Coordinates
