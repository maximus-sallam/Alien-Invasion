"""This file is for testing"""
import pygame
import math

class Block(pygame.sprite.Sprite):
    """ This class represents the ball that moves in a circle. """

    def __init__(self, color, width, height):
        """ Constructor that create's the ball's image. """
        super().__init__()
        self.image =pygame.image.load('images/abby.png')
        self.rect = self.image.get_rect()
        self.radius = 25
        self.angle = 0.1

    def update(self):
        """ Update the ball's position. """
        # Calculate a new x, y
        self.rect.x = self.radius * math.sin(self.angle / 75) + 150
        self.rect.y = self.radius * math.cos(self.angle / 75) + 150
        self.angle += 0.25


# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode((300, 300))

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
block = Block(0, 0, 0)
all_sprites_list.add(block)

# Loop until the user clicks the close button.
done = False

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites_list.update()
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
