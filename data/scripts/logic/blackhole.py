from data.scripts.shared.graphics import LevelGraphics

from data.scripts.logic.asteroid import Asteroid
from data.scripts.logic.upgrade import Upgrade

import pygame, random

# THE BLACK HOLE CLASS
class Blackhole(pygame.sprite.Sprite):
    def __init__(self, pos, field, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load(LevelGraphics.blackhole).convert_alpha()   # LOAD SPRITE
        self.rect = self.image.get_rect(center=pos)                                 # GET RECTANGLE FROM SPRITE
        self.field = field
        
        self.itemset = ['asteroid_small', 'asteroid_large', 'heart', 'rocket', 'boost', 'shield']
        #self.weights = [0, 0, 0.25, 0.25, 0.25, 0.25]
        self.weights = [0.45, 0.20, 0.03, 0.20, 0.06, 0.06]
        self.asteroids = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
        self.ready = True
        self.launch_time = 0                              
        self.cooldown = 800                               # COOLDOWN LOGIC
    
    # COOLDOWN BETWEEN SHOTS
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.launch_time >= self.cooldown:
                self.ready = True
    
    # CHOOSE WHAT TO SPAWN
    def choose(self):
        choice = random.choices(self.itemset, weights=self.weights)
        return choice[0]
    
    # RANDOMLY SPAWN SOMETHING
    def launch(self):
        if self.ready:
            choice = self.choose()
            if choice == 'asteroid_small':
                self.asteroids.add(Asteroid(self.rect.center, self.speed, self.field, 'small'))
                self.ready = False
                self.launch_time = pygame.time.get_ticks()
            if choice == 'asteroid_large':
                self.asteroids.add(Asteroid(self.rect.center, self.speed, self.field, 'large'))
                self.ready = False
                self.launch_time = pygame.time.get_ticks()
            if choice == 'heart':
                self.items.add(Upgrade(self.rect.center, self.speed, self.field, 'heart'))
                self.ready = False
                self.launch_time = pygame.time.get_ticks()
            if choice == 'rocket':
                self.items.add(Upgrade(self.rect.center, self.speed, self.field, 'rocket'))
                self.ready = False
                self.launch_time = pygame.time.get_ticks()
            if choice == 'boost':
                self.items.add(Upgrade(self.rect.center, self.speed, self.field, 'boost'))
                self.ready = False
                self.launch_time = pygame.time.get_ticks()
            if choice == 'shield':
                self.items.add(Upgrade(self.rect.center, self.speed, self.field, 'shield'))
                self.ready = False
                self.launch_time = pygame.time.get_ticks()
    
    def reset(self):
        self.asteroids = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        
    # UPDATE EVERYTHING
    def update(self):
        self.launch()
        self.recharge()
        self.items.update()
        self.asteroids.update()