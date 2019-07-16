import arcade
import settings
from ship import Ship
from bullet import Bullet
"""
Must be ran with sudo on linux.
"""
#  TODO: fire bullets.
class AlienArcade(arcade.Window):
    def __init__(self):
        self.ai_settings = settings.Settings()
        super().__init__(self.ai_settings.screen_width, 
                         self.ai_settings.screen_height, 
                         "Alien Arcade")
        arcade.set_background_color(arcade.color.WHITE)
        

        #  create sprite lists and set them to none
        self.alien_list = None
        self.bullet_list = None
        self.ship = None

    def setup(self):
        #  Create sprites and sprite lists here
        self.ship = Ship(self.ai_settings)

        self.bullet_list = arcade.SpriteList()



    def on_draw(self):
        """
        Render the screen.
        """

        #  Call this function before drawing, it will clear everything but the 
        #  background color.
        arcade.start_render()

        #  call all .draw() methods here
        self.ship.draw()
        self.bullet_list.draw()

    def update(self, delta_time):
        """
        All the logic to move and all game logic
        """
        self.ship.update()

        for bullet in self.bullet_list:
            if bullet.bottom > self.ai_settings.screen_height:
                self.bullet_list.remove(bullet)

        self.bullet_list.update()

    def on_key_press(self, key, modifiers):
        #TODO: Prevent ship moving offscreen.
        if key == arcade.key.RIGHT:
            self.ship.change_x = self.ai_settings.ship_speed_factor
        if key == arcade.key.LEFT:
            self.ship.change_x = -self.ai_settings.ship_speed_factor
        if key == arcade.key.SPACE:
            if len(self.bullet_list) < 3:
                bullet = Bullet(self.ai_settings, self.ship)
                self.bullet_list.append(bullet)
        if key == arcade.key.ESCAPE:
            arcade.close_window()
    
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