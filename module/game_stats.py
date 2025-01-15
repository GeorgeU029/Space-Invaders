class GameStats():
    """ Track the stats for alien invasion"""
    def __init__(self,ai_settings):
         """initizlize statsitcs"""
         self.ai_settings = ai_settings
         self.reset_stats()

    def reset_stats(self):      
        """Intialize stats that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit