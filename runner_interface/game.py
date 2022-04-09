"""This module sets the scene and starts the game loop."""

# Import the pygame library and some event types, such as key presses
from colorama import Back
import pygame
from pygame.locals import (
    K_UP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# Import our custom classes
from background import Background
from player import Player
from floor import Floor

# Initialize the pygame library
pygame.init()

# Constants for screen width and height, floor height, and player speed essentially
SCREEN_WIDTH: int = 1200
SCREEN_HEIGHT: int = 700
FLOOR_HEIGHT: int = 130

# Clock to control frame rate 
clock = pygame.time.Clock()

# Set up the drawing window and size
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# TODO Instantiate the background
background:Background = Background()

# TODO Instantiate the floor
floor: Floor = Floor(0, SCREEN_HEIGHT - FLOOR_HEIGHT, SCREEN_WIDTH, FLOOR_HEIGHT)

# TODO Create a list of ground or platform Rects the player can collide with
platforms: list[pygame.rect.Rect] = [floor.rect]

# TODO Instantiate player, passing in the position, width, height, and ground collision list

# Run the game until the user asks to quit or dies and `running` is set to False
running = True
# Game loop
while running:
    for event in pygame.event.get():
        # Check for QUIT event (user closes window). If QUIT, then set running to false.
        if event.type == QUIT:
            running = False
        # Check if user presses down on a key
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                # If the Esc key is pressed, then set running to False
                running = False
            elif event.key == K_UP:
                # TODO call jump method on player
                ...

    # TODO Update and render scrolling background
    background.render(screen)

    # Render the floor
    floor.render(screen)

    # TODO Update the player sprite

    # TODO Call gravity on player, so the player falls at the right times

    # Flip the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(40)

# Done playing
pygame.quit()