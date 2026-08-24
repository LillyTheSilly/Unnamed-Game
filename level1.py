import pygame
from pygame.locals import *

pygame.font.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Level 1")


# images
sun_img = pygame.image.load("platformer_assets/img/sun.png")
bg_img = pygame.image.load("platformer_assets/img/sky.png")


run =True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
                    run = False

pygame.quit()