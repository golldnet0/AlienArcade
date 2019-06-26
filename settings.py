class Settings():
    """
    Stores all the settings needed for the game.
    """

    def __init__(self):
        """
        Initializes game settings.
        """

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #  bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1

        self.initizlize_dynamic_settings()

    def initizlize_dynamic_settings(self):
        self.ship_speed_factor = 1.5  # how fast the ship will move (1.5px)
        self.ship_lives = 2
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1

        #  +1 means to the right on the horizontal axis
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
