import pygame
from pygame.locals import *

pygame.font.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Level 1")

# variables
tile_size = 200

# image load
sun_img = pygame.image.load("assets/img/sun.png")
bg_img = pygame.image.load("assets/img/sky.png")

def draw_grid():
    for line in range(0, 6):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


world_data =

[1, 1, 1, 1, 1]





run =True
while run:

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img,(100, 100))


    draw_grid()
    for event in pygame.event.get():
        if event.type == QUIT:
                    run = False

    pygame.display.update()

pygame.quit()