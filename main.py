#import os
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from data.scripts.shared.settings import GameSettings
from data.scripts.shared.graphics import ApplicationGraphics

from data.scripts.shared.manager import GameStateManager
from data.scripts.shared.sound import SoundManager

from data.scripts.states.startup import Startup
from data.scripts.states.menu import Menu
from data.scripts.states.options import Options
from data.scripts.states.level import Level
from data.scripts.states.pause import Paused
from data.scripts.states.gameover import GameOver

import pygame, sys


class Game:
    def __init__(self):
        '''Setup for the whole game'''
        pygame.init()
        pygame.display.set_caption('SPACE DUEL')
        
        self.appicon = pygame.image.load(ApplicationGraphics.app_icon)
        pygame.display.set_icon(self.appicon)
        
        self.screen = pygame.display.set_mode(GameSettings.screen_size, pygame.FULLSCREEN|pygame.SCALED)
        self.clock = pygame.time.Clock()
        
        #self.controllers = {}
        
        self.gameStateManager = GameStateManager(self, 'start')
        self.soundManager = SoundManager()
        
        self.start = Startup(self.screen, self.gameStateManager, self.soundManager)
        self.menu = Menu(self.screen, self.gameStateManager, self.soundManager)
        self.options = Options(self.screen, self.gameStateManager, self.soundManager)
        self.level = Level(self.screen, self.gameStateManager, self.soundManager)
        self.pause = Paused(self.screen, self.gameStateManager, self.soundManager)
        self.gameover = GameOver(self.screen, self.gameStateManager, self.soundManager)
        
        self.states = {
            'start' : self.start,
            'menu': self.menu,
            'options': self.options,
            'level': self.level,
            'pause' : self.pause,
            'gameover' : self.gameover
        }
    
    def run(self):
        '''Run the game'''
        while self.gameStateManager.is_running() == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                ''' JoyDevice
                if event.type == pygame.JOYDEVICEADDED:
                    connected = pygame.joystick.Joystick(event.device_index)
                    self.controllers[connected.get_instance_id()] = connected
                    print(f"Controller {connected.get_name()} connected")
                if event.type == pygame.JOYDEVICEREMOVED:
                    if event.instance_id in self.controllers:
                        del self.controllers[event.instance_id]
                    else:
                        print('Error while removing controller')
                '''
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_just_pressed()
                    if keys[pygame.K_TAB]:
                        pygame.display.toggle_fullscreen()
            if self.gameStateManager.get_state() == 'quit':
                pygame.quit()
                sys.exit()
            
            self.states[self.gameStateManager.get_state()].run()
            self.clock.tick(GameSettings.fps)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()