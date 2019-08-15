class Settngs():
    """A class to store all settings for Max Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 175, 255)

        # Ship settings
        self.ship_speed_factor = 15

        # Bullet settings
        self.bullet_speed_factor = 30
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0