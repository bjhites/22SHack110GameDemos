import pygame

class Player:
    # player attribute has some way to keep track of whether it should be moving and which direction

    def __init__(self, num: int, rect: pygame.Rect):
        """Construct player object."""

    def move(self) -> None:
        """Move player."""

    def getKeyDown(self, key: pygame.event.Event) -> None:
        """Handles event where user presses a key."""
        
    def getKeyUp(self, key: pygame.event.Event) -> None:
        """Handles event where a key is released by user."""

    # TODO getters and setters for attributes