class Settings():
    """ A class that is used to store the settings for the Alien Invasion Game"""
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (17,17,132)

        #ship settings 
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 57,255,20
        self.bullets_allowed = 3