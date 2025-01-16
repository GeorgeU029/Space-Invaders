import pygame
from module.settings import Settings
from module.ship import Ship
from module.alien import Alien
from module.star import Star
from module.game_stats import GameStats
from module.button import Button
from module.scoreboard import Scoreboard
import module.game_functions as gf
from pygame.sprite import Group

def run_game():
    #Initialize the game and create the screeen object
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings,screen,"Play")
    #Create an instance to store game stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #creating the ship
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings,screen)
    #creating a container for the bullets
    bullets = Group()
    #creaing the fleet of aliens
    aliens = Group()
    stars = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    gf.create_stars(ai_settings,screen,stars)
    
    #Starts the main loop of the game
    
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,bullets,aliens)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,stars,play_button)
       
        if stats.game_active:
       
            ship.update()
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        
        #set the baclground color of the screen 
        
run_game()                
