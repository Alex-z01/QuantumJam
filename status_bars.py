import pygame


class health_bar:
	def __init__(self, screen, player, x_pos=142, y_pos=30, font_type="./font/Pixeltype.ttf", font_size=30):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.player = player
		self.screen = screen
		self.current_health = player.health
		self.max_health = player.max_health
		self.font = pygame.font.Font(font_type, font_size)

	def show_health(self):
		self.current_health = self.player.get_health()
		health_text = "Health: " + str(self.current_health) + " / " + str(self.max_health)
		surface = self.font.render(health_text, False, "black")
		self.screen.blit(surface, (self.x_pos, self.y_pos))


class level_display:
	def __init__(self, screen, x_pos= 42, y_pos=30, font_type="./font/Pixeltype.ttf", font_size=30):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.screen = screen
		self.level = "1"
		self.font = pygame.font.Font(font_type, font_size)

	def show_level(self):
		level_text = "Level: " + self.level
		surface = self.font.render(level_text, False, "black")
		self.screen.blit(surface, (self.x_pos, self.y_pos))

	def update_level(self, level):
		self.level = level
