from . import Playable

class Human(Playable):
	def __init__(self, name, health=10, attack=2):
		super(Human, self).__init__(name, health, attack)
		self.name = name
		self.health = health
		self.attack = attack

	
