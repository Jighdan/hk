from ..modules.graph import Point, AlphaPoint
from ..modules.board_interpreter import convert_alpha_to_point, convert_point_to_alpha

class BasePlayer:
	def __init__(self, character):
		self.character = character
		self.position: Point = None

	def __str__(self) -> str:
		return str(self.character)

	def set_position(self, position: Point) -> None:
		self.position = position
