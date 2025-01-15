import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """ initialize the ship to it's starting pos"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship and make it's hitbox
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the correct pos (center bot)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #used to store the decimal value of the ships cener
        self.center = float(self.rect.centerx)

        #flags for the movement
        self.moving_right = False
        self.moving_left = False



    def update(self):    
        """update the ship's position based on the mov of the flag"""
        if self.moving_right and self.center < self.screen_rect.right - 60:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.center > 60:
            self.center -= self.ai_settings.ship_speed_factor


        self.rect.centerx = self.center    
    
    
    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)