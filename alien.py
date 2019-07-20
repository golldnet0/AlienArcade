import arcade

class Alien(arcade.Sprite):
    """
    Class for the enemy aliens in the game.
    """

    def __init__(self, ai_settings):
        """
        Creates an enemy alien.
        """

        super().__init__("images/shipGreen_manned.png")
        self.ai_settings = ai_settings
        self.scale = 0.6

    # def update(self):
        #  self.center_x += self.ai_settings.alien_speed_factor
        # pass

    def check_edges(self):
        """
        Check to see if the alien has reached the edge of the screen.
        """
        pass