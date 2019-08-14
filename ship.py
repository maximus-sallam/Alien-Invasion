import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's cneter value, not the rect
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_down:
            self.bottom += self.ai_settings.ship_speed_factor

        if self.moving_up:
            self.bottom -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)