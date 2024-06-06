from data.scripts.shared.graphics import LevelGraphics

from math import radians, sin, cos
import pygame, random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos, speed, field, id):
        '''A <small> or <large> asteroid object. Despawns if gets out of playfield.'''
        super().__init__()
        self._id = id
        self.field = field
        
        if self._id == 'small':
            self.image = pygame.image.load(LevelGraphics.asteroid_small).convert_alpha()
            self.speed = speed
        elif self._id == 'large':
            self.image = pygame.image.load(LevelGraphics.asteroid_large).convert_alpha()
            self.speed = speed * 0.25
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = pos)
        
        rad = radians(random.randint(0, 360))
        self.delta_x = self.speed * cos(rad)
        self.delta_y = -self.speed * sin(rad)
    
    @property
    def id(self):
        '''Returns <small> or <large>'''
        return self._id
    
    def move(self):
        '''Automatic movement in one direction'''
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

    def wiggle(self):
        '''Randomly change direction'''
        self.delta_x += random.uniform(-0.3, 0.3)
        self.delta_y += random.uniform(-0.3, 0.3)
    
    def despawn(self):
        '''Despawn if leaving playfield bounds'''
        if (self.rect.right >= self.field.right or
            self.rect.left <= self.field.left or
            self.rect.top <= self.field.top or
            self.rect.bottom >= self.field.bottom):
            self.kill()
    
    def update(self):
        '''The update method of an asteroid object'''
        self.move()
        self.wiggle()
        self.despawn()