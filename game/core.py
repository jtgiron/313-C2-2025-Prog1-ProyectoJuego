import pygame
import sys
import time
from game.settings import *
from game.state_machine import StateMachine


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.dt = 0.0

        self.state = StateMachine(self)
        
        self.running = True

    def run(self):
        prev = time.perf_counter()
        accumulator = 0.0
        step = 1.0 / FPS

        while self.running:
            now = time.perf_counter()
            frame_time = now - prev
            prev = now
            accumulator += frame_time

            #Eventos

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.quit()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    self.quit()
                self.state.handle_event(evento)

            while accumulator >= step:
                self.state.update(step)
                accumulator -= step

        pygame.quit()


def quit(self):
    self.running = False









