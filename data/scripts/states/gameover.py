from data.scripts.shared.colours import Colours
from data.scripts.shared.controls import ControlsGameOver
from data.scripts.shared.graphics import MenuGraphics
import pygame

class GameOver:
    def __init__(self, screen, gameStateManager, soundManager):
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.soundManager = soundManager
        self.controls = ControlsGameOver(self.gameStateManager,
                                         self.soundManager,
                                         pygame.K_UP, pygame.K_DOWN, pygame.K_RETURN)
        self.font = pygame.font.Font(MenuGraphics.font, 100)
        self.box_size = (950, 650)
        
        self.box = pygame.Rect(self.screen.get_width() / 2 - self.box_size[0] / 2,
                               self.screen.get_height() / 2 - self.box_size[1] / 2,
                               self.box_size[0], self.box_size[1])
        
        self.text = self.font.render('GAME OVER', True, Colours.white)
        self.text_rect = pygame.Rect(self.screen.get_width() / 2 - self.text.get_width() / 2,
                                     self.box.midtop[1] + self.text.get_height() / 2,
                                     self.text.get_width(), self.text.get_height())
        
        self.restart_button = pygame.image.load(MenuGraphics.buttons['restart']).convert_alpha()
        self.restart_button_rect = pygame.Rect(self.screen.get_width() / 2 - self.restart_button.get_width() / 2,
                                              self.text_rect.midbottom[1] + self.restart_button.get_height(),
                                              self.restart_button.get_width(), self.restart_button.get_height())
        self.selection_mask = pygame.mask.from_surface(self.restart_button)
        
        self.quit_button = pygame.image.load(MenuGraphics.buttons['quit']).convert_alpha()
        self.quit_button_rect = pygame.Rect(self.screen.get_width() / 2 - self.quit_button.get_width() / 2,
                                              self.restart_button_rect.midbottom[1] + self.quit_button.get_height(),
                                              self.quit_button.get_width(), self.quit_button.get_height())
        
        self.selection_box = [
            (self.selection_mask.to_surface(setcolor=(Colours.purple_m), unsetcolor=(Colours.transparent_m)),
             (self.screen.get_width() / 2 - self.restart_button.get_width() / 2 + 15,
              self.restart_button_rect.midtop[1] + 15)),
            (self.selection_mask.to_surface(setcolor=(Colours.purple_m), unsetcolor=(Colours.transparent_m)),
             (self.screen.get_width() / 2 - self.quit_button.get_width() / 2 + 15,
              self.quit_button_rect.midtop[1] + 15))
        ]
    
    def check_input(self):
        '''Check for user input on keyboard'''
        self.controls.check_input(pygame.key.get_just_pressed())
    
    def draw_box(self):
        '''Draw the gray rectangle with a white border and the text on it'''
        pygame.draw.rect(self.screen, Colours.gray, self.box, 0, 0)
        pygame.draw.rect(self.screen, Colours.white, self.box, 2, 0)
        self.screen.blit(self.text, self.text_rect)
    
    def display_selected(self):
        '''Display a purple parallelogram behind the selected button'''
        self.screen.blit(self.selection_box[self.controls.selected][0], self.selection_box[self.controls.selected][1])
    
    def draw_buttons(self):
        '''Draw the buttons'''
        self.screen.blit(self.restart_button, self.restart_button_rect)
        self.screen.blit(self.quit_button, self.quit_button_rect)
    
    def run(self):
        '''The Game Over screen with two buttons'''
        self.check_input()
        self.draw_box()
        self.display_selected()
        self.draw_buttons()
