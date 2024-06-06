from data.scripts.shared.graphics import ProjectileGraphics
import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, field, id, colour):
        '''A <colour> laser object for player <id>. Despawns if gets out of playfield.'''
        super().__init__()
        self.id = id
        self.colour = colour
        
        self.field = field
        self.speed = speed * 1.5
        
        self.image = pygame.image.load(ProjectileGraphics.laser[self.colour]).convert_alpha()
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = pos)
    
    def move(self):
        '''Automatic movement in one direction'''
        if self.id == 'p1':
            self.rect.x += self.speed
        elif self.id == 'p2':
            self.rect.x -= self.speed
    
    def despawn(self):
        '''Despawn if leaving playfield bounds'''
        if (self.rect.right >= self.field.right
            or
            self.rect.left <= self.field.left):
            self.kill()
    
    def update(self):
        '''The update method of a laser object'''
        self.move()
        self.despawn()