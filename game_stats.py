class GameStats:
    """
    Class that holds infomation of the game's current state to be used by the
    scoreboard.
    """

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        
        self.game_running = False
        #TODO: save highscore to a file?
        self.high_score = 0


    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_lives
        self.score = 0
        self.level = 1
