from .. import BasePlayer
from ._inventory import Inventory
from ._gold import Gold

class Player(BasePlayer):
	def __init__(self, character):
		super().__init__(character=character)
		self.name = "Illio"
		self.inventory = Inventory()

	def __str__(self) -> str:
		return str(self.character)

	def set_character(self, payload) -> None:
		self.character = payload

	def set_character_initial_position(self, payload) -> None:
		self.character_position = payload

