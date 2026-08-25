import pygame
from pygame.locals import *
from pygame import mixer
import pickle
from os import path

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.font.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")

#define game variables
tile_size = 50
game_over = 0
main_menu = True
level = 1

#load images
sun_img = pygame.image.load("assets/img/sun.png")
bg_img = pygame.image.load("assets/img/sky.png")
restart_img = pygame.image.load("assets/img/restart_btn.png")
start_img = pygame.image.load("assets/img/start_btn.png")
exit_img = pygame.image.load("assets/img/exit_btn.png")
lava_img = pygame.image.load("assets/img/lava.png")
blob_img = pygame.image.load("assets/img/blob.png")
coin_img = pygame.image.load("assets/img/coin.png")


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check for clicks
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
            self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        screen.blit(self.image, self.rect)

        return action


#load sounds
coin_fx = pygame.mixer.Sound('assets/img/coin.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('assets/img/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('assets/img/game_over.wav')
game_over_fx.set_volume(0.5)

class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'assets/img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            self.images_right.append(img_right)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0


    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5

        #get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            jump_fx.play()
            self.vel_y = -15
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_LEFT] ==False and key[pygame.K_RIGHT]==False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_right[self.index]


        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #check for collision
        for tile in world.tile_list:
            #check for collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            #check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #check if bellow the ground - jumping
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                    # check if above the ground - falling
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0


        #update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0

        #draw player onto screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

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
                if tile == 3:
                    img = pygame.transform.scale(exit_img, (tile_size, tile_size))
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

#load in data, create level from file
if path.exists(f'Levels/level{level}_data'):
    pickle_in = open(f'Levels/level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
world = World(world_data)


def draw(self):
    for tile in self.tile_list:
        screen.blit(tile[0], tile[1])

class Exit():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("assets/img/exit.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()

player = Player(100, screen_height - 130)

restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)


#main game loop
run = True
while run:

    clock.tick(fps)

    screen.blit(bg_img, (0,0))
    screen.blit(sun_img,(100, 100))

    if main_menu:
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False
    else:
        world.draw()
        player.update()

    #event handler
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    pygame.display.update()

pygame.quit()