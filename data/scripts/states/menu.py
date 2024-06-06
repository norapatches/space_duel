from data.scripts.shared.colours import Colours
from data.scripts.shared.controls import ControlsMenu
from data.scripts.shared.graphics import MenuGraphics
import pygame

class Menu:
    def __init__(self, screen, gameStateManager, soundManager):
        '''Main Menu'''
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.soundManager = soundManager
        self.controls = ControlsMenu(self.gameStateManager,
                                     self.soundManager,
                                     pygame.K_UP, pygame.K_DOWN, pygame.K_RETURN)
        
        self.bg = pygame.image.load(MenuGraphics.background)
        self.logo = pygame.image.load(MenuGraphics.game_logo).convert_alpha()
        
        self.start_button = pygame.image.load(MenuGraphics.buttons['start']).convert_alpha()
        self.quit_button = pygame.image.load(MenuGraphics.buttons['quit']).convert_alpha()
        
        self.start_button_rect = pygame.Rect(self.screen.get_width() / 2 - self.start_button.get_width() / 2,
                                             self.screen.get_height() / 2 + 2 * self.start_button.get_height(),
                                             self.start_button.get_width(), self.start_button.get_height())
        self.quit_button_rect = pygame.Rect(self.screen.get_width() / 2 - self.quit_button.get_width() / 2,
                                             self.start_button_rect.centery + 1.5 * self.quit_button.get_height(),
                                             self.quit_button.get_width(), self.quit_button.get_height())
        
        self.selection_mask = pygame.mask.from_surface(self.start_button)
        
        self.selection_box = [
            (self.selection_mask.to_surface(setcolor=(Colours.purple_m), unsetcolor=(Colours.transparent_m)),
             (self.start_button_rect.left + 15, self.start_button_rect.top + 15)),
            (self.selection_mask.to_surface(setcolor=(Colours.purple_m), unsetcolor=(Colours.transparent_m)),
             (self.quit_button_rect.left + 15, self.quit_button_rect.top + 15))
        ]
    
    def check_input(self):
        '''Check for user input on keyboard'''
        self.controls.check_input(pygame.key.get_just_pressed())
    
    def draw_logo(self):
        '''Draw the game logo'''
        self.screen.blit(self.logo,
                         (self.screen.get_width() / 2 - self.logo.get_width() / 2,
                          self.screen.get_height() / 3 - self.logo.get_height() / 2))
    
    def display_selected(self):
        '''Display a purple parallelogram behind the selected button'''
        self.screen.blit(self.selection_box[self.controls.selected][0], self.selection_box[self.controls.selected][1])
    
    def draw_buttons(self):
        '''Draw the buttons'''
        self.screen.blit(self.start_button, self.start_button_rect)
        self.screen.blit(self.quit_button, self.quit_button_rect)
    
    def run(self):
        '''The Main Menu with two buttons'''
        self.screen.blit(self.bg, (0,0))
        self.check_input()
        self.draw_logo()
        self.display_selected()
        self.draw_buttons()