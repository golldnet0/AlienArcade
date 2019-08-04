import arcade

class Alien_Bullet(arcade.Sprite):
    """
    Class for the alien's bullets.
    """
    
    def __init__(self, ai_settings, an_alien):
        super().__init__("images/alien_bullet.png")
        self.ai_settings = ai_settings
        self.alien = an_alien

        self.center_x = an_alien.center_x
        self.top = an_alien.bottom
        self.speed_factor = ai_settings.bullet_speed_factor /3

    def update(self):
        self.bottom -= self.speed_factor

