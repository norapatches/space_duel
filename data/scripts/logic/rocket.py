from data.scripts.shared.graphics import ProjectileGraphics
import pygame


class Rocket(pygame.sprite.Sprite):
    def __init__(self, pos, speed, field, id):
        '''A rocket object for player <id>. Despawns if gets out of playfield.'''
        super().__init__()
        self.id = id
        
        self.field = field
        self.speed = speed * 3
        
        if self.id == 'p1':
            self.image = pygame.image.load(ProjectileGraphics.rocket['->']).convert_alpha()
        elif self.id == 'p2':
            self.image = pygame.image.load(ProjectileGraphics.rocket['<-']).convert_alpha()
        
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
        '''The update method of a rocket object'''
        self.move()
        self.despawn()