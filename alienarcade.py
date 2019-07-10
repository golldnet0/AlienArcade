import arcade
import settings
"""
Must be ran with sudo on linux.
"""
class AlienArcade(arcade.Window):
    def __init__(self):
        self.ai_settings = settings.Settings()
        super().__init__(self.ai_settings.screen_width, 
                         self.ai_settings.screen_height, 
                         "Alien Arcade")
        arcade.set_background_color(arcade.color.WHITE)
        

        #  create sprite lists and set them to none
        self.alien_list = None
        self.ship = None

    def setup(self):
        #  Create sprites and sprite lists here
        
        self.ship = arcade.Sprite("images/shipBlue_manned.png")
        self.ship.scale = 0.5
        self.ship.center_x = self.ai_settings.screen_width / 2
        self.ship.bottom = 0



    def on_draw(self):
        """
        Render the screen.
        """

        #  Call this function before drawing, it will clear everything but the 
        #  background color.
        arcade.start_render()

        #  call all .draw() methods here
        self.ship.draw()

    def update(self, delta_time):
        """
        All the logic to move and all game logic
        """
        self.ship.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.ship.change_x = self.ai_settings.ship_speed_factor
        if key == arcade.key.LEFT:
            self.ship.change_x = -self.ai_settings.ship_speed_factor
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.ship.change_x = 0

    def on_mouse_press(self, x, y, button, modifiers):
        pass


def main():
    print("Prepare for the alien invasion.")
    game = AlienArcade()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()