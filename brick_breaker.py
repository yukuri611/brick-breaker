import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Brick Breaker")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.exit()
        
    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(60)