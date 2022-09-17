import math

import pygame
import weapons


def calculate_angle(src_x, src_y, target_x, target_y):
	radians = math.atan2(target_y - src_y, target_x - src_x)
	return math.degrees(radians)


def rot_center(image, angle, x, y):
	rotated_image = pygame.transform.rotate(image, angle)
	new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

	return rotated_image, new_rect


def is_onscreen(rectangle):
	w, h = pygame.display.get_surface().get_size()
	if rectangle.top > 0 and rectangle.bottom < h and rectangle.left > 0 and rectangle.right < w:
		return True
	return False


class Player:
	def __init__(self, x_pos=0, y_pos=0, model_location="graphics/player/player_walk_1.png"):
		self.angle = 0

		self.model_location = model_location
		self.surface = pygame.image.load(model_location)
		self.rectangle = self.surface.get_rect(midbottom=(x_pos, y_pos))

		self.weapon = weapons.weapon_type.PARTICLE
		self.projectiles = []
		self.time_since_last_attack = 0
		self.delay_between_attack = 300  # 300 ms delay between attacks, higher value = less attack speed
		self.health = 100

		self.horizontal_speed = 5
		self.vertical_speed = 5

	def get_surface(self):
		return self.surface

	def get_rectangle(self):
		return self.rectangle

	def on_key_press(self, keys_pressed):
		w, h = pygame.display.get_surface().get_size()

		if (keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]) and self.rectangle.top > 0:
			self.rectangle.top -= self.vertical_speed
		if (keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]) and self.rectangle.bottom < h:
			self.rectangle.top += self.vertical_speed
		if (keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]) and self.rectangle.left > 0:
			self.rectangle.left -= self.horizontal_speed
		if (keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]) and self.rectangle.right < w:
			self.rectangle.left += self.horizontal_speed

		if keys_pressed[pygame.K_q] or keys_pressed[pygame.K_e]:  # swap weapon with q or e
			self.swap_weapon()

	def attack(self, mouse):
		current_time = pygame.time.get_ticks()
		if mouse.get_pressed()[0] and current_time - self.time_since_last_attack > self.delay_between_attack:
			mouse_location_x, mouse_location_y = mouse.get_pos()
			angle = calculate_angle(self.rectangle.centerx, self.rectangle.centery, mouse_location_x, mouse_location_y)

			self.angle = angle
			self.surface = pygame.transform.rotate(pygame.image.load(self.model_location), -self.angle)
			self.rectangle = self.surface.get_rect(center=self.rectangle.center)

			self.time_since_last_attack = current_time
			self.projectiles.append(weapons.particle(self.rectangle.centerx, self.rectangle.centery, angle))

	# Need enemy.get_hitbox() and enemy.get_damage() implemented, todo
	def detect_enemy_collision(self, enemies):
		for enemy in enemies:
			enemy_hitbox = enemy.get_hitbox()
			if self.rectangle.colliderect(enemy_hitbox):
				self.health -= enemy.get_damage()

	def handle_projectiles(self, screen):
		on_screen_projectiles = []
		for projectile in self.projectiles:
			projectile.move()
			if is_onscreen(projectile.rectangle):
				on_screen_projectiles.append(projectile)
			screen.blit(projectile.surface, projectile.rectangle)
		self.projectiles = on_screen_projectiles

	def swap_weapon(self):
		if self.weapon == weapons.weapon_type.PARTICLE:
			self.weapon = weapons.weapon_type.WAVE
		elif self.weapon == weapons.weapon_type.WAVE:
			self.weapon = weapons.weapon_type.PARTICLE

	def do_player_things(self, screen, key_pressed, mouse, enemies):  # enemies have rectangle collision box and damage
		self.on_key_press(key_pressed)
		self.attack(mouse)
		self.handle_projectiles(screen)
		self.detect_enemy_collision(enemies)

		screen.blit(self.surface, self.rectangle)
