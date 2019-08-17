import pygame

class Settings():
    """A class to store all settings for Max Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 175, 255)
        self.bg_image = pygame.image.load("images/background.jpg")

        # Ship settings
        self.ship_speed_factor = 15
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed_factor = 30
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1