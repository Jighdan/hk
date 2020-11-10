from .tools.graph import Point, AlphaPoint
from .tools.board_interpreter import convert_alpha_to_point, convert_point_to_alpha

class Machine:
	def __init__(self):
		self.character = None
		self.character_position = None
		
	def set_character(self, payload) -> None:
		self.character = payload

	def set_character_position(self, payload: Point) -> None:
		self.character_position = payload


class Player:
	def __init__(self, name):
		self.name = name
		self.character = None
		self.character_position = None
		self.ref_board = None

	def __str__(self) -> str:
		return str(self.character)

	def set_character(self, payload) -> None:
		self.character = payload

	def set_character_initial_position(self, payload) -> None:
		self.character_position = payload

	def call_character_move(self, target_position: AlphaPoint) -> AlphaPoint:
		temp_position = convert_alpha_to_point(self.character_position)
		self.ref_board.move_content(temp_position, convert_alpha_to_point(target_position))
		self.character_position = convert_point_to_alpha(temp_position)
		return target_position

	def call_character_attack(self, target_position: AlphaPoint) -> AlphaPoint:
		temp_position = convert_alpha_to_point(self.character_position)
		self.ref_board.call_character_attack(temp_position, target_position)
		return target_position
