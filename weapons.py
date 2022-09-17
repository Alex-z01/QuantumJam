from enum import Enum
import pygame
import math
import util

class weapon_type(Enum):
	WAVE = 1
	PARTICLE = 2


class weapon:
	def __init__(self, x_pos=0, y_pos=0, angle=0, model_location="graphics/Fly/Fly1.png", ):
		self.angle = angle

		self.surface = pygame.image.load(model_location)
		self.rectangle = self.surface.get_rect(center=(x_pos, y_pos))

		self.speed = 10
		self.damage = 10

	def move(self):
		self.rectangle.left += self.speed * math.cos(math.radians(self.angle))
		self.rectangle.top += self.speed * math.sin(math.radians(self.angle))


class particle(weapon):
	def __init__(self, x_pos=0, y_pos=0, angle=0, model_location="graphics/Fly/Fly1.png"):
		super().__init__(x_pos, y_pos, angle, model_location)


class wave(weapon):
	def __init__(self, x_pos=0, y_pos=0, angle=0, model_location="graphics/New_Piskel-1.png.png", wave_growth=1.01):
		super().__init__(x_pos, y_pos, angle, model_location)
		self.model_location = model_location
		self.wave_growth = wave_growth
		self.surface = pygame.transform.rotate(pygame.image.load(self.model_location), -angle-90)
		self.rectangle = self.surface.get_rect(center=self.rectangle.center)