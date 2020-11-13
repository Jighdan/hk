from .. import BasePlayer
from ._inventory import Inventory
from ._gold import Gold

class Lead(BasePlayer):
	def __init__(self, characters: list, player_name="Illio"):
		super().__init__(characters=characters)
		self.name = player_name
		self.inventory = Inventory()
		self.gold = Gold()
