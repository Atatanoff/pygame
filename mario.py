import pygame
import sys
from pygame.color import THECOLORS





def go_r():
    window.blit(animation_set_r[i // 12], (100, 20))
    i += 1
    if i == 60:
        i = 0

def go_l():
    window.blit(animation_set_l[i // 12], (100, 20))
    i += 1
    if i == 60:
        i = 0

pygame.init()
window = pygame.display.set_mode((539, 476))

animation_set_r = [pygame.image.load(f"img\\r{i}.png") for i in range(1, 6)]
animation_set_l = [pygame.image.load(f"img\\l{i}.png") for i in range(1, 6)]
player = pygame.image.load('img\\0.png').convert()
background = pygame.image.load('img\\map.png').convert()

window.blit(background, (0, 0))
window.blit(player,(269,340))



clock = pygame.time.Clock()
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            pygame.quit()
            sys.exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:
        player.    
        print('Лево')
    elif pressed_keys[pygame.K_RIGHT]:
        print('право')
    else:
        print("ghzvj")
        
           
    

    pygame.display.flip()
    clock.tick(60)