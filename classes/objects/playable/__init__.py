class Playable:
	def __init__(self, name, health, attack):
		self.alive = True
		self.name = name
		self.health = health
		self.attack = attack

	def __repr__(self):
		fmt = f"HP: {self.health}" if self.alive else "Dead"
		return f"{self.name} | {fmt}"
		

	def _is_dead(self):
		if self.health <= 0:
			return True

	def reduce_health(self, payload):
		self.health -= payload
		if self._is_dead():
			self.alive = False
