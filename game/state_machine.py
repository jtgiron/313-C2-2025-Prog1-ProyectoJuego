class StateMachine:
    def __init__(self, game):
        self.game = game
    
    def handle_event(self, event):
        
        self.game.level.handle_event(event)

    def update(self, dt):
        self.game.level.update(dt)


    def render(self, surface):
        surface.fill((18, 18, 32))
        self.game.level.render(surface)
        