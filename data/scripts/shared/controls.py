import pygame

class ControlsMenu:
    def __init__(self, gameStateManager, soundManager, up, down, ok):
        '''Main Menu control scheme for keyboard'''
        self.up = up
        self.down = down
        self.ok = ok
        
        self.gameStateManager = gameStateManager
        self.soundManager = soundManager
        
        self.choices = ['options', 'quit']
        self.selected = 0
    
    def selection_cycle(self):
        '''Cycle through Main Menu'''
        if self.selected > len(self.choices) - 1:
            self.selected = 0
        if self.selected < 0:
            self.selected = len(self.choices) - 1
    
    def selection_confirm(self):
        '''Confirm selected choice'''
        if self.choices[self.selected]:
            self.gameStateManager.set_state(self.choices[self.selected])
    
    def check_input(self, keys):
        '''Keyboard input for Main Menu. Confirming a choice changes game state.'''
        if keys[self.up]:
            self.soundManager.menu_sfx('select')
            self.selected -= 1
            self.selection_cycle()
        if keys[self.down]:
            self.soundManager.menu_sfx('select')
            self.selected += 1
            self.selection_cycle()
        if keys[self.ok]:
            self.soundManager.menu_sfx('confirm')
            self.selection_confirm()


class ControlsPaused:
    def __init__(self, gameStateManager, soundManager, up, down, ok):
        '''Pause Screen control scheme for keyboard'''
        self.up = up
        self.down = down
        self.ok = ok
        
        self.gameStateManager = gameStateManager
        self.soundManager = soundManager
        
        self.choices = ['level', 'menu']
        self.selected = 0
    
    def selection_cycle(self):
        '''Cycle through Pause Screen'''
        if self.selected > len(self.choices) - 1:
            self.selected = 0
        if self.selected < 0:
            self.selected = len(self.choices) - 1
    
    def selection_confirm(self):
        '''Confirm selected choice'''
        self.gameStateManager.paused = False
        if self.selected == 1:
            self.gameStateManager.game.states['level'].reset()
        self.gameStateManager.set_state(self.choices[self.selected])
        self.reset()
    
    def check_input(self, keys):
        '''Keyboard input in Puase Screen. Confirming to quit changes game state and resets level.'''
        if keys[self.up]:
            self.soundManager.menu_sfx('select')
            self.selected -= 1
            self.selection_cycle()
        if keys[self.down]:
            self.soundManager.menu_sfx('select')
            self.selected += 1
            self.selection_cycle()
        if keys[self.ok]:
            self.soundManager.menu_sfx('confirm')
            self.selection_confirm()
    
    def reset(self):
        '''Reset selected to <resume>'''
        self.selected = 0


class ControlsGameOver:
    def __init__(self, gameStateManager, soundManager, up, down, ok):
        self.up = up
        self.down = down
        self.ok = ok
        
        self.gameStateManager = gameStateManager
        self.soundManager = soundManager
        
        self.choices = ['level', 'menu']
        self.selected = 0
    
    def selection_cycle(self):
        '''Cycle through Game Over screen'''
        if self.selected > len(self.choices) - 1:
            self.selected = 0
        if self.selected < 0:
            self.selected = len(self.choices) - 1
    
    def selection_confirm(self):
        if self.selected == 0:
            self.gameStateManager.set_state('level')
        if self.selected == 1:
            self.gameStateManager.set_state('menu')
    
    def check_input(self, keys):
        if keys[self.up]:
            self.soundManager.menu_sfx('select')
            self.selected -= 1
            self.selection_cycle()
        if keys[self.down]:
            self.soundManager.menu_sfx('select')
            self.selected += 1
            self.selection_cycle()
        if keys[self.ok]:
            self.soundManager.menu_sfx('confirm')
            self.selection_confirm()
    
    def reset(self):
        '''Reset selected to <restart>'''
        self.selected = 0


class ControlsOptions:
    def __init__(self, gameStateManager, soundManager, up, down, left, right, confirm, cancel):
        '''Spaceship selection control scheme for keyboard'''
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        
        self.confirm = confirm
        self.cancel = cancel
        
        self.gameStateManager = gameStateManager
        self.soundManager = soundManager
        
        self.choices = ['p1_ship', 'p2_ship', 'start']
        self.ship_choices = ['orange', 'green', 'yellow', 'blue']
        
        self.updown = True
        self.lefright = False
        
        self.selected = 2
        self.p1_selected = 3
        self.p2_selected = 0
    
    @property
    def p1_colour(self):
        return self.ship_choices[self.p1_selected]
    
    @property
    def p2_colour(self):
        return self.ship_choices[self.p2_selected]
    
    def selection_cycle(self):
        if self.selected > len(self.choices) - 1:
            self.selected = 0
        if self.selected < 0:
            self.selected = len(self.choices) - 1
    
    def ship_selection_cycle(self):
        if self.p1_selected > len(self.ship_choices) - 1:
            self.p1_selected = 0
        if self.p1_selected < 0:
            self.p1_selected = len(self.ship_choices) - 1
        
        if self.p2_selected > len(self.ship_choices) - 1:
            self.p2_selected = 0
        if self.p2_selected < 0:
            self.p2_selected = len(self.ship_choices) - 1
    
    def selection_confirm(self):
        if self.selected != 2:
            self.updown = False
            self.lefright = True
        if self.selected == 2:
            self.gameStateManager.set_state('level')
            self.reset()
    
    def check_input(self, keys):
        if self.updown == True:
            if keys[self.up]:
                self.soundManager.menu_sfx('select')
                self.selected -= 1
                self.selection_cycle()
            if keys[self.down]:
                self.soundManager.menu_sfx('select')
                self.selected += 1
                self.selection_cycle()
            if keys[self.confirm]:
                self.soundManager.menu_sfx('confirm')
                self.selection_confirm()
        elif self.lefright == True:
            if self.selected == 0:
                if keys[self.left]:
                    self.soundManager.menu_sfx('select')
                    self.p1_selected -= 1
                    self.ship_selection_cycle()
                if keys[self.right]:
                    self.soundManager.menu_sfx('select')
                    self.p1_selected += 1
                    self.ship_selection_cycle()
                if keys[self.confirm]:
                    self.soundManager.menu_sfx('confirm')
                    self.lefright = False
                    self.updown = True
                if keys[self.cancel]:
                    self.soundManager.menu_sfx('confirm')
                    self.lefright = False
                    self.updown = True
            if self.selected == 1:
                if keys[self.left]:
                    self.soundManager.menu_sfx('select')
                    self.p2_selected -= 1
                    self.ship_selection_cycle()
                if keys[self.right]:
                    self.soundManager.menu_sfx('select')
                    self.p2_selected += 1
                    self.ship_selection_cycle()
                if keys[self.confirm]:
                    self.soundManager.menu_sfx('confirm')
                    self.lefright = False
                    self.updown = True
                if keys[self.cancel]:
                    self.soundManager.menu_sfx('confirm')
                    self.lefright = False
                    self.updown = True
    
    def set_colours(self):
        self.gameStateManager.p1_colour = self.p1_colour
        self.gameStateManager.p2_colour = self.p2_colour
        self.gameStateManager.game.level.reset()
    
    def reset(self):
        '''Reset selected to <start>'''
        self.selected = 2


class ControlsPlayer:
    def __init__(self, up, down, left, right, laser, rocket):
        '''Spaceship control scheme for keyboard'''
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        
        self.laser = laser
        self.rocket = rocket
    
    def move(self, player, keys):
        '''Move the spaceship in four main directions'''
        if keys[self.up]:
            player.rect.move_ip(0, -player.speed)
        if keys[self.down]:
            player.rect.move_ip(0, player.speed)
        if keys[self.right]:
            player.rect.move_ip(player.speed, 0)
        if keys[self.left]:
            player.rect.move_ip(-player.speed, 0)
    
    def shoot_laser(self, player, keys):
        '''Shoot a laser beam'''
        if keys[self.laser] and player.ready == True:
            player.shoot()
            player.ready = False
            player.shot_time = pygame.time.get_ticks()
    
    def shoot_rocket(self, player, keys):
        '''Shoot a rocket if in posession of any'''
        if keys[self.rocket] and player._rocket_count > 0 and player.rocket_ready == True:
            player.rocket()
            player.rocket_ready = False
            player.rocket_shot_time = pygame.time.get_ticks()
    
    def check_input(self, player, hold, press):
        '''Spaceship movement, laser and rocket launches.'''
        self.move(player, hold)
        self.shoot_laser(player, press)
        self.shoot_rocket(player, press)


class ControllerSupport:
    def __init__(self) -> None:
        pass