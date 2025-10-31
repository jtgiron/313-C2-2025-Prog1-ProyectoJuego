import pygame
import os

# Cargar imágenes

ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets')

class Resources:
    def __init__(self):
        self.sprites = {}
        self.sounds = {}

    def load_image(self, key, path):
        full = os.path.join(ASSETS_DIR, path)
        img = pygame.image.load(full).convert_alpha()
        self.sprites[key] = img
        return img
    
    def get(self, key):
        return self.sprites.get(key)
    