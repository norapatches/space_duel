class GameStateManager:
    def __init__(self, game, initialState):
        '''Manages the game states. Needs the game itself, and the initial state'''
        self.game = game
        self.state = initialState
        self.previousState = None
        
        self.running = True
        self.paused = False
        
        self.p1_colour = 'orange'
        self.p2_colour = 'green'
    
    def get_state(self) -> str:
        '''Get current state'''
        return self.state
    
    def get_previous_state(self) -> str:
        '''Get previous state'''
        return self.previousState
    
    def set_state(self, newState):
        '''Set current state to a new one. This inevitably changes the previous state too'''
        self.previousState = self.state
        self.state = newState
    
    def is_running(self):
        return self.running
    
    def pause_level(self):
        self.paused = True
    
    def is_paused(self):
        return self.paused