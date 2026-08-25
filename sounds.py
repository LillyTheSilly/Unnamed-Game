import pygame
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

#load sounds
coin_fx = pygame.mixer.Sound('assets/img/coin.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('assets/img/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('assets/img/game_over.wav')
game_over_fx.set_volume(0.5)