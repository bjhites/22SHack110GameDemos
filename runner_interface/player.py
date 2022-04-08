"""The Player class lives here. Player objects include a Surface, Rect, and logic for moving left, right, and jumping on other Surfaces."""

import pygame
from pygame.locals import RLEACCEL


class Player(pygame.sprite.Sprite):
    """The Player extends pygame.sprite.Sprite to take advantage of builtin Sprite methods."""
    movey: int
    image: pygame.surface.Surface
    rect: pygame.rect.Rect
    is_jumping: bool
    is_falling: bool
    collision_list: list[pygame.rect.Rect]

    def __init__(self, x: int, y: int, width: int, height: int, collision_list: list[pygame.rect.Rect]):
        """Constructor takes x and y as coordinates, height and width for the size and a list of Rects (rectangles) the player could collide with."""
        # TODO Extend the pygame Sprite class by calling it's constructor with self

    def update(self):
        """This is called every frame to check for collisions with the floor and apply jumping movement."""
        # TODO Check for collision using a builtin collision method and the list of floors
        # The collidelist method returns the index in the list of the rect a game object collides with or -1 if there was no collision

        # TODO Launch the jump
        
        # TODO Move player rect based on movey value

        # TODO Keep player on the screen
    
    def gravity(self):
        """Turns on the gravity only when the Player object should be falling."""

    def jump(self):
        """If the Player object is not currently jumping, this method starts a jump by changing the values of is_jumping and is_falling."""

    def render(self, screen) -> None:
        """Draw surface of player onto the screen at its rect location."""