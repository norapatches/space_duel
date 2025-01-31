import pygame, random

from data.scripts.shared.settings import GameSettings

from data.scripts.shared.graphics import UIGraphics

from data.scripts.logic.spaceship import Spaceship
from data.scripts.logic.blackhole import Blackhole
from data.scripts.logic.asteroid import Asteroid

class Level:
    def __init__(self, screen, gameStateManager, soundManager):
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.soundManager = soundManager
        
        self.paused = gameStateManager.is_paused()
        
        self.bg = pygame.image.load(UIGraphics.ui_bg)
        self.field_bg = pygame.image.load(UIGraphics.field_bg)
        
        self.playfield = pygame.Rect(GameSettings.screen_width / 32,
                                     GameSettings.screen_height / 6,
                                     GameSettings.field_size[0],
                                     GameSettings.field_size[1])
        
        self.player_one_sprite = Spaceship(self.soundManager,
                                           (self.playfield.midleft[0] + 100, self.playfield.midleft[1]),
                                           'p1', self.gameStateManager.p1_colour,
                                           self.playfield,
                                           GameSettings.player_speed)
        self.player_two_sprite = Spaceship(self.soundManager,
                                           (self.playfield.midright[0] - 100, self.playfield.midright[1]),
                                           'p2', self.gameStateManager.p2_colour,
                                           self.playfield,
                                           GameSettings.player_speed)
        
        self.blackhole_sprite = Blackhole((self.playfield.midleft[0] + self.playfield.width / 2,
                                           self.playfield.midtop[1] + self.playfield.height / 2),
                                           self.playfield,
                                           GameSettings.blackhole_speed)
        
        self.player_one = pygame.sprite.GroupSingle(self.player_one_sprite)
        self.player_two = pygame.sprite.GroupSingle(self.player_two_sprite)
        self.blackhole = pygame.sprite.GroupSingle(self.blackhole_sprite)
        
        # DISPLAY PLAYER'S STATS ON TOP
        self.life_full = pygame.image.load(UIGraphics.heart_full).convert_alpha()
        self.life_empty = pygame.image.load(UIGraphics.heart_empty).convert_alpha()
        self.rockets_full = pygame.image.load(UIGraphics.rocket).convert_alpha()
        
        self.p1score_bar = {
            'base' : pygame.image.load(UIGraphics.p1_score_base).convert_alpha(),
            'top' : pygame.image.load(UIGraphics.p1_score_top).convert_alpha()
        }
        self.p2score_bar = {
            'base' : pygame.image.load(UIGraphics.p2_score_base).convert_alpha(),
            'top' : pygame.image.load(UIGraphics.p2_score_top).convert_alpha()
        }
        
        # player 1
        self.lives_display_p1_pos_x = self.playfield.topleft[0] + 10
        self.lives_display_p1_pos_y = self.playfield.topleft[1] - self.life_full.get_height() * 1.75
        
        self.rockets_display_p1_pos_x = self.playfield.midtop[0] - self.rockets_full.get_width() * 8
        self.rockets_display_p1_pos_y = self.playfield.topleft[1] - self.rockets_full.get_height() * 1.4
        
        self.score_display_p1_pos_x = self.playfield.bottomleft[0] - self.p1score_bar['base'].get_width() - 8
        self.score_display_p1_pos_y = self.playfield.bottomleft[1] - self.p1score_bar['base'].get_height() + 10
        # player 2
        self.lives_display_p2pos_x = self.playfield.topright[0] - (5 * self.life_full.get_width() * 1.75) + 10
        self.lives_display_p2pos_y = self.playfield.topright[1] - self.life_full.get_height() * 1.75
        
        self.rockets_display_p2_pos_x = self.playfield.midtop[0] + self.rockets_full.get_width() * 7
        self.rockets_display_p2_pos_y = self.playfield.topright[1] - self.rockets_full.get_height() * 1.4
        
        self.score_display_p2_pos_x = self.playfield.bottomright[0] + 8
        self.score_display_p2_pos_y = self.playfield.bottomright[1] - self.p1score_bar['base'].get_height() + 10
    
    # RESET GAME
    def reset(self):
        self.paused = self.gameStateManager.is_paused()
        
        player_one_sprite = Spaceship(self.soundManager,
                                      (self.playfield.midleft[0] + 100, self.playfield.midleft[1]),
                                      'p1', self.gameStateManager.p1_colour,
                                      self.playfield,
                                      GameSettings.player_speed)
        player_two_sprite = Spaceship(self.soundManager,
                                      (self.playfield.midright[0] - 100, self.playfield.midright[1]),
                                      'p2', self.gameStateManager.p2_colour,
                                      self.playfield,
                                      GameSettings.player_speed)
        
        blackhole_sprite = Blackhole((self.playfield.midleft[0] + self.playfield.width / 2,
                                      self.playfield.midtop[1] + self.playfield.height / 2),
                                      self.playfield,
                                      GameSettings.blackhole_speed)
        
        self.player_one = pygame.sprite.GroupSingle(player_one_sprite)
        self.player_two = pygame.sprite.GroupSingle(player_two_sprite)
        self.blackhole = pygame.sprite.GroupSingle(blackhole_sprite)
        
        # player 1
        self.lives_display_p1_pos_x = self.playfield.topleft[0] + 10
        self.lives_display_p1_pos_y = self.playfield.topleft[1] - self.life_full.get_height() * 1.75
        
        self.rockets_display_p1_pos_x = self.playfield.midtop[0] - self.rockets_full.get_width() * 8
        self.rockets_display_p1_pos_y = self.playfield.topleft[1] - self.rockets_full.get_height() * 1.4
        
        self.score_display_p1_pos_x = self.playfield.bottomleft[0] - self.p1score_bar['base'].get_width() - 8
        self.score_display_p1_pos_y = self.playfield.bottomleft[1] - self.p1score_bar['base'].get_height() + 10
        # player 2
        self.lives_display_p2pos_x = self.playfield.topright[0] - (5 * self.life_full.get_width() * 1.75) + 10
        self.lives_display_p2pos_y = self.playfield.topright[1] - self.life_full.get_height() * 1.75
        
        self.rockets_display_p2_pos_x = self.playfield.midtop[0] + self.rockets_full.get_width() * 7
        self.rockets_display_p2_pos_y = self.playfield.topright[1] - self.rockets_full.get_height() * 1.4
        
        self.score_display_p2_pos_x = self.playfield.bottomright[0] + 8
        self.score_display_p2_pos_y = self.playfield.bottomright[1] - self.p1score_bar['base'].get_height() + 10
    
    def player1_projectiles_collision(self):
        # PLAYER 1 LASERS
        if self.player_one.sprite.lasers:
            for laser in self.player_one.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.player_two, False, pygame.sprite.collide_mask):                  # hit P2
                    laser.kill()
                    self.player_two.sprite.take_hit(1)
                    if self.player_two.sprite.lives <= 0:
                        self.reset()
                        self.blackhole.sprite.reset()
                        self.gameStateManager.set_state('gameover')
                if pygame.sprite.spritecollide(laser, self.blackhole.sprite.asteroids, False, pygame.sprite.collide_mask):  # hit asteroid
                    laser.kill()
        
        # PLAYER 1 ROCKETS
        if self.player_one.sprite.rockets:
            for rocket in self.player_one.sprite.rockets:
                if pygame.sprite.spritecollide(rocket, self.player_two, False, pygame.sprite.collide_mask):                 # hit P2
                    rocket.kill()
                    self.player_two.sprite.take_hit(2)
                    if self.player_two.sprite.lives <= 0:
                        self.reset()
                        self.blackhole.sprite.reset()
                        self.gameStateManager.set_state('gameover')
                if pygame.sprite.spritecollide(rocket, self.blackhole.sprite.asteroids, False, pygame.sprite.collide_mask): # hit asteroid
                    rocket.kill()
                    self.player_one.sprite.add_score()
                    for collided in pygame.sprite.spritecollide(rocket, self.blackhole.sprite.asteroids, False, pygame.sprite.collide_mask):
                        if collided.id == 'large':
                            self.soundManager.explosion('big')
                            # SPAWN 2-4 small asteroids
                            collided.kill()
                            new = random.randint(2, 4)
                            for _ in range(new):
                                self.blackhole.sprite.asteroids.add(Asteroid(collided.rect.center, GameSettings.blackhole_speed, self.playfield, 'small'))
                        else:
                            self.soundManager.explosion('small')
                            collided.kill()
    
    def player2_projectiles_collision(self):
        # PLAYER 2 LASERS
        if self.player_two.sprite.lasers:
            for laser in self.player_two.sprite.lasers:
                if pygame.sprite.spritecollide(laser, self.player_one, False, pygame.sprite.collide_mask):                  # hit P1
                    laser.kill()
                    self.player_one.sprite.take_hit(1)
                    if self.player_one.sprite.lives <= 0:
                        self.reset()
                        self.blackhole.sprite.reset()
                        self.gameStateManager.set_state('gameover')
                if pygame.sprite.spritecollide(laser, self.blackhole.sprite.asteroids, False, pygame.sprite.collide_mask):  # hit asteroid
                    laser.kill()
        
        # PLAYER 2 ROCKETS
        if self.player_two.sprite.rockets:
            for rocket in self.player_two.sprite.rockets:
                if pygame.sprite.spritecollide(rocket, self.player_one, False,pygame.sprite.collide_mask):                  # hit P1
                    rocket.kill()
                    self.player_one.sprite.take_hit(2)
                    if self.player_one.sprite.lives <= 0:
                        self.reset()
                        self.blackhole.sprite.reset()
                        self.gameStateManager.set_state('gameover')
                if pygame.sprite.spritecollide(rocket, self.blackhole.sprite.asteroids, False, pygame.sprite.collide_mask): # hit asteroid
                    rocket.kill()
                    self.player_two.sprite.add_score()
                    for collided in pygame.sprite.spritecollide(rocket, self.blackhole.sprite.asteroids, False, pygame.sprite.collide_mask):
                        if collided.id == 'large':
                            # SPAWN 2-4 small asteroids
                            collided.kill()
                            new = random.randint(2, 4)
                            for _ in range(new):
                                self.blackhole.sprite.asteroids.add(Asteroid(collided.rect.center, GameSettings.blackhole_speed, self.playfield, 'small'))
                        else:
                            collided.kill()
    
    def upgrades_collision(self):
        # UPGRADES
        if self.blackhole.sprite.items:
            for item in self.blackhole.sprite.items:
                # ROCKET UPGRADE
                if item.id == 'rocket':
                    if pygame.sprite.spritecollide(item, self.player_one, False, pygame.sprite.collide_mask):               # P1 pickup
                        self.player_one.sprite.pickup_rocket()
                        item.kill()
                    if pygame.sprite.spritecollide(item, self.player_two, False, pygame.sprite.collide_mask):               # P2 pickup
                        self.player_two.sprite.pickup_rocket()
                        item.kill()
                # HEART REFILL
                if item.id == 'heart':
                    if pygame.sprite.spritecollide(item, self.player_one, False, pygame.sprite.collide_mask):               # P1 pickup
                        if self.player_one.sprite.lives < 5:
                            self.player_one.sprite.pickup_heart()
                        item.kill()
                    if pygame.sprite.spritecollide(item, self.player_two, False, pygame.sprite.collide_mask):               # P2 pickup
                        if self.player_two.sprite.lives < 5:
                            self.player_two.sprite.pickup_heart()
                        item.kill()
                # SPEED BOOST
                if item.id == 'boost':
                    if pygame.sprite.spritecollide(item, self.player_one, False, pygame.sprite.collide_mask):               # P1 pickup
                        self.player_one.sprite.pickup_boost()
                        item.kill()
                    if pygame.sprite.spritecollide(item, self.player_two, False, pygame.sprite.collide_mask):               # P2 pickup
                        self.player_two.sprite.pickup_boost()
                        item.kill()
                # SHIELD
                if item.id == 'shield':
                    if pygame.sprite.spritecollide(item, self.player_one, False, pygame.sprite.collide_mask):               # P1 pickup
                        self.player_one.sprite.pickup_shield()
                        item.kill()
                    if pygame.sprite.spritecollide(item, self.player_two, False, pygame.sprite.collide_mask):               # P2 pickup
                        self.player_two.sprite.pickup_shield()
                        item.kill()
    
    def asteroids_collision(self):
        if self.blackhole.sprite.asteroids:
            for asteroid in self.blackhole.sprite.asteroids:
                if asteroid.id == 'small':
                    if pygame.sprite.spritecollide(asteroid, self.player_one, False, pygame.sprite.collide_mask):
                        self.player_one.sprite.take_hit(1)
                        if self.player_one.sprite.lives <= 0:
                            self.reset()
                            self.blackhole.sprite.reset()
                            self.gameStateManager.set_state('gameover')
                        asteroid.kill()
                    if pygame.sprite.spritecollide(asteroid, self.player_two, False, pygame.sprite.collide_mask):
                        self.player_two.sprite.take_hit(1)
                        if self.player_two.sprite.lives <= 0:
                            self.reset()
                            self.blackhole.sprite.reset()
                            self.gameStateManager.set_state('gameover')
                        asteroid.kill()
                if asteroid.id == 'large':
                    if pygame.sprite.spritecollide(asteroid, self.player_one, False, pygame.sprite.collide_mask):
                        self.player_one.sprite.take_hit(2)
                        if self.player_one.sprite.lives <= 0:
                            self.reset()
                            self.blackhole.sprite.reset()
                            self.gameStateManager.set_state('gameover')
                        asteroid.kill()
                    if pygame.sprite.spritecollide(asteroid, self.player_two, False, pygame.sprite.collide_mask):
                        self.player_two.sprite.take_hit(2)
                        if self.player_two.sprite.lives <= 0:
                            self.reset()
                            self.blackhole.sprite.reset()
                            self.gameStateManager.set_state('gameover')
                        asteroid.kill()
    
    def gravity_area_collision(self):
            if pygame.sprite.spritecollide(self.blackhole.sprite, self.player_one, False, pygame.sprite.collide_rect_ratio(0.5)):
                x = random.randint(self.playfield.left, int(self.playfield.width / 2 - (1.25 * 166)))
                y = random.randint(self.playfield.top, self.playfield.height)
                coord = x,y
                self.player_one.sprite.rect = self.player_one.sprite.rect.move_to(center=coord)
            
            if pygame.sprite.spritecollide(self.blackhole.sprite, self.player_two, False, pygame.sprite.collide_rect_ratio(0.5)):
                x = random.randint(int(self.playfield.width / 2 + (1.25 * 166)), self.playfield.right)
                y = random.randint(self.playfield.top, self.playfield.height)
                coord = x,y
                self.player_two.sprite.rect = self.player_two.sprite.rect.move_to(center=coord)
    
    # ALL COLLISIONS DETECTION
    def collision_checks(self):
        self.gravity_area_collision()
        self.player1_projectiles_collision()
        self.player2_projectiles_collision()
        self.upgrades_collision()
        self.asteroids_collision()
    
    # PLAYER 1 STATS
    def display_stats_p1(self):
        # DISPLAY HEALTH
        for i in range(5):
            x = self.lives_display_p1_pos_x + (i * self.life_full.get_width() * 1.75)
            if i < self.lives[0]:
                self.screen.blit(self.life_full, (x,self.lives_display_p1_pos_y))
            else:
                self.screen.blit(self.life_empty, (x,self.lives_display_p1_pos_y))  
        # DISPLAY ROCKETS
        for rocket in range(self.rockets[0]):
            x =  self.rockets_display_p1_pos_x - (rocket * self.rockets_full.get_width() * 1.75)
            self.screen.blit(self.rockets_full, (x,self.rockets_display_p1_pos_y))
        # DISPLAY LEVEL UP PROGRESS
        for score in range(self.player_one.sprite.score):
            if score == 0:
                self.screen.blit(self.p1score_bar['base'], (self.score_display_p1_pos_x, self.score_display_p1_pos_y))
            elif score > 0:
                y = self.score_display_p1_pos_y - (score * (self.p1score_bar['top'].get_height() - 5))
                self.screen.blit(self.p1score_bar['top'], (self.score_display_p1_pos_x, y))
    
    # PLAYER 2 STATS
    def display_stats_p2(self):
        # DISPLAY HEALTH
        for i in range(5):
            x = self.lives_display_p2pos_x + (i * self.life_full.get_width() * 1.75)
            if i < self.lives[1]:
                self.screen.blit(self.life_full, (x,self.lives_display_p2pos_y))
            else:
                self.screen.blit(self.life_empty, (x,self.lives_display_p2pos_y))
        # DISPLAY ROCKETS
        for rocket in range(self.rockets[1]):
            x =  self.rockets_display_p2_pos_x + (rocket * self.rockets_full.get_width() * 1.75)
            self.screen.blit(self.rockets_full, (x,self.rockets_display_p2_pos_y))
        # DISPLAY LEVEL UP PROGRESS
        for score in range(self.player_two.sprite.score):
            if score == 0:
                self.screen.blit(self.p2score_bar['base'], (self.score_display_p2_pos_x, self.score_display_p2_pos_y))
            elif score > 0:
                y = self.score_display_p2_pos_y - (score * (self.p2score_bar['top'].get_height() - 5))
                self.screen.blit(self.p2score_bar['top'], (self.score_display_p2_pos_x, y))

    # GAME ROUND
    def run(self):
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_ESCAPE]:
            self.gameStateManager.paused = True
            self.soundManager.set_bgm_volume(0.3)
            self.gameStateManager.set_state('pause')
            
        
        if self.paused == False:
            self.soundManager.set_bgm_volume(1)
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.field_bg, (GameSettings.screen_width / 32, GameSettings.screen_height / 6))
            
            self.lives = [self.player_one.sprite.lives, self.player_two.sprite.lives]
            self.rockets = [self.player_one.sprite.rocket_count, self.player_two.sprite.rocket_count]
            
            self.display_stats_p1()
            self.display_stats_p2()
            
            self.player_one.update()
            self.player_two.update()
            self.blackhole.update()
            self.blackhole.draw(self.screen)
            
            self.player_one.sprite.lasers.draw(self.screen)
            self.player_two.sprite.lasers.draw(self.screen)
            
            self.player_one.sprite.rockets.draw(self.screen)
            self.player_two.sprite.rockets.draw(self.screen)
            
            self.blackhole.sprite.asteroids.draw(self.screen)
            self.blackhole.sprite.items.draw(self.screen)
            
            self.collision_checks()
            
            self.player_one.draw(self.screen)
            self.player_two.draw(self.screen)
