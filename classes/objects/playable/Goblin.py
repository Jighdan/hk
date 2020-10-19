from . import Playable

class Goblin(Playable):
	"""docstring for Goblin"""
	def __init__(self, name="#", health=5, attack=1):
		super(Goblin, self).__init__(name, health, attack)
		self.name = name
		self.health = health
		self.attack = attack


