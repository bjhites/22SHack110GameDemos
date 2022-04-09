"""The Background class for the scrolling background."""

import pygame


class Background():
    image: pygame.surface.Surface
    rect: pygame.rect.Rect
    x: int
    y: int
    speed: int

    def __init__(self):
        """Contruct scrolling background objects."""
        # TODO Load background image
        self.image = pygame.image.load("assets/background.png")
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
         
    def update(self):
        """Move the background by moving speed amount."""
        # TODO Update the x0, x1 attributes

    def render(self, screen):
        """Draw background object to the screen"""
        screen.blit(self.image, (self.x, self.y))
