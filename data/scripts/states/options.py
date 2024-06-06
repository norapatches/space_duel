from data.scripts.shared.colours import Colours
from data.scripts.shared.controls import ControlsOptions
from data.scripts.shared.graphics import OptionsGraphics
from data.scripts.shared.graphics import MenuGraphics
from data.scripts.shared.graphics import ProjectileGraphics
import pygame


class Options:
    def __init__(self, screen, gameStateManager, soundManager):
        '''Options screen where the players can select a ship colour'''
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.soundManager = soundManager
        self.controls = ControlsOptions(self.gameStateManager, self.soundManager,
                                        pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT,
                                        pygame.K_RETURN, pygame.K_ESCAPE)
        
        self.bg = pygame.image.load(OptionsGraphics.background)
        self.font = pygame.font.Font(OptionsGraphics.font, 48)
        
        self.lasers = {
            'orange' : pygame.image.load(ProjectileGraphics.laser['orange']).convert_alpha(),
            'green' : pygame.image.load(ProjectileGraphics.laser['green']).convert_alpha(),
            'yellow' : pygame.image.load(ProjectileGraphics.laser['yellow']).convert_alpha(),
            'blue' : pygame.image.load(ProjectileGraphics.laser['blue']).convert_alpha()
        }
        self.rockets = {
            '<-' : pygame.image.load(ProjectileGraphics.rocket['<-']).convert_alpha(),
            '->' : pygame.image.load(ProjectileGraphics.rocket['->']).convert_alpha()
        }
        
        self.p1_button = pygame.image.load(MenuGraphics.buttons['player1']).convert_alpha()
        self.p2_button = pygame.image.load(MenuGraphics.buttons['player2']).convert_alpha()
        self.start_button = pygame.image.load(MenuGraphics.buttons['start']).convert_alpha()
        
        self.p1_button_rect = pygame.Rect(self.screen.get_width() / 2 - self.p1_button.get_width() / 2,
                                          self.screen.get_height() / 2 + 5,
                                          self.p1_button.get_width(), self.p1_button.get_height())
        self.p2_button_rect = pygame.Rect(self.screen.get_width() / 2 - self.p2_button.get_width() / 2,
                                          self.screen.get_height() / 2 + 2 * self.p2_button.get_height() + 5,
                                          self.p2_button.get_width(), self.p2_button.get_height())
        self.start_button_rect = pygame.Rect(self.screen.get_width() / 2 - self.start_button.get_width() / 2,
                                             self.screen.get_height() / 2 + 4 * self.start_button.get_height() + 5,
                                             self.start_button.get_width(), self.start_button.get_height())
        
        self.selection_mask = pygame.mask.from_surface(self.p1_button)
        self.selection_box = [
            (self.selection_mask.to_surface(setcolor=(Colours.purple_m), unsetcolor=(Colours.transparent_m)),
             (self.p1_button_rect.left+ 15, self.p1_button_rect.top + 15)),
            (self.selection_mask.to_surface(setcolor=(Colours.purple_m), unsetcolor=(Colours.transparent_m)),
             (self.p2_button_rect.left + 15, self.p2_button_rect.top + 15)),
            (self.selection_mask.to_surface(setcolor=(Colours.purple_m), unsetcolor=(Colours.transparent_m)),
             (self.start_button_rect.left + 15, self.start_button_rect.top + 15))
        ]
        
        
        self.user_controls = {
            'player_one' : pygame.image.load(MenuGraphics.controls['player1']).convert_alpha(),
            'player_two' : pygame.image.load(MenuGraphics.controls['player2']).convert_alpha()
        }
        
        self.orange = [
            pygame.image.load(OptionsGraphics.orange[0]).convert_alpha(),
            pygame.image.load(OptionsGraphics.orange[1]).convert_alpha()
        ]
        self.green = [
            pygame.image.load(OptionsGraphics.green[0]).convert_alpha(),
            pygame.image.load(OptionsGraphics.green[1]).convert_alpha()
        ]
        self.yellow = [
            pygame.image.load(OptionsGraphics.yellow[0]).convert_alpha(),
            pygame.image.load(OptionsGraphics.yellow[1]).convert_alpha()
        ]
        self.blue = [
            pygame.image.load(OptionsGraphics.blue[0]).convert_alpha(),
            pygame.image.load(OptionsGraphics.blue[1]).convert_alpha()
        ]
        
        self.ships = [self.orange, self.green, self.yellow, self.blue]
    
    def check_input(self):
        '''Check for user input on keyboard'''
        self.controls.check_input(pygame.key.get_just_pressed())
    
    def display_selected(self):
        '''Display a purple parallelogram behind the selected button'''
        self.screen.blit(self.selection_box[self.controls.selected][0], self.selection_box[self.controls.selected][1])
    
    def draw_buttons(self):
        '''Draw the buttons'''
        self.screen.blit(self.p1_button, self.p1_button_rect)
        self.screen.blit(self.p2_button, self.p2_button_rect)
        self.screen.blit(self.start_button, self.start_button_rect)
    
    def draw_p1_controls(self):
        '''Display player one control scheme'''
        text = self.font.render('P1 controls', True, Colours.white)
        text_rect = pygame.Rect(self.screen.get_width() / 4 - text.get_width() / 2,
                                90,
                                text.get_width(), text.get_height())
        self.screen.blit(text, text_rect)
        img_rect = pygame.Rect(self.screen.get_width() / 4 - self.user_controls['player_one'].get_width() / 2,
                                250,
                                self.user_controls['player_one'].get_width(), self.user_controls['player_one'].get_height())
        self.screen.blit(self.user_controls['player_one'], img_rect)
        laser = self.lasers[self.gameStateManager.p1_colour]
        self.screen.blit(laser, (img_rect.centerx + 160, img_rect.centery - 25))
        rocket = self.rockets['->']
        self.screen.blit(rocket, (img_rect.centerx + 260, img_rect.centery - 25))
    
    def draw_p2_controls(self):
        '''Display player two control scheme'''
        text = self.font.render('P2 controls', True, Colours.white)
        text_rect = pygame.Rect((self.screen.get_width() / 4 * 3) - text.get_width() / 2,
                                90,
                                text.get_width(), text.get_height())
        self.screen.blit(text, text_rect)
        img_rect = pygame.Rect((self.screen.get_width() / 4 * 3) - self.user_controls['player_two'].get_width() / 2,
                                250,
                                self.user_controls['player_two'].get_width(), self.user_controls['player_two'].get_height())
        self.screen.blit(self.user_controls['player_two'], img_rect)
        laser = self.lasers[self.gameStateManager.p2_colour]
        self.screen.blit(laser, (img_rect.centerx + 160, img_rect.centery - 25))
        rocket = self.rockets['<-']
        self.screen.blit(rocket, (img_rect.centerx + 260, img_rect.centery - 25))
    
    def p1_ship_box(self):
        '''Display player one ship colour'''
        ship = self.ships[self.controls.p1_selected][0]
        rotated = pygame.transform.rotate(ship, -90)
        if self.controls.lefright == True and self.controls.selected == 0:
            self.screen.blit(rotated,
                        (self.screen.get_width() / 6 - self.ships[self.controls.p1_selected][0].get_width() / 2,
                         self.screen.get_height() / 2))
        else:
            self.screen.blit(ship,
                        (self.screen.get_width() / 6 - self.ships[self.controls.p1_selected][0].get_width() / 2,
                         self.screen.get_height() / 2))
    
    def p2_ship_box(self):
        '''Display player two ship colour'''
        ship = self.ships[self.controls.p2_selected][0]
        rotated = pygame.transform.rotate(ship, 90)
        if self.controls.lefright == True and self.controls.selected == 1:
            self.screen.blit(rotated,
                            ((self.screen.get_width() / 6 * 5 - self.ships[self.controls.p2_selected][0].get_width() / 2),
                                self.screen.get_height() / 2))
        else:
            self.screen.blit(ship,
                        ((self.screen.get_width() / 6 * 5 - self.ships[self.controls.p2_selected][0].get_width() / 2),
                            self.screen.get_height() / 2))
    
    def run(self):
        self.screen.blit(self.bg, (0,0))
        self.check_input()
        self.draw_p1_controls()
        self.draw_p2_controls()
        self.p1_ship_box()
        self.p2_ship_box()
        self.display_selected()
        self.draw_buttons()
        self.controls.set_colours()