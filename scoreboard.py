import arcade

class Scoreboard():
    """
    A class that helps display the current score and level to the screen.
    """

    def __init__(self, stats, ai_settings):
        self.stats = stats
        self.ai_settings = ai_settings

    def draw_score(self):
        """
        Draws the current score to the top right of the screen.
        """
        arcade.draw_text(str(self.stats.score), self.ai_settings.screen_width-50,
                        self.ai_settings.screen_height - 10, arcade.color.BLACK,
                        font_size=18, align="right", anchor_x="right",
                        anchor_y="top")

    def draw_high_score(self):
        """
        Draws the current high score to the top of the screen.
        """
        arcade.draw_text(str(self.stats.high_score), self.ai_settings.screen_width/2,
                         self.ai_settings.screen_height - 10, arcade.color.BLACK, 
                         font_size=18, align="center", anchor_x="center", 
                         anchor_y="top")

    def draw_level(self):
        """
        Draws the current level to the screen
        """
        arcade.draw_text(str(self.stats.level), self.ai_settings.screen_width-50,
                        self.ai_settings.screen_height - 45, arcade.color.BLACK,
                        font_size=18, align="right", anchor_x="right",
                        anchor_y="top")

    def draw_lives(self):
        """
        Draws the lives as icons at the top left of the screen.
        """
        for ship_count in range(self.stats.ship_lives):
            ship_icon = arcade.load_texture("images/playerShip1_blue.png", 
                                            scale=0.3)
            ship_icon.draw(50 + (ship_count * ship_icon.width * 0.3),
                           self.ai_settings.screen_height - 35,
                           ship_icon.width * 0.3, ship_icon.height * 0.3)

            
        
