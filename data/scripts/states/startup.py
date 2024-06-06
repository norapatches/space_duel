from data.scripts.shared.colours import Colours
from data.scripts.shared.settings import GameSettings
from data.scripts.shared.graphics import ApplicationGraphics
import pygame

class Startup:
    def __init__(self, screen, gameStateManager, soundManager):
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.soundManager = soundManager
        
        self.pygame_logo = pygame.image.load_sized_svg(ApplicationGraphics.pygame_logo, GameSettings.screen_size)
    
    def run(self):
        self.screen.fill(Colours.gray)
        self.screen.blit(self.pygame_logo, (0,(GameSettings.screen_height / 2) - (self.pygame_logo.get_height() / 2)))
        pygame.display.update()
        pygame.time.delay(5000)
        self.gameStateManager.set_state('menu')