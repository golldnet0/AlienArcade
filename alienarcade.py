import arcade
import settings
"""
Must be ran with sudo on linux.
"""

def main():
    print("Prepare for the alien invasion.")
    ai_settings = settings.Settings()
    arcade.open_window(ai_settings.screen_width, ai_settings.screen_width, 
                       "Alien Arcade")

main()