"""This file is for testing"""
import pygame

# initialize game engine
pygame.init()

# Open a window
screen = pygame.display.set_mode((1200, 800))

dead = True
background_image = pygame.image.load("images/background.jpg")

while (dead == True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = False

    screen.blit(background_image, (0, 0))
    pygame.display.flip()