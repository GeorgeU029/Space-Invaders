import pygame.font

class Scoreboard():
    """A class for displaying information to the player"""
    def __init__(self,ai_settings,screen,stats):
        """Initilize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #Font settings for scoring information
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #Prepate the initial score image.
        self.prep_score()
    def prep_score(self):        
        """Turn the score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 200
        self.score_rect.top = 200
    
    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image,self.score_rect)       
