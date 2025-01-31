import pygame


class SoundManager:
    def __init__(self):
        self.bgm = pygame.mixer.Sound('./data/assets/sound/level/bgm.wav')
        
        self.menu = {
            'select' : pygame.mixer.Sound('./data/assets/sound/menu/select.ogg'),
            'confirm' : pygame.mixer.Sound('./data/assets/sound/menu/confirm.ogg'),
            'back' : pygame.mixer.Sound('./data/assets/sound/menu/blip.wav')
        }
        self.projectiles = {
            'laser' : pygame.mixer.Sound('./data/assets/sound/level/sfx/laser.ogg'),
            'rocket' : pygame.mixer.Sound('./data/assets/sound/level/sfx/rocket.wav')
        }
        self.boom = {
            'small' : pygame.mixer.Sound('./data/assets/sound/level/sfx/explodemini.wav'),
            'big' : pygame.mixer.Sound('./data/assets/sound/level/sfx/explode.wav')
        }
        # new sounds
        '''
        heal
        shield
        boost
        damage
        pickup rocket
        gravity-field
        '''
    
    def play_bgm(self):
        self.bgm.play(-1)
    
    def set_bgm_volume(self, value):
        self.bgm.set_volume(value)
    
    def shoot_laser(self):
        self.projectiles['laser'].play()
    
    def shoot_rocket(self):
        self.projectiles['rocket'].play()
    
    def explosion(self, size):
        self.boom[size].play()
    
    def menu_sfx(self, sound):
        self.menu[sound].play()

