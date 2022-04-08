# Simple pygame program

# Import and initialize the pygame library
import pygame
import math
from ball import Ball

ball = Ball(10, 0, 205, 3, [1, 0])


def main():
    pygame.init()
    fixed_update: int = 0
    # Set up the drawing window
    screen = pygame.display.set_mode([800, 500])

    triangle: pygame.Rect = pygame.Rect(400, 200, 50, 50)
    triangle_norm: pygame.Vector2 = pygame.Vector2(-math.cos(45 * (math.pi)/180), math.sin((45 * (math.pi)/180)))

                        
    # Run until the user asks to quit
    clock = pygame.time.Clock()
    running = True
    while running:
        # update fixed update
        fixed_update += 1

        clock.tick(60)
        # Draw the game board
        screen.fill((100, 20, 100))

        pygame.draw.rect(screen, (200, 200, 200), ball.getRect())
        pygame.draw.circle(screen, (10, 10, 10), (ball.getRect().centerx, ball.getRect().centery), ball.radius)

        # Draw triangle off rect points
        pygame.draw.polygon(screen, (10, 10, 10), [(triangle.bottomleft), (triangle.bottomright), (triangle.topright)])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        ball.move()

        # don't want multiple collisions in a short time span
        if (fixed_update > 10):
            # Check points along line, since pygame has no collisions for triangles
            if(ball.getRect().collidepoint(triangle.center)):
                ball.bounce(triangle_norm)
                fixed_update = 0

            elif(ball.getRect().collidepoint(triangle.topright)):
                ball.bounce(triangle_norm)
                fixed_update = 0
            
            elif(ball.getRect().collidepoint(triangle.bottomright)):
                ball.bounce(triangle_norm)
                fixed_update = 0

        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()


if __name__ == '__main__':
    main()

