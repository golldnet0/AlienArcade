import arcade


class Ship(arcade.Sprite):
    def __init__(self, ai_settings):
        super().__init__("images/shipBlue_manned.png")
        self.ai_settings = ai_settings
        self.scale = 0.5
        self.center_x = self.ai_settings.screen_width / 2
        self.bottom = 0