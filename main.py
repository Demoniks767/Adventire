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


class SuperGroup(pygame.sprite.Group):
    def camera_update(self, stepx, stepy):
        for sprite in self.sprites():
            sprite.camera_move(stepx, stepy)


class Camera():
    def camera_move(self, stepx, stepy):
        self.rect.x += stepx
        self.rect.y += stepy


class Player(pygame.sprite.Sprite, Camera):
    def __init__(self, image_lists, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists[0]
        self.current_list = player_idle_image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velocity_y = 0
        self.on_ground = True
        self.anime_idle = True
        self.anime_jump = False
        self.anime_duble_jump = False
        self.speed = 5
        self.frame = 0
        self.skore = 0
        self.timer_anime = 0
        self.anime = False
        self.key = pygame.key.get_pressed()
        self.dir = 'right'
        self.hp = 100
        self.timer_attack = 0
        self.duble_jump = True
        self.timer_jump = 0

    def update(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x += self.speed

            self.anime = True
            self.current_list = player_run_image
            try:
                self.image = player_run_image[self.frame]
            except:
                self.frame = 0
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.camera_update(-self.speed, 0)
        if key[pygame.K_a]:
            self.rect.x -= self.speed
            self.anime = True
            self.current_list = player_run_image
            try:
                self.image = pygame.transform.flip(player_run_image[self.frame], True, False)
            except:
                self.frame = 0
            if self.rect.left < 100:
                self.rect.left = 100
                camera_group.camera_update(+self.speed, 0)
        if self.rect.bottom > 900:
            self.rect.bottom = 900
            camera_group.camera_update(0, -self.velocity_y)

        self.animation()
        # self.attack()
        self.jump()
        # self.draw_stats()
        self.key = pygame.key.get_pressed()

    def animation(self):
        print(self.frame)
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(self.current_list) - 1:

                    self.frame = 0
                    if self.anime_jump:
                        self.current_list = player_idle_image
                        self.anime_jump = False
                        self.anime_idle = True
                    if self.anime_duble_jump:
                        self.current_list = player_idle_image
                        self.anime_duble_jump = False
                        self.anime_idle = True

            else:
                self.frame += 1
            self.timer_anime = 0



    def jump(self):
        if self.key[pygame.K_SPACE] and self.on_ground:
            print(2)
            self.velocity_y = -15
            self.on_ground = False
        if self.on_ground == False:
            self.timer_jump += 1
            if self.key[pygame.K_SPACE] and self.duble_jump and self.timer_jump / FPS > 0.3:
                print(3)
                self.velocity_y = -15
                self.on_ground = False
                self.anime = True
                self.duble_jump = False
                self.timer_jump = 0

        self.rect.y += self.velocity_y
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10


class RockTrap(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = -5
        self.height = 500

    def update(self):
        self.rect.y += self.speed
        self.height -= abs(self.speed)
        if self.height <= 0:
            self.speed *= -1
            self.height = 500

        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
                player.on_ground = True
                player.duble_jump = True
                player.timer_jump = 0
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Earth(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
                player.duble_jump = True
                player.timer_jump = 0
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Earth_pink(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):

        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
                player.on_ground = True
                player.duble_jump = True
                player.timer_jump = 0
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Earth_orange(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Med(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
                player.on_ground = True
                player.duble_jump = True
                player.timer_jump = 0
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Plita_w(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Falling_platform(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
                player.on_ground = True
                player.duble_jump = True
                player.timer_jump = 0
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


class Spikes(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Melon(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            player.skore += 50
            self.kill()


class Earth_mini(pygame.sprite.Sprite, Camera):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top - 5
                player.on_ground = True
                player.on_ground = True
                player.duble_jump = True
                player.timer_jump = 0
            if abs(self.rect.bottom - player.rect.top) < 15:
                player.rect.top = self.rect.bottom + 5
                player.velocity_y = 0
            if (abs(self.rect.left - player.rect.right) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.right = self.rect.left
            if (abs(self.rect.right - player.rect.left) < 15
                    and abs(self.rect.centery - player.rect.centery) < 50):
                player.rect.left = self.rect.right


def restart():
    global player_group, player, camera_group, earth_group, earth_mini_group, earth_pink_group, spikes_group, rock_trap_group, falling_platforms_group, med_group, melon_group
    player_group = pygame.sprite.Group()
    player = Player(player_idle_image, (100, 800))
    player_group.add(player)
    camera_group = SuperGroup()
    earth_group = pygame.sprite.Group()
    earth_mini_group = pygame.sprite.Group()
    earth_pink_group = pygame.sprite.Group()
    spikes_group = pygame.sprite.Group()
    rock_trap_group = pygame.sprite.Group()
    falling_platforms_group = pygame.sprite.Group()
    med_group = pygame.sprite.Group()
    melon_group = pygame.sprite.Group()


def game_lvl():
    sc.fill('pink')
    player_group.update()
    player_group.draw(sc)
    earth_group.update()
    earth_group.draw(sc)
    earth_mini_group.update()
    earth_mini_group.draw(sc)
    earth_pink_group.update()
    earth_pink_group.draw(sc)
    med_group.update()
    med_group.draw(sc)
    melon_group.update()
    melon_group.draw(sc)
    spikes_group.update()
    spikes_group.draw(sc)
    falling_platforms_group.update()
    falling_platforms_group.draw(sc)
    rock_trap_group.update()
    rock_trap_group.draw(sc)
    pygame.display.update()


def drawMaps(nameFile):
    global player
    maps = []
    source = 'game lvl/' + str(nameFile)
    with open(source, 'r') as file:
        for i in range(0, 16):
            maps.append(file.readline().replace('\n', '').split(',')[0:-1])

    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == '1':

                earth = Earth(earth_image, pos)
                earth_group.add(earth)
                camera_group.add(earth)
            elif maps[i][j] == '2':
                med = Med(med_image, pos)
                med_group.add(med)
                camera_group.add(med)
            elif maps[i][j] == '3':
                earth_mini = Earth_mini(earth_mini_image, pos)
                earth_mini_group.add(earth_mini)
                camera_group.add(earth_mini)
            elif maps[i][j] == '4':
                spikes = Spikes(spikes_image, pos)
                spikes_group.add(spikes)
                camera_group.add(spikes)
            elif maps[i][j] == '5':
                rocktrap = RockTrap(rock_trap_image, pos)
                rock_trap_group.add(rocktrap)
                camera_group.add(rocktrap)
            elif maps[i][j] == '6':
                earth_pink = Earth_pink(earth_pink_image, pos)
                earth_pink_group.add(earth_pink)
                camera_group.add(earth_pink)
            elif maps[i][j] == '7':
                falling_platform = Falling_platform(falling_platforms_image, pos)
                falling_platforms_group.add(falling_platform)
                camera_group.add(falling_platform)
            elif maps[i][j] == '8':
                melon = Melon(melon_image, pos)
                melon_group.add(melon)
                camera_group.add(melon)


restart()
drawMaps('untitled.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)
