class Playable:
	def __init__(self, name, health, attack, faction):
		self.faction = faction
		self.alive = True
		self.name = name
		self.health = health
		self.attack = attack

	def __repr__(self):
		return f"{self.name}"
		
	def _is_dead(self):
		if self.health <= 0:
			return True

	def reduce_health(self, payload):
		self.health -= payload
		if self._is_dead():
			self.alive = False

	def add_health(self, payload):
		self.health += payload

	def add_attack(self, payload):
		self.attack += payload
