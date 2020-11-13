from . import BasePlayable

class Human(BasePlayable):
	def __init__(self, health, attack):
		super().__init__(icon="@", health=health, attack=attack, faction="human")
		self.health = health
		self.attack = attack
		self.holding_item = None
