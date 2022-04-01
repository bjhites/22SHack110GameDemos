# Simple pygame program

# Import and initialize the pygame library
import pygame
import pygame_gui
from player import Player
from ball import Ball

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([800, 500])

# TODO Instantiate game objects

# TODO Constant rect for game board

# TODO Handles gui 


# TODO Constant gui for the score 


                                             
# Run until the user asks to quit
clock = pygame.time.Clock()
running = True
while running:
    # Sets frame rate
    time_delta = clock.tick(60)/1000.0

    # Check if goal has happened

    # Fill background
    screen.fill((10, 10, 10))

    # Draw the game board
    
    # Handle goal results from point
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO Fill the background with white

    # TODO Move player rectangles


    # TODO Check ball collisions with paddles and walls
    
    # TODO Move ball


    # TODO Drawing players paddles

    # TODO Drawing ball,

    # TODO Set score

    # TODO Flips screen so players can see all the updates
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

