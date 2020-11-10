from . import Playable

class Human(Playable):
	def __init__(self):
		super().__init__(icon="@", health=10, attack=1, faction="human")
		self.holding_item = None

	def add_stats_from_holding_item(self):
		"""Upgrades target attribute from item"""
		# ONLY UPDATES ATTACK(?)
		if self.holding_item:
			self._upgrade_attack(self.holding_item.value)

	def set_holding(self, payload) -> None:
		self.holding = payload

