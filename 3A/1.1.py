from turtle import Screen
import pygame
import sys
import pygame.locals


pygame.init()


FPS = 30
timer = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
Green = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


Screen = pygame.display.set_mode((300, 300))
Screen.fill(WHITE)
pygame.display.set_caption('CreatShapes')

pygame.draw.line(Screen, BLUE, (150, 130), (130, 170))
pygame.draw.line(Screen, BLUE, (150, 130), (170, 170))
pygame.draw.line(Screen, Green, (130, 170), (170, 170))
pygame.draw.circle(Screen, BLACK, (100, 50), 30)
pygame.draw.circle(Screen, BLACK, (200, 50), 30)
pygame.draw.rect(Screen, RED, (100, 200, 100, 50), 2)

pygame.draw.rect(Screen, BLACK, (110, 260, 80, 5))


while True:

    for event in pygame.event.get():

        if  event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()


    timer.tick(FPS)
    pygame.display.update()