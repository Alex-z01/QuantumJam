import math

import pygame
import util


class Player:
	def __init__(self, x_pos=0, y_pos=0, model_location="graphics/player/player_walk_1.png"):
		self.angle = 0

		self.model_location = model_location
		self.surface = pygame.image.load(model_location)
		self.rectangle = self.surface.get_rect(midbottom=(x_pos, y_pos))
		self.rect = self.rectangle

		self.weapon = weapons.weapon_type.PARTICLE
		self.projectiles = []
		self.time_since_last_attack = 0
		self.time_since_weapon_swap = 0
		self.time_since_damage_taken = 0
		self.weapon_swap_delay = 200
		self.attack_delay = 300  # 300 ms delay between attacks, higher value = less attack speed
		self.damage_taken_delay = 1000
		self.health = 100
		self.max_health = 100

		self.horizontal_speed = 5
		self.vertical_speed = 5

	def get_surface(self):
		return self.surface

	def get_rectangle(self):
		return self.rectangle

	def get_health(self):
		return self.health

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

		current_time = pygame.time.get_ticks()
		if (keys_pressed[pygame.K_q] or keys_pressed[pygame.K_e]) and \
				current_time - self.time_since_weapon_swap > self.weapon_swap_delay:
			self.swap_weapon()
			self.time_since_weapon_swap = current_time

	def attack(self, mouse):
		current_time = pygame.time.get_ticks()
		mouse_location_x, mouse_location_y = mouse.get_pos()
		angle = util.calculate_angle(self.rectangle.centerx, self.rectangle.centery, mouse_location_x, mouse_location_y)
		self.angle = angle
		self.surface = pygame.transform.rotate(pygame.image.load(self.model_location), -self.angle)
		self.rectangle = self.surface.get_rect(center=self.rectangle.center)

		if mouse.get_pressed()[0] and current_time - self.time_since_last_attack > self.attack_delay:
			self.time_since_last_attack = current_time
			if self.weapon == weapons.weapon_type.PARTICLE:
				self.projectiles.append(weapons.particle(self.rectangle.centerx, self.rectangle.centery, angle))
			elif self.weapon == weapons.weapon_type.WAVE:
				self.projectiles.append(weapons.wave(self.rectangle.centerx, self.rectangle.centery, angle))

	def calculate_player_damage_taken(self, enemy):
		current_time = pygame.time.get_ticks()
		if current_time - self.time_since_damage_taken > self.damage_taken_delay:
			self.health -= enemy.getDMG()
			self.time_since_damage_taken = current_time

	def calculate_enemy_damage_taken(self, enemy, projectile):
		enemy_current_hp = enemy.getCurrentHP()
		projectile_damage = projectile.get_damage()
		enemy.setCurrentHP(enemy_current_hp - projectile_damage)

	def detect_enemy_collision(self, enemies, enemy_projectiles):
		for enemy in enemies:
			enemy_hitbox = enemy.rect
			if self.rectangle.colliderect(enemy_hitbox):
				self.calculate_player_damage_taken(enemy)

	def handle_player_projectiles(self, screen, enemies):
		# check if projectile hits an enemy, destroy projectile if it does
		on_screen_projectiles = []
		for projectile in self.projectiles:
			collision_detected = False
			for enemy in enemies:
				if projectile.get_rectangle().colliderect(enemy):
					self.calculate_enemy_damage_taken(enemy, projectile)
					collision_detected = True
			if not collision_detected:
				on_screen_projectiles.append(projectile)
		self.projectiles = on_screen_projectiles

		# check if projectile still in screen
		on_screen_projectiles = []
		for projectile in self.projectiles:
			projectile.move()
			if util.is_onscreen(projectile.rectangle):
				on_screen_projectiles.append(projectile)
			screen.blit(projectile.surface, projectile.rectangle)
		self.projectiles = on_screen_projectiles

	def swap_weapon(self):
		if self.weapon == weapons.weapon_type.PARTICLE:
			self.weapon = weapons.weapon_type.WAVE
		elif self.weapon == weapons.weapon_type.WAVE:
			self.weapon = weapons.weapon_type.PARTICLE

	def do_player_things(self, screen, key_pressed, mouse, enemies, enemy_projectiles):
		self.on_key_press(key_pressed)
		self.attack(mouse)
		self.handle_player_projectiles(screen, enemies)
		self.detect_enemy_collision(enemies, enemy_projectiles)

		screen.blit(self.surface, self.rectangle)
