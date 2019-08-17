import pygame
import math
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initializa the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image =pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Load the alien image and set its rect attribute.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.radius = 7.5
        self.angle = 5

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor
                   * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        self.rect.x = self.radius * math.sin(self.angle) + self.rect.x
        self.rect.y = self.radius * math.cos(self.angle) + self.rect.y
        self.angle -= 0.5