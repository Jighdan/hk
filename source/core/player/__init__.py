from ..modules.graph import Point, AlphaPoint
from ..modules.board_interpreter import convert_alpha_to_point, convert_point_to_alpha

class BasePlayer:
	def __init__(self, characters: list):
		self.characters: list = characters

	def __repr__(self) -> list:
		return [_ for _ in self.characters]

	def __str__(self) -> list:
		return [str(_) for _ in self.characters]

