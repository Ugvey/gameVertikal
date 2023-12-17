import pygame

WIDTH = 600
HIGHT = 800

def background():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('fon/final.jpg').convert(),(600,800))
        self.rect = self.image.get_rect()
        self.muving = 2

    def update(self):
        self.rect.y -= self.muving

    def render(self,window):
        window.blit((0,0))


