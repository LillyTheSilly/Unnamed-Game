import pygame
from pygame.locals import *

pygame.font.init()

clock = pygame.time.Clock()
fps = 60


screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Level 1")

# define game variables
tile_size = 50



#load images
sun_img = pygame.image.load("assets/img/sun.png")
bg_img = pygame.image.load("assets/img/sky.png")

#grid
def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'assets/img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            self.images_right.append(img_right)
        #self.image = pygame.transform.scale(img (40, 80))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False


    def update(self):
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5

        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #check for collision

        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
        dy = 0

        # draw player onto screen
        screen.blit(self.image, self.rect)


class World():
    def __init__(self, data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load("assets/img/dirt.png")
        grass_img = pygame.image.load("assets/img/grass.png")

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])


word_data = [

]

world = World(word_data)


def draw(self):
    for tile in self.tile_list:
        screen.blit(tile[0], tile[1])


player = Player(100, screen_height - 130)


run =True
while run:

    clock.tick(fps)

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img,(100, 100))

    world.draw()
    player.update()


    draw_grid()
    # event handler
    for event in pygame.event.get():
        if event.type == QUIT:
                    run = False

    pygame.display.update()

pygame.quit()