import pygame


class Ball:
    x: float
    y: float
    radius: int
    speed: float
    vector: list[float]

    def __init__(self, radius, x, y, speed, vector = [1, 0]):
        self.radius = radius
        self.x = x
        self.y = y
        self.speed = speed
        # Ball moves left to start
        self.vector = vector

    def move(self):
        self.x += (self.vector[0] * self.speed)
        self.y += (self.vector[1] * self.speed)
    
    def getRect(self) -> pygame.Rect:
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 3, self.radius * 3)

    def bounce(self, norm: pygame.Vector2):
        """A bounce is essentially a reflection of the subjects angle across the normal of the object its hitting."""
        # Create a pygame vector for ball's current vector, easier to do vector math
        # -1 * y to convert to cartesian plane (y increases going down in pygame screen)
        ball_vec: pygame.Vector2 = pygame.Vector2(self.vector[0], -1 * self.vector[1])

        proj = (ball_vec.dot(norm) / norm.magnitude_squared()) * norm

        orthogonal = ball_vec - proj

        reflection = orthogonal - proj
        # change ball's vector the -1 converts from cartesian plane to pygame window (y increases going down instead of up)
        self.vector = [reflection.x, -1 * reflection.y]


    