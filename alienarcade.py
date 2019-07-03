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
        arcade.set_background_color(arcade.color.BLACK)
        

        #  create sprite lists and set them to none

    def setup(self):
        #  Create sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        #  Call this function before drawing, it will clear everything but the 
        #  background color.
        arcade.start_render()

        #  call all .draw() methods here

    def update(self, delta_time):
        """
        All the logic to move and all game logic
        """
        pass

    def on_key_press(self, key, key_modifiers):
        pass
    
    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


def main():
    print("Prepare for the alien invasion.")
    game = AlienArcade()
    arcade.run()

if __name__ == "__main__":
    main()