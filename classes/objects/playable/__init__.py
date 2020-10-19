class Playable:
	def __init__(self, name, health, attack):
		self.name = name
		self.health = health
		self.attack = attack

	def __repr__(self):
		return f"{self.name}"

	def reduce_health(self, payload):
		self.health -= payload

