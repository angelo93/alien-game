import pygame

class Ship:
    """ Initialize ship and its settings """
    
    def __init__(self, ai_game):
        """ Draw the ship in it's starting position """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship and its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Place every new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Convert integer to float for speed value
        self.x = float(self.rect.x)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def bliteme(self):
        """ Draw ship at its current location """
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """ Update the ship's position based on set flags """
        # Update the x value not the rect(its draw position)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect from self.x
        self.rect.x = self.x