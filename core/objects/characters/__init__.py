from .. import BaseObject

faction_colors = {
	"human": "white",
	"goblin": "green",
}

class BasePlayable(BaseObject):
	def __init__(self, icon, health, attack, faction):
		super().__init__(icon=icon, color=faction_colors[faction])
		self.alive = True
		self.health = health
		self.attack = attack
		self.position = None
		
	def _is_dead(self):
		if self.health <= 0:
			return True

	def reduce_health(self, payload):
		self.health -= payload
		if self._is_dead():
			self.alive = False

	def _upgrade_health(self, payload):
		self.health += payload

	def _upgrade_attack(self, payload):
		self.attack += payload
