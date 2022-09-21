import pygame


class health_bar:
	def __init__(self, screen, player, x_pos=142, y_pos=30, font_type="./font/Pixeltype.ttf", font_size=30):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.screen = screen
		self.player = player
		self.max_health = player.max_health
		self.current_health = player.health
		self.font = pygame.font.Font(font_type, font_size)

	def show_health(self):
		self.current_health = self.player.getHealth()
		health_text = "Health: " + str(self.current_health) + " / " + str(self.max_health)
		surface = self.font.render(health_text, False, "black")
		self.screen.blit(surface, (self.x_pos, self.y_pos))

class level_display:
	def __init__(self, screen, x_pos= 42, y_pos=30, font_type="./font/Pixeltype.ttf", font_size=30):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.screen = screen
		self.level = 1
		self.font = pygame.font.Font(font_type, font_size)

	def show_level(self):
		level_text = f"Level: {self.level}" 
		surface = self.font.render(level_text, False, "black")
		self.screen.blit(surface, (self.x_pos, self.y_pos))

	def set_level(self, level):
		self.level = level

class game_over:
	def __init__(self, screen, player, quit_x_pos=600, quit_y_pos=300, restart_x_pos=300, restart_y_pos=300, font_type="./font/Pixeltype.ttf", font_size=100):
		self.player = player
		self.screen = screen
		self.font_size = font_size
		self.font_type = font_type
		self.restart_y_pos = restart_y_pos
		self.restart_x_pos = restart_x_pos
		self.quit_y_pos = quit_y_pos
		self.quit_x_pos = quit_x_pos
		self.font = pygame.font.Font(font_type, font_size)
		self.game_over = False

	def show(self):
		self.game_over = self.player.getHealth() <= 0
		if self.game_over:
			black_screen_surface = pygame.image.load("./graphics/black_screen.png")
			self.screen.blit(black_screen_surface, (0,0))

			restart_text = "Restart"
			restart_surface = self.font.render(restart_text, False, "green")
			self.screen.blit(restart_surface, (self.restart_x_pos, self.restart_y_pos))

			quit_text = "Quit"
			quit_surface = self.font.render(quit_text, False, "red")
			self.screen.blit(quit_surface, (self.quit_x_pos, self.quit_y_pos))
