import math
import pygame

def calculate_angle(src_x, src_y, target_x, target_y):
	radians = math.atan2(target_y - src_y, target_x - src_x)
	return math.degrees(radians)


def rot_center(image, angle, x, y):
	rotated_image = pygame.transform.rotate(image, angle)
	new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

	return rotated_image, new_rect


def is_onscreen(rectangle):
	w, h = pygame.display.get_surface().get_size()
	if (rectangle.top > 0 and rectangle.bottom < h) or (rectangle.right > 0 and rectangle.left < w):
		return True
	return False