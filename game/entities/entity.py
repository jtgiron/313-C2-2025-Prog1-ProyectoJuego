import pygame

class Entity:
    def __init__(self, game, x=0, y=0, w=32, h=32):
        self.game = game
        self.x = float(x)
        self.y = float(y)
        self.w = w
        self.h = h
        self.on_ground = False
        self.alive = True   


    @property
    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.w, self.h)
    
    def update(self, dt):
        pass

    def render(self, surface, camera):
        #dibuja el rectangulo
        r = self.rect.move(-camera.x, -camera.y)
        pygame.draw.rect(surface, (200, 50, 50), r)