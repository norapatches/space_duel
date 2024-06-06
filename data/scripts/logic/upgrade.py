from data.scripts.shared.graphics import LevelGraphics

from math import radians, sin, cos
import pygame, random


class Upgrade(pygame.sprite.Sprite):
    def __init__(self, pos, speed, field, id):
        '''A <heart>, <rocket>, <boost> or <shield> upgrade object. Despawns if gets out of playfield.'''
        super().__init__()
        self._id = id
        self.field = field
        self.speed = speed * 0.5
        
        if self.id == 'heart':
            self.image = pygame.image.load(LevelGraphics.heart).convert_alpha()
        if self.id == 'rocket':
            self.image = pygame.image.load(LevelGraphics.rocket).convert_alpha()
        if self.id == 'boost':
            self.image = pygame.image.load(LevelGraphics.boost).convert_alpha()
        if self.id == 'shield':
            self.image = pygame.image.load(LevelGraphics.shield).convert_alpha()
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = pos)
        
        rad = radians(random.randint(0, 360))
        self.delta_x = self.speed * cos(rad)
        self.delta_y = -self.speed * sin(rad)
    
    @property
    def id(self):
        '''Returns <heart>, <rocket>, <boost> or <shield>'''
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
        '''The update method of an upgrade object'''
        self.move()
        self.wiggle()
        self.despawn()