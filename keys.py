import sys
import pygame

def keydown_event():
    print("poop")

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
                keydown_event()

run_game()