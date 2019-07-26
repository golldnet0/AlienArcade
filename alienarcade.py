import arcade
import settings
import math
from ship import Ship
from bullet import Bullet
from alien import Alien
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
        self.bullet_list = None
        self.ship = None
        self.game_running = False

    def setup(self):
        #  Create sprites and sprite lists here
        self.ship = Ship(self.ai_settings)

        self.bullet_list = arcade.SpriteList()

        self.alien_list = arcade.SpriteList()
        self.alien_setup()


    def alien_setup(self):
        #  Create an alien for measurement purposes.
        an_alien = Alien(self.ai_settings)

        #  how many aliens will fit in a row?
        aliens_per_row = math.floor(self.ai_settings.screen_width / 
                                    (an_alien.width *2)) - 1

        #  how many aliens will fit in a column?
        aliens_per_col = math.floor(self.ai_settings.screen_height / 
                                    an_alien.width) - 3

        #  spawn aliens
        for alien_y in range(aliens_per_col):
            for alien_x in range(aliens_per_row):
                some_alien = Alien(self.ai_settings)
                some_alien.left = some_alien.width/2 + (alien_x * some_alien.width *2)
                some_alien.bottom = self.ai_settings.screen_height - (some_alien.height + (alien_y * some_alien.height))
                self.alien_list.append(some_alien)

        an_alien.kill()

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
        self.alien_list.draw()
        if not self.game_running:
            #Draw start button
            arcade.draw_rectangle_filled(self.ai_settings.screen_width /2,
                                        self.ai_settings.screen_height /2, 100,
                                        40, arcade.color.LIGHT_GRAY)
            arcade.draw_text("Start", self.ai_settings.screen_width/2, 
                             self.ai_settings.screen_height/2, arcade.color.BLACK,
                             font_size=18, width=100, align="center",
                             anchor_x="center", anchor_y="center")

    def update(self, delta_time):
        """
        All the logic to move and all game logic
        """
        if self.game_running:
            if len(self.alien_list) == 0:
                self.setup()
                self.ai_settings.increase_speed()

            self.ship.update()

            for bullet in self.bullet_list:
                #  Grab any aliens that the bullet is colliding with and put it 
                #  into a list.
                hit_list = arcade.check_for_collision_with_list(bullet, self.alien_list)
                
                # if the bullet hits anything, remove it
                if len(hit_list) > 0:
                    bullet.kill()

                for alien in hit_list:
                    alien.kill()

                #  remove off-screen bullets
                if bullet.bottom > self.ai_settings.screen_height:
                    self.bullet_list.remove(bullet)


            self.bullet_list.update()
            self.move_fleet()
            self.aliens_reached_bottom()
            self.alien_list.update()
    
    def aliens_reached_bottom(self):
        """
        If the aliens touch the bottom, the player loses a life and the game
        state is reset.
        """
        for alien in self.alien_list:
            if alien.bottom <= self.ship.top:
                self.ai_settings.ship_lives -= 1
                self.setup()
                break

        if self.ai_settings.ship_lives <= 0:
            self.game_running = False

    def move_fleet(self):
        change_direction = False

        # Find out if an alien has touched either wall
        for an_alien in self.alien_list:
            if (an_alien.right >= self.ai_settings.screen_width or
                an_alien.left <= 0):
                self.change_fleet_direction()
                change_direction = True
                break

        #  if not, don't change their y position
        if not change_direction:
            for alien in self.alien_list:
                alien.change_y = 0

        #  move fleet across the x axis depending if they are moving left/right
        if self.ai_settings.move_fleet_right:
            for alien in self.alien_list:
                alien.change_x = self.ai_settings.alien_speed_factor
        else:
            for alien in self.alien_list:
                alien.change_x = -self.ai_settings.alien_speed_factor

    def change_fleet_direction(self):
        """
        If the fleet is touching a wall, move the fleet down a bit and change
        direction.
        """
        for alien in self.alien_list:
            alien.change_y = -(self.ai_settings.fleet_drop_speed)

        self.ai_settings.move_fleet_right = not self.ai_settings.move_fleet_right


    def on_key_press(self, key, modifiers):
        #  move left and right
        if key == arcade.key.RIGHT:
           self.ship.move_right = True
        if key == arcade.key.LEFT:
            self.ship.move_left = True
        
        #  fire bullets
        if key == arcade.key.SPACE:
            if len(self.bullet_list) < 3:
                bullet = Bullet(self.ai_settings, self.ship)
                self.bullet_list.append(bullet)

        #  quit the game
        if key == arcade.key.ESCAPE:
            arcade.close_window()
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.ship.move_right = False
        if key == arcade.key.LEFT:
            self.ship.move_left = False


    def on_mouse_press(self, x, y, button, modifiers):
        """
        Method for checking for mouse pressing events.
        """
        #  if the game is not currently running and the user clicks in the 
        #  start button area, it will start the game
        if (not self.game_running and x < self.ai_settings.screen_width /2 + 50 
        and x > self.ai_settings.screen_width/2 - 50 and
        y < self.ai_settings.screen_height/2 + 10 and
        y > self.ai_settings.screen_height/2 - 10):
            self.game_running = True


def main():
    print("Prepare for the alien invasion.")
    game = AlienArcade()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()