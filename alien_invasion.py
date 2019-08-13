import sys
import pygame
from settings import Settings
from ship import Ship
# pylint: disable=no-member

class AlienInvasion:
    """ Main class to manage initialization of the game and its behavior """

    def __init__(self):
        """ Initialize the game, and create the assets """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Must be placed after screen initialization as it requires the screen attribute.
        self.ship = Ship(self)

        # Set background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """ Start the main gameplay loop """
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """ Respond to keydown strokes """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self, event):
        """ Respond to keyup strokes """        
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Redraw screen after each pass of the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.bliteme()
        # Makes most recent drawn display visible
        pygame.display.flip()


if __name__ == "__main__":
    # Realize and instance of the game
    ai = AlienInvasion()
    ai.run_game()
