import sys
import pygame

def run_game():
    # Initialize pygame
    pygame.init()
    bg_color = (25, 175, 255)
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Keys")

    # Start the main loop for the game.
    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

run_game()