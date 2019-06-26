import arcade
import settings


def main():
    print("Prepare for the alien invasion.")
    ai_settings = settings.Settings()
    arcade.open_window(ai_settings.screen_width, ai_settings.screen_width, 
                       "Alien Arcade")

main()