import  pygame
import background as bg
from gamer import Dragon
from enemy import Enemy

pygame.init()

pygame.display.set_caption('Dragon faer')
window = pygame.display.set_mode((600, 800))
back = pygame.transform.scale(pygame.image.load('fon/final.jpg').convert(),(600,800))
human = Dragon(window)
enemy_bloop = Enemy(window)


while True:

    window.blit(back, (0,0))
    human.update()
    enemy_bloop.update()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()

