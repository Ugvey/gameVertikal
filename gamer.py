import pygame

class Dragon:
    def __init__(self,window):
        self.window = window
        self.image = pygame.transform.scale(pygame.image.load('person/dragon.png').convert_alpha(),(300,200))
        self.rect = self.image.get_rect(center=(300,200))
        self.speed = 1

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d] and self.rect.x < 400:
            self.rect.x += self.speed
        if key[pygame.K_a] and self.rect.x > -50:
            self.rect.x -= self.speed
        if key[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key[pygame.K_s] and self.rect.y < 400:
            self.rect.y += self.speed

        self.window.blit(self.image, self.rect)

