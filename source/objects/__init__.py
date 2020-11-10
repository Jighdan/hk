from termcolor import colored

class BaseObject:
	def __init__(self, icon, color):
		self.icon = icon
		self.color = color

	def __str__(self):
		return colored(self.icon, self.color)

