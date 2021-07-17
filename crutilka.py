import time

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))


def crutilka(x):
    for i in range(100):
        pygame.draw.rect(screen, (255, 255, 0), (x + 450 * i, 300, 50, 50))
        pygame.draw.rect(screen, (0, 255, 0), (x + 450 * i + 100, 300, 50, 50))
        pygame.draw.rect(screen, (255, 0, 0), (x + 450 * i + 200, 300, 50, 50))
        pygame.draw.rect(screen, (0, 0, 255), (x + 450 * i + 300, 300, 50, 50))

x=0
sec = 1

def timing():
    ls = [i for i in range(10,0)]

while True:

    screen.fill((0,0,0))
    x-=10
    sec+=1

    pygame.draw.polygon(screen, (255, 25, 0), ((100, 0), (200, 0), (150, 300)))
    crutilka(x)
    print(sec)
    if sec>980:
        time.sleep(5)
        break
    pygame.time.delay(int(round(sec*0.02)))
    pygame.display.flip()
