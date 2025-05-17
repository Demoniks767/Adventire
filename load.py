import pygame
from script import load_image
player_idle_image = load_image('image/player/idle')
player_run_image = load_image('image/player/run')
player_jump_image = load_image('image/player/jump')
falling_platforms_image = load_image('image/traps/falling platform')
melon_image = load_image('image/fruit/melon')
player_duble_jump_image = load_image('image/player/duble jump')
collected_image = load_image('image/fruit/collected')


earth_image = pygame.image.load('image/bloks/earth.png').convert_alpha()
earth_mini_image = pygame.image.load('image/bloks/earth2.png').convert_alpha()
earth_pink_image = pygame.image.load('image/bloks/earth-pink.png').convert_alpha()
med_image = pygame.image.load('image/bloks/med.png').convert_alpha()
rock_trap_image = pygame.image.load('image/traps/rock_trap/rock.png').convert_alpha()
spikes_image = pygame.image.load('image/traps/Spikes/Idle.png').convert_alpha()


