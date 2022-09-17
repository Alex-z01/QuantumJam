from enum import Enum
import pygame
import math


class weapon_type(Enum):
	WAVE = 1
	PARTICLE = 2


class particle:
	def __init__(self, x_pos=0, y_pos=0, angle=0, model_location="graphics/Fly/Fly1.png", ):
		self.angle = angle

		self.surface = pygame.image.load(model_location)
		self.rectangle = self.surface.get_rect(center=(x_pos, y_pos))

		self.speed = 10

	def move(self):
		self.rectangle.left += self.speed * math.cos(math.radians(self.angle))
		self.rectangle.top += self.speed * math.sin(math.radians(self.angle))