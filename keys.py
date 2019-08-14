import sys
import pygame

def run_game():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Keys")
    screen.fill((0, 0, 255))
    pygame.display.update()

    # Start the main loop.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

run_game()