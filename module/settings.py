class Settings():
    """ A class that is used to store the settings for the Alien Invasion Game"""
    def __init__(self):
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10,15,48)

        #ship settings 
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #bullet settings
        self.bullet_speed_factor = 4
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = 57,255,20
        self.bullets_allowed = 3

        #Alien Settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        #flet_Direction 1 represents right and -1 representings left
        self.fleet_direction = 1