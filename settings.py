class Settings():
    """Stores settings for game"""

    def __init__ (self):
        """Initialize the games settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Enemy settings
        self.enemy_speed_factor = .1
        # Goomba settings
        self.goomba_direction = 1
        # Koopa settings
        self.koopa_direction = 1
