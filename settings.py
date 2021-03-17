import pygame

class Settings():
    """A class to store all settings for Max Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = int(1200)
        self.screen_height = int(800)
        self.bg_color = (25, 175, 255)
        self.bg_image = pygame.image.load("images/background.jpg")

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = int(3)

        # Bullet settings
        self.bullet_speed_factor = int(3)
        self.bullet_width = int(5)
        self.bullet_height = int(10)
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = int(3)

        # Alien settings
        self.fleet_drop_speed = int(10)

        # How quickly the game speeds up
        self.speedup_scale = 1.25

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = int(1)
        self.bullet_speed_factor = int(3)
        self.alien_speed_factor = int(1)

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = int(1)

        # Scoring
        self.alien_points = int(10)

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
