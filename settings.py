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

        #  bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 3
        
        self.fleet_drop_speed = 15
        self.speedup_scale = 1.1

        self.initizlize_dynamic_settings()

    def initizlize_dynamic_settings(self):
        self.ship_speed_factor = 5  # how fast the ship will move 
        self.bullet_speed_factor = 15
        self.alien_speed_factor = 2
        self.alien_fire_rate = 995

        #  Alien fleet direction. False means the fleet is moving left.
        self.move_fleet_right = True

    def increase_speed(self):
        """
        Increases the speed of the game upon reaching the next level.
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_fire_rate -= 7
