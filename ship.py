import arcade


class Ship(arcade.Sprite):
    def __init__(self, ai_settings):
        super().__init__("images/shipBlue_manned.png")
        self.ai_settings = ai_settings
        self.scale = 0.5
        self.center_x = self.ai_settings.screen_width / 2
        self.bottom = 0
        self.move_right = False
        self.move_left = False

    def update(self): 
        """
        Updates ship's position (movement)
        Overrides the update method in arcade.Sprite
        """
        #  The example code provided in the official API doesn't account for 
        #  pressing left and right at the same time as they're switching
        #  directions. Using flags instead creates a smoother movement.
        if self.move_right:
            self.center_x += self.ai_settings.ship_speed_factor
        if self.move_left:
            self.center_x -= self.ai_settings.ship_speed_factor

        if self.right > self.ai_settings.screen_width:
            self.right = self.ai_settings.screen_width - 1
        
        if self.left < 0:
            self.left = 1
        