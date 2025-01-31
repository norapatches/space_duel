# GRAPHIC ASSETS

class SpaceshipGraphics:
    '''Spaceship graphics for the level'''
    level_one = {
        'orange' : {
            'basic' : './data/assets/graphic/spaceship/level_one/orange/basic.png',
            'boost' : './data/assets/graphic/spaceship/level_one/orange/boost.png',
            'shield' : './data/assets/graphic/spaceship/level_one/orange/shield.png',
            'both' : './data/assets/graphic/spaceship/level_one/orange/both.png'},
        'green' : {
            'basic' : './data/assets/graphic/spaceship/level_one/green/basic.png',
            'boost' : './data/assets/graphic/spaceship/level_one/green/boost.png',
            'shield' : './data/assets/graphic/spaceship/level_one/green/shield.png',
            'both' : './data/assets/graphic/spaceship/level_one/green/both.png'},
        'yellow' : {
            'basic' : './data/assets/graphic/spaceship/level_one/yellow/basic.png',
            'boost' : './data/assets/graphic/spaceship/level_one/yellow/boost.png',
            'shield' : './data/assets/graphic/spaceship/level_one/yellow/shield.png',
            'both' : './data/assets/graphic/spaceship/level_one/yellow/both.png'},
        'blue' : {
            'basic' : './data/assets/graphic/spaceship/level_one/blue/basic.png',
            'boost' : './data/assets/graphic/spaceship/level_one/blue/boost.png',
            'shield' : './data/assets/graphic/spaceship/level_one/blue/shield.png',
            'both' : './data/assets/graphic/spaceship/level_one/blue/both.png'
        }
    }
    level_two = {
        'orange' : {
            'basic' : './data/assets/graphic/spaceship/level_two/orange/basic.png',
            'boost' : './data/assets/graphic/spaceship/level_two/orange/boost.png',
            'shield' : './data/assets/graphic/spaceship/level_two/orange/shield.png',
            'both' : './data/assets/graphic/spaceship/level_two/orange/both.png'},
        'green' : {
            'basic' : './data/assets/graphic/spaceship/level_two/green/basic.png',
            'boost' : './data/assets/graphic/spaceship/level_two/green/boost.png',
            'shield' : './data/assets/graphic/spaceship/level_two/green/shield.png',
            'both' : './data/assets/graphic/spaceship/level_two/green/both.png'},
        'yellow' : {
            'basic' : './data/assets/graphic/spaceship/level_two/yellow/basic.png',
            'boost' : './data/assets/graphic/spaceship/level_two/yellow/boost.png',
            'shield' : './data/assets/graphic/spaceship/level_two/yellow/shield.png',
            'both' : './data/assets/graphic/spaceship/level_two/yellow/both.png'},
        'blue' : {
            'basic' : './data/assets/graphic/spaceship/level_two/blue/basic.png',
            'boost' : './data/assets/graphic/spaceship/level_two/blue/boost.png',
            'shield' : './data/assets/graphic/spaceship/level_two/blue/shield.png',
            'both' : './data/assets/graphic/spaceship/level_two/blue/both.png'
        }
    }


class OptionsGraphics:
    '''Spacehsip (large) graphics for colour selection screen'''
    background = './data/assets/graphic/menu/background.png'
    font = './data/assets/fonts/ethnocentric.otf'
    orange = [
        './data/assets/graphic/selection/orange_1.png',
        './data/assets/graphic/selection/orange_2.png'
    ]
    green = [
        './data/assets/graphic/selection/green_1.png',
        './data/assets/graphic/selection/green_2.png'
    ]
    yellow = [
        './data/assets/graphic/selection/yellow_1.png',
        './data/assets/graphic/selection/yellow_2.png'
    ]
    blue = [
        './data/assets/graphic/selection/blue_1.png',
        './data/assets/graphic/selection/blue_2.png'
    ]


class UIGraphics:
    '''User Interface graphic assets for both Level and Menu
            ./data/assets/graphic/user_interface/
            ./data/assets/fonts/'''
    font = './data/assets/fonts/ethnocentric.otf'
    
    p1_score_base = './data/assets/graphic/user_interface/p1_score1.png'
    p1_score_top = './data/assets/graphic/user_interface/p1_score2.png'
    
    p2_score_base = './data/assets/graphic/user_interface/p2_score1.png'
    p2_score_top = './data/assets/graphic/user_interface/p2_score2.png'
    
    ui_bg = './data/assets/graphic/user_interface/ui_background.png'
    field_bg = './data/assets/graphic/user_interface/field_background.png'
    
    heart_full = './data/assets/graphic/user_interface/heart_full.png'
    heart_empty = './data/assets/graphic/user_interface/heart_empty.png'
    rocket = './data/assets/graphic/user_interface/rocket.png'


class ProjectileGraphics:
    '''Four coloured laser beams and rocket
            ./data/assets/graphic/projectiles/'''
    laser = {
        'orange' : './data/assets/graphic/projectiles/laser_orange.png',
        'green' : './data/assets/graphic/projectiles/laser_green.png',
        'yellow' : './data/assets/graphic/projectiles/laser_yellow.png',
        'blue' : './data/assets/graphic/projectiles/laser_blue.png'
    }
    rocket = {
        '->' : './data/assets/graphic/projectiles/rocket_right.png',
        '<-' : './data/assets/graphic/projectiles/rocket_left.png'
    }


class LevelGraphics:
    '''Graphic assets for blackhole, asteroids and upgrades
            ./data/assets/graphic/level/'''
    
    blackhole = './data/assets/graphic/level/blackhole.png'
    
    heart = './data/assets/graphic/level/heart_up.png'
    boost = './data/assets/graphic/level/speed_up.png'
    shield = './data/assets/graphic/level/shield_up.png'
    rocket = './data/assets/graphic/level/rocket_up.png'
    
    asteroid_small = './data/assets/graphic/level/asteroid_small.png'
    asteroid_large = './data/assets/graphic/level/asteroid_large.png'


class ApplicationGraphics:
    app_icon = './data/assets/app/app_icon.png'
    pygame_logo = './data/assets/app/pygame_logo.svg'


class MenuGraphics:
    font = './data/assets/fonts/ethnocentric.otf'
    background = './data/assets/graphic/menu/background.png'
    game_logo = './data/assets/graphic/menu/spaceduel_logo.png'
    controls = {
        'player1' : './data/assets/graphic/menu/controls_p1.png',
        'player2' : './data/assets/graphic/menu/controls_p2.png'
    }
    
    buttons = {
        'start' : './data/assets/graphic/menu/start.png',
        'resume' : './data/assets/graphic/menu/resume.png',
        'restart' : './data/assets/graphic/menu/restart.png',
        'player1' : './data/assets/graphic/menu/p1button.png',
        'player2' : './data/assets/graphic/menu/p2button.png',
        'quit' : './data/assets/graphic/menu/quit.png'
    }