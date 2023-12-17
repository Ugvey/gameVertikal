import pygame

class Enemy:
    def __init__(self,window):
        self.window = window
        self.image = pygame.transform.scale(pygame.image.load('person/enemy/bloop.png').convert_alpha(), (100, 100))
        self.rect = self.image.get_rect(center=(300, 700))
        self.speed = 3
    def update(self):
        self.window.blit(self.image, self.rect)

