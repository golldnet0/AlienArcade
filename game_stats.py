
class GameStats:
    """
    Class that holds infomation of the game's current state to be used by the
    scoreboard.
    """

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        
        self.game_running = False
        self.ship_lives = 3
        #TODO: save highscore to a file?
        self.high_score = 0

        #  attempt to get the high score from a file. otherwise the highscore
        #  will be zero.
        self.filename = "score.dat"
        try:
            with open(self.filename, 'r') as file_object:
                highscore_str = file_object.readline()
        except FileNotFoundError:
            print("No scores saved.")
        else:
            self.high_score = int(highscore_str)

    def reset_stats(self):
        """
        Resets the stats upon starting a new game.
        """
        self.score = 0
        self.level = 1
        self.lives = 3

    def increase_score(self):
        """
        Increases the score after shooting an alien.
        """
        self.score += 100 * self.level

    def update_highscore(self):
        """
        If the current score is higher than the current high score, update it.
        """
        if self.score > self.high_score:
            self.high_score = self.score

    def save_score(self):
        """
        Saves the current high score to a file.
        """
        with open(self.filename, 'w') as file_object:
            file_object.write(str(self.high_score))