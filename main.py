import pygame
import os
import sys
import random

from pygame import K_RETURN

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1920
HEIGHT = 1080
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
from load import *
from math import (cos, sin, radians)
from random import (choice)

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velocity_y= 0
        self.on_ground = True
        self.speed = 5
        self.frame = 0
        self.skore = 0
        self.timer_anime = 0
        self.anime = False
        self.key = pygame.key.get_pressed()
        self.dir = 'right'
        self.hp = 100
        self.timer_attack = 0

    def update(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x += self.speed
            self.image = player_idle_image[self.frame]
            self.anime = True
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.update(-self.speed)
        if key[pygame.K_a]:
            self.rect.x -= self.speed
            self.image = pygame.transform.flip(player_idle_image[self.frame], True, False)
            self.anime = True
            if self.rect.left < 100:
                self.rect.left = 100
                camera_group.update(+self.speed)

        self.animation()
        self.attack()
        self.jump()
        self.draw_stats()
        self.key = pygame.key.get_pressed()



    def animation(self):
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_idle_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0







    def jump(self):
        if self.key[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -15
            self.on_ground = False
        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10




class Earth(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Earth_pink(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Earth_orange(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Med(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Plita_w(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Earth(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]





def restart():
    global player_group, player, camera_group
    player_group = pygame.sprite.Group()
    player = Player(player_idle_image, (300, 300))
    player_group.add(player)
    camera_group = pygame.sprite.Group()





