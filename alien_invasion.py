import pygame

from settings import Settngs
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settngs()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Max Invasion")

    # Make a ship.
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

run_game()