"""The Background class for the scrolling background."""

import pygame


class Background():
    image: pygame.surface.Surface
    rect: pygame.rect.Rect
    x0: int
    y0: int
    x1: int 
    y1: int
    moving_speed: int

    def __init__(self):
        """Contruct scrolling background objects."""
         
    def update(self):
        """Move the background by moving speed amount."""
        # TODO Update the x0, x1 attributes

    def render(self, screen):
        """Draw background object to the screen"""