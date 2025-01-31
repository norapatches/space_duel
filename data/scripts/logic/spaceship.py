from data.scripts.shared.controls import ControlsPlayer
from data.scripts.shared.graphics import SpaceshipGraphics

from data.scripts.logic.laser import Laser
from data.scripts.logic.rocket import Rocket
import pygame

# SPACESHIP CLASS
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, soundManager, pos, id, colour, field, speed):
        super().__init__()
        self.soundManager = soundManager
        
        self.id = id
        self.field = field
        self.colour = colour
        self.speed = speed
        self._lives = 5
        self._score = 10
        self.levelup = False
        
        self.p1_images = {
            'lv1' : {
                'basic' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_one[self.colour]['basic']).convert_alpha(), -90.0),
                'boost' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_one[self.colour]['boost']).convert_alpha(), -90.0),
                'shield' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_one[self.colour]['shield']).convert_alpha(), -90.0),
                'shield_boost' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_one[self.colour]['both']).convert_alpha(), -90.0)
            },
            'lv2' : {
                'basic' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_two[self.colour]['basic']).convert_alpha(), -90.0),
                'boost' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_two[self.colour]['boost']).convert_alpha(), -90.0),
                'shield' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_two[self.colour]['shield']).convert_alpha(), -90.0),
                'shield_boost' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_two[self.colour]['both']).convert_alpha(), -90.0)
            }
        }
        
        self.p2_images = {
            'lv1' : {
                'basic' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_one[self.colour]['basic']).convert_alpha(), 90.0),
                'boost' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_one[self.colour]['boost']).convert_alpha(), 90.0),
                'shield' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_one[self.colour]['shield']).convert_alpha(), 90.0),
                'shield_boost' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_one[self.colour]['both']).convert_alpha(), 90.0)
            },
            'lv2' : {
                'basic' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_two[self.colour]['basic']).convert_alpha(), 90.0),
                'boost' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_two[self.colour]['boost']).convert_alpha(), 90.0),
                'shield' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_two[self.colour]['shield']).convert_alpha(), 90.0),
                'shield_boost' : pygame.transform.rotate(pygame.image.load(SpaceshipGraphics.level_two[self.colour]['both']).convert_alpha(), 90.0)
            }
        }
        
        if self.id == 'p1':
            self.image = self.p1_images['lv1']['basic']
        elif self.id == 'p2':
            self.image = self.p2_images['lv1']['basic']
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect(center=pos)
        
        self.lasers = pygame.sprite.Group()
        self.rockets = pygame.sprite.Group()
        self._rocket_count = 5
        
        # COOLDOWN LOGIC FOR LASER
        self.ready = True
        self.shot_time = 0
        self.cooldown = 400
        # COOLDOWN LOGIC FOR ROCKET
        self.rocket_ready = True
        self.rocket_shot_time = 0
        self.rocket_cooldown = 800
        # COOLDOWN LOGIC FOR SPEED BOOST
        self.boosted = False
        self.boost_time = 0
        self.boost_cooldown = 5000
        # COOLDOWN LOGIC FOR SHIELD
        self.shielded = False
        self.shield_time = 0
        self.shield_cooldown = 5000
        # FOR DAMAGE AND HEAL ANIMATIONS
        self.hit = False
        self.hit_time = 0
        self.heal = False
        self.heal_time = 0
        self.animation_cooldown = 300
        
        self.p1_controls = ControlsPlayer(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_e, pygame.K_r)
        self.p2_controls = ControlsPlayer(pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l, pygame.K_o, pygame.K_p)
    
    @property
    def rocket_count(self) -> int:
        return self._rocket_count
    
    @property
    def lives(self) -> int:
        return self._lives
    
    @property
    def score(self) -> int:
        return self._score
    
    
    def pickup_rocket(self):        # PICK UP ROCKET (call from outside)
        if self._rocket_count < 5:
            self._rocket_count += 1
    
    def pickup_heart(self):         # PICK UP HEART (call from outside)
        if not self.heal:
            self.heal_time = pygame.time.get_ticks()
            self.heal = True
            if self._lives < 5:
                self._lives += 1
    
    def pickup_boost(self):         # PICK UP BOOST (call from outside)
        if not self.boosted:
            self.speed *= 2
            self.boost_time = pygame.time.get_ticks()
            self.boosted = True
    
    def pickup_shield(self):        # PICK UP SHIELD (call from outside)
        if self.shielded == False:
            self.shield_time = pygame.time.get_ticks()
            self.shielded = True
    
    def take_hit(self, hit):        # TAKE DAMAGE (call from outside)
        if self.shielded == False:
            self.hit_time = pygame.time.get_ticks()
            self.hit = True
            self._lives -= hit
        if self.shielded == True:
            self.shielded = False
    
    
    def gravity_field(self):
        if self.id == 'p1':
            if (self.rect.centerx >= self.field.centerx - (1.25 * 166) and
                self.rect.centerx < self.field.centerx
                and
                self.rect.centery >= self.field.centery - (1.25 * 166) and
                self.rect.centery < self.field.centery):
                self.rect.move_ip((self.speed / 4), (self.speed / 4))       # move down-right
            
            if (self.rect.centerx >= self.field.centerx - (1.25 * 166) and
                self.rect.centerx < self.field.centerx
                and
                self.rect.centery == self.field.centery):
                self.rect.move_ip((self.speed / 4), 0)                      # move right
            
            if (self.rect.centerx >= self.field.centerx - (1.25 * 166) and
                self.rect.centerx < self.field.centerx
                and
                self.rect.centery <= self.field.centery + (1.25 * 166) and
                self.rect.centery > self.field.centery):
                self.rect.move_ip((self.speed / 4), -(self.speed / 4))      # move up-right
            
        if self.id == 'p2':
            if (self.rect.centerx <= self.field.centerx + (1.25 * 166) and
                self.rect.centerx > self.field.centerx
                and
                self.rect.centery >= self.field.centery - (1.25 * 166) and
                self.rect.centery < self.field.centery):
                self.rect.move_ip(-(self.speed / 4), (self.speed / 4))      # move down-left
            
            if (self.rect.centerx <= self.field.centerx + (1.25 * 166) and
                self.rect.centerx > self.field.centerx
                and
                self.rect.centery == self.field.centery):
                self.rect.move_ip(-(self.speed / 4), 0)                     # move left
            
            if (self.rect.centerx <= self.field.centerx + (1.25 * 166) and
                self.rect.centerx > self.field.centerx
                and
                self.rect.centery <= self.field.centery + (1.25 * 166) and
                self.rect.centery > self.field.centery):
                self.rect.move_ip(-(self.speed / 4), -(self.speed / 4))     # move up-left
    
    # CHECK FOR FIELD BOUNDS
    def bounds(self):
        if self.id == 'p1':                                                 # PLAYER 1
            if self.rect.left <= self.field.left:
                self.rect.left = self.field.left
            if self.rect.right >= self.field.left + self.field.width / 2:
                self.rect.right = self.field.left + self.field.width / 2
            if self.rect.top <= self.field.top:
                self.rect.top = self.field.top
            if self.rect.bottom >= self.field.bottom:
                self.rect.bottom = self.field.bottom
        
        if self.id == 'p2':                                               # PLAYER 2
            if self.rect.left <= (self.field.right - (self.field.width / 2)):
                self.rect.left = (self.field.right - (self.field.width / 2 ))
            if self.rect.right >= self.field.right:
                self.rect.right = self.field.right
            if self.rect.top <= self.field.top:
                self.rect.top = self.field.top
            if self.rect.bottom >= self.field.bottom:
                self.rect.bottom = self.field.bottom
    
    # SET SCORE UNTIL 10
    def add_score(self):
        if self._score < 10:
            self._score += 1
    
    # LEVEL UP
    def level_up(self):
        if self._score >= 10:
            self.levelup = True
    
    # CONTROLS
    def get_input(self):
        if self.id == 'p1':
            keys = pygame.key.get_pressed()
            fire = pygame.key.get_just_pressed()
            
            self.p1_controls.check_input(self, keys, fire)
        elif self.id == 'p2':
            keys = pygame.key.get_pressed()
            fire = pygame.key.get_just_pressed()
            
            self.p2_controls.check_input(self, keys, fire)
    
    # SHOOT LASER
    def shoot(self):
        self.soundManager.shoot_laser()
        if self.id == 'p1':
            pos_c = (self.rect.center[0] + 20, self.rect.center[1])
            pos_t = (self.rect.midtop[0], self.rect.midtop[1] + 20)
            pos_b = (self.rect.midbottom[0], self.rect.midbottom[1] - 9)
        if self.id == 'p2':
            pos_c = (self.rect.center[0] - 20, self.rect.center[1])
            pos_t = (self.rect.midtop[0], self.rect.midtop[1] + 20)
            pos_b = (self.rect.midbottom[0], self.rect.midbottom[1] - 9)
        
        if self.levelup == True:
            self.lasers.add(Laser(pos_t, self.speed, self.field, self.id, self.colour),
                            Laser(pos_b, self.speed, self.field, self.id, self.colour))
        else:
            self.lasers.add(Laser(pos_c, self.speed, self.field, self.id, self.colour))
    
    # SHOOT ROCKET
    def rocket(self):
        self.soundManager.shoot_rocket()
        if self.id == 'p1':
            if self.levelup == True:
                pos_c = (self.rect.center[0] + 20, self.rect.center[1] + 8)
            pos_c = (self.rect.center[0] + 20, self.rect.center[1] + 1)
        if self.id == 'p2':
            if self.levelup == True:
                pos_c = (self.rect.center[0] - 20, self.rect.center[1] + 8)
            pos_c = (self.rect.center[0] - 20, self.rect.center[1] + 1)
        self.rockets.add(Rocket(pos_c, self.speed, self.field, self.id))
        self._rocket_count -= 1
    
    
    def counter_laser(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.shot_time >= self.cooldown:
                self.ready = True
    
    def counter_rocket(self):
        if not self.rocket_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.rocket_shot_time >= self.rocket_cooldown:
                self.rocket_ready = True
    
    def counter_boost(self):
        current_time = pygame.time.get_ticks()
        if self.boosted == True:
            if current_time - self.boost_time >= self.boost_cooldown:
                self.speed /= 2
                self.boosted = False                
    
    def counter_shield(self):
        current_time = pygame.time.get_ticks()
        if self.shielded == True:
            if current_time - self.shield_time >= self.shield_cooldown:
                self.shielded = False
    
    def counter_hit(self):
        current_time = pygame.time.get_ticks()
        if self.hit == True:
            if current_time - self.hit_time >= self.animation_cooldown:
                self.hit = False
    
    def counter_heal(self):
        current_time = pygame.time.get_ticks()
        if self.heal == True:
            if current_time - self.heal_time >= self.animation_cooldown:
                self.heal = False
    
    def all_counters(self):
        self.counter_laser()
        self.counter_rocket()
        self.counter_boost()
        self.counter_shield()
        self.counter_hit()
        self.counter_heal()
    
    
    def animations(self):
        if self.heal == True:
            self.image = self.mask.to_surface(setcolor=(0, 255, 0, 255), unsetcolor=(0, 0, 0, 0))
        if self.hit == True:
            self.image = self.mask.to_surface(setcolor=(255, 0, 0, 255), unsetcolor=(0, 0, 0, 0))
    
    def ship_appearance(self):
        if self.id == 'p1':
            if (self.levelup == True
                and self.shielded == True
                and self.boosted == True):
                self.image = self.p1_images['lv2']['shield_boost']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == True
                and self.shielded == True
                and self.boosted == False):
                self.image = self.p1_images['lv2']['shield']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == True
                and self.shielded == False
                and self.boosted == True):
                self.image = self.p1_images['lv2']['boost']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == True
                and self.shielded == False
                and self.boosted == False):
                self.image = self.p1_images['lv2']['basic']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == False
                and self.shielded == True
                and self.boosted == True):
                self.image = self.p1_images['lv1']['shield_boost']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == False
                and self.shielded == True
                and self.boosted == False):
                self.image = self.p1_images['lv1']['shield']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == False
                and self.shielded == False
                and self.boosted == True):
                self.image = self.p1_images['lv1']['boost']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == False
                and self.shielded == False
                and self.boosted == False):
                self.image = self.p1_images['lv1']['basic']
                self.mask = pygame.mask.from_surface(self.image)
        
        if self.id == 'p2':
            if (self.levelup == True
                and self.shielded == True
                and self.boosted == True):
                self.image = self.p2_images['lv2']['shield_boost']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == True
                and self.shielded == True
                and self.boosted == False):
                self.image = self.p2_images['lv2']['shield']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == True
                and self.shielded == False
                and self.boosted == True):
                self.image = self.p2_images['lv2']['boost']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == True
                and self.shielded == False
                and self.boosted == False):
                self.image = self.p2_images['lv2']['basic']
                self.mask = pygame.mask.from_surface(self.image)
            
            if (self.levelup == False
                and self.shielded == True
                and self.boosted == True):
                self.image = self.p2_images['lv1']['shield_boost']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == False
                and self.shielded == True
                and self.boosted == False):
                self.image = self.p2_images['lv1']['shield']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == False
                and self.shielded == False
                and self.boosted == True):
                self.image = self.p2_images['lv1']['boost']
                self.mask = pygame.mask.from_surface(self.image)
            if (self.levelup == False
                and self.shielded == False
                and self.boosted == False):
                self.image = self.p2_images['lv1']['basic']
                self.mask = pygame.mask.from_surface(self.image)
    
    # UPDATE EVERYTHING
    def update(self):
        self.get_input()
        self.gravity_field()
        self.bounds()
        self.all_counters()
        self.level_up()
        self.lasers.update()
        self.rockets.update()
        self.ship_appearance()
        self.animations()