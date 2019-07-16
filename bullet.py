import arcade

class Bullet(arcade.Sprite):
    """
    Class for bullets fired from the ship.
    """
    def __init__(self, ai_settings, ship):
        #TODO: Try drawing the sprite as opposed to rendering it as a sprite.
        super().__init__("images/bullet.png")
        self.ai_settings = ai_settings
        
        self.center_x = ship.center_x
        self.bottom = ship.top
        self.color = arcade.color.RED
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """
        Move bullet up the screen.
        """

        self.bottom += self.speed_factor


    