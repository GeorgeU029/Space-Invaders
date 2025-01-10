import sys
import pygame

def check_events(ship):
    """This will respond to keyboard and mouse presses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
               
def update_screen(ai_settings,screen,ship): 
    """This will update the images on the screen """
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #update the frames of the gane
    pygame.display.flip()
def check_keydown_events(event,ai_settings,ship,bullets):
    """"will respond and move the ship depending on key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True   
def check_keyup_events(event,ship):
    """"will respond and move the ship depending on key press_up"""
    if event.key == pygame.K_RIGHT:    
        ship.moving_right = False
    if event.key == pygame.K_LEFT:    
        ship.moving_left = False             
    