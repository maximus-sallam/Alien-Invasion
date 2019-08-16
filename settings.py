import pygame

class Settngs():
    """A class to store all settings for Max Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 175, 255)
        self.bg_image = pygame.image.load("images/background.jpg")

        """Background Music"""
        # All the stars are closer
        # self.bg_sound = (pygame.mixer.music.load("sound/stars.mp3"), pygame.mixer.music.play(-1, 19.5))
        # Star wars main theme
        self.bg_sound = (pygame.mixer.music.load("sound/starwars.mp3"), pygame.mixer.music.play(-1, 0))

        # Ship settings
        self.ship_speed_factor = 15
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 30
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1