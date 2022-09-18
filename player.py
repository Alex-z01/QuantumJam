import pygame
import util
import GLOBALS
from particle import Particle
from waveProj import Wave

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)

        self.angle = 0

        self.image_loc = image
        self.image = pygame.image.load(self.image_loc)

        centerX = GLOBALS.SCREEN_W / 2
        centerY = GLOBALS.SCREEN_H / 2
        self.rect = self.image.get_rect(midbottom=(centerX, centerY))
        self.pos = (centerX, centerY)

        self.weapon = 0
        self.projectiles = pygame.sprite.Group()
        self.time_since_last_attack = 0
        self.time_since_weapon_swap = 0
        self.time_since_damage_taken = 0
        self.weapon_swap_delay = 200
        self.attack_delay = 300  # 300 ms delay between attacks, higher value = less attack speed
        self.damage_taken_delay = 1000
        self.max_health = 100
        self.health = self.max_health
        self.horizontal_speed = 5
        self.vertical_speed = 5

    def getHealth(self):
        return self.health

    def actions(self, key_pressed):
        w, h = pygame.display.get_surface().get_size()

        if (key_pressed[pygame.K_UP] or key_pressed[pygame.K_w]) and self.rect.top > 0:
            self.rect.top -= self.vertical_speed
        if (key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_s]) and self.rect.bottom < h:
            self.rect.top += self.vertical_speed
        if (key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_a]) and self.rect.left > 0:
            self.rect.left -= self.horizontal_speed
        if (key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_d]) and self.rect.right < w:
            self.rect.left += self.horizontal_speed

        current_time = pygame.time.get_ticks()
        if (key_pressed[pygame.K_q] or key_pressed[pygame.K_e]) and \
                current_time - self.time_since_weapon_swap > self.weapon_swap_delay:
            self.swap_weapon()
            self.time_since_weapon_swap = current_time
    
    def swap_weapon(self):
        if self.weapon == 1:
            self.weapon = 0
        else:
            self.weapon = 1
        print(self.weapon)

    def attack(self, mouse):
        current_time = pygame.time.get_ticks()
        mouse_location_x, mouse_location_y = mouse.get_pos()
        angle = util.calculate_angle(self.rect.centerx, self.rect.centery, mouse_location_x, mouse_location_y)
        self.angle = angle
        self.image = pygame.transform.rotate(pygame.image.load(self.image_loc), -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        if mouse.get_pressed()[0] and current_time - self.time_since_last_attack > self.attack_delay:
            self.time_since_last_attack = current_time
            if self.weapon == 0:
                self.projectiles.add(Particle(self.rect.centerx, self.rect.centery, GLOBALS.FLY1, angle))
            else:
                self.projectiles.add(Wave(self.rect.centerx, self.rect.centery, GLOBALS.WAVE, angle))

    def TakeDamage(self, damage):
        self.health -= damage

    def update(self, key_pressed):
        self.actions(key_pressed)
        self.attack(pygame.mouse)
        self.projectiles.draw(GLOBALS.SCREEN)
        self.projectiles.update()