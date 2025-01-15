class Settings():
    """ A class that is used to store the settings for the Alien Invasion Game"""
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10,15,48)

        #How the score increased every level
        self.score_scale = 1.5

        #ship settings 
        
        self.ship_limit = 3

        #bullet settings
        
        self.bullet_width = 1500
        self.bullet_height = 15
        self.bullet_color = 57,255,20
        self.bullets_allowed = 3

        #Alien Settings
        self.fleet_drop_speed = 10

        

        #rate of speed of the game
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """"Initialize the seetings that will change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 4
        self.alien_speed_factor = 0.5

        #direction of that the aliens are moving 1 = right, -1 = left
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale      

        self.alien_points = int(self.alien_points * self.score_scale)