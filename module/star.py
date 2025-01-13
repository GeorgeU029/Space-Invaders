import pygame
from random import Random
from pygame.sprite import Sprite
class Star(Sprite):
    
    def __init__(self,screen):
        """ Initialize the stars to randomly spawn in the background"""
        super(Star,self).__init__()
        self.screen = screen

        #LOAD EACH STAR
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        

    def blitme(self):
        """ Draw the start at the location"""
        self.screen.blit(self.image,self.rect)        


