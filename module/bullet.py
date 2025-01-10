import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite):
    """A class thate managet the bullets that will be fired from the ship"""

    def __init__(self,ai_settings,screen,ship):
        """ create the bullet and set its position equal to the ships pos"""
        super(Bullet,self).__init__()
        self.screen = screen

        #Create a bullet rect/hitbox at 0,0 and then move it to the correct pos that it should be at!
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the pos of the bullet as a decimal
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.ship_speed_factor

    def update(self):
        """ Move the bulllet up the screen"""   
        #update The decimal pos of the bullet
        self.y -= self.speed_factor
        #Update the rect pos
        self.rect.y = self.y 
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)     
