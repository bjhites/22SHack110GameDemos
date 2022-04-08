import pygame
import math


class Ball:
    x: float
    y: float
    radius: int
    speed: float
    vector: list[float]
    maxBounce: float = 75 * (math.pi / 180)

    def __init__(self, radius, x, y, speed):
        """Construct a ball object."""
        ...

    # TODO Create some getters and setters for attributes in the object

    def move(self):
       """Move ball."""
       ...

    def changeVector(self, paddle: pygame.Rect):
        """Flips the x direction, so that it reverses back towards other paddle, as well as handling paddle curving"""
        # Ball gets faster over time
        ...

    def wallBounce(self, paddle: pygame.Rect):
        """Reverse y direction, so ball moves off walls"""
        ...

    def checkWallCollisions(self):
        """Is the ball about to move off screen, but not into a goal."""
        ...

    def checkPoint(self) -> int:
        """Is the ball moving past a paddle, into a goal."""
        ...

    def getRect(self) -> pygame.Rect:
        """Creates a rect object to be used for collisions with pygame rect."""


    