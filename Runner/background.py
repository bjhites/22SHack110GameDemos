"""The Background class for the scrolling background."""

from turtle import speed
import pygame


class Background():
    image: pygame.surface.Surface
    rect: pygame.rect.Rect
    x0: int
    x1: int
    y: int
    speed: int

    def __init__(self):
        """Contruct scrolling background objects."""
        # TODO Load background image
        self.image = pygame.image.load("assets/background.png")
        self.rect = self.image.get_rect()
        self.x0 = 0
        self.x1 = self.rect.width
        self.y = 0
        self.speed = 10
         
    def update(self):
        """Move the background by moving speed amount."""
        # TODO Update the x0, x1 attributes
        self.x0 -= self.speed
        self.x1 -= self.speed
        if self.x0 <= -self.rect.width:
            self.x0 = self.rect.width
        if self.x1 <= -self.rect.width:
            self.x1 = self.rect.width

    def render(self, screen):
        """Draw background object to the screen"""
        screen.blit(self.image, (self.x0, self.y))
        screen.blit(self.image, (self.x1, self.y))
