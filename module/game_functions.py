import sys
import pygame
from random import randint
from module.bullet import Bullet
from module.alien import Alien 
from module.star import Star
def check_events(ai_settings,screen,ship,bullets):
    """This will respond to keyboard and mouse presses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
             
               
def update_screen(ai_settings,screen,ship,aliens,bullets,stars): 
    """This will update the images on the screen """
    screen.fill(ai_settings.bg_color)
    for star in stars.sprites():
        star.blitme()    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #update the frames of the gane
    pygame.display.flip()

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """"will respond and move the ship depending on key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()    

def check_keyup_events(event,ship):
    """"will respond and move the ship depending on key press_up"""
    if event.key == pygame.K_RIGHT:    
        ship.moving_right = False
    if event.key == pygame.K_LEFT:    
        ship.moving_left = False 
def fire_bullets(ai_settings,screen,ship,bullets):
    """Used to fire the bullets when pressing space """  
    if len(bullets) < ai_settings.bullets_allowed:
        #Create a new bullet and add it to the bullets group
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet) 

def update_bullets(aliens,bullets):
    """update the pos of the bullets and remove old bullets"""
    bullets.update()
    #remove the bullets that are off the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)                

def get_number_alien_x(ai_settings,alien_width):
    """Determine num of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * (alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width)) 
    return number_aliens_x

def get_number_of_rows(ai_settings,ship_height,alien_height):
    """Determine the num of rows of aliens that can fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int((available_space_y / (2 * alien_height))/2) 
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + 2 * alien.rect.height * row_number) * 1.4
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """used to create a fleet of aliens"""
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_alien_x(ai_settings,alien.rect.width)
    number_rows = get_number_of_rows(ai_settings, ship.rect.height , alien.rect.height)

    #create the first row of aliens 
    for row_number in range(number_rows): 
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def change_fleet_direction(ai_settings,aliens):            
    """drop the entire fleet and change directions"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,aliens):
    """updates the position of the aliens"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def check_fleet_edges(ai_settings,aliens):    
    """respondes to the aliens reaching the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def create_star(screen,stars,x,y):
    star = Star(screen)
    star.x = 1
    star.rect.x = x
    star.rect.y = y
    stars.add(star)

def create_stars(ai_settings,screen,stars):
  
    number_starts = 500

    for _ in range(number_starts):
        random_x = randint(0,ai_settings.screen_width-1)
        random_y = randint(0,ai_settings.screen_width-1)

        create_star(screen,stars,random_x,random_y)