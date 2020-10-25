from copy import copy
from .tools import graph as graph
from .tools.board_interpreter import alphabet

class Board:
	def __init__(self, size=6):
		self.board = []
		self.size = size if size <= 26 else 26 # Max size = 26
		self.empty_space = "."
		self._generate_board()

	# Magic Methods
	def __repr__(self) -> str:
		board = copy(self.board)
		for index in range(0, len(board)):
			for jndex in range(0, len(board)):
				board[index][jndex] = str(board[index][jndex])

		output = []
		for _ in range(0, self.size):
			template: str = f"{' '.join(board[_])}  {str(_ + 1)}"
			output.append(template)
		alpha_template = [f"{alphabet[_]}" for _ in range(0, self.size)]
		output.append(" ".join(alpha_template))
		return "\n".join(output)

	# Private methods
	def _generate_board(self) -> None:
		"""Generates a board based on the provided size"""
		for _ in range(0, self.size):
			self.board.append([f"{self.empty_space}" for _ in range(self.size)])

	def _call_character_attack(self, origin: graph.Point, target: graph.Point):
		if self.board[target.y][target.x] != self.empty_space:
			damage_amount = self.board[origin.y][origin.x].attack
			self.board[target.y][target.x].reduce_health(damage_amount)

	def _swap_areas(self, origin: graph.Point, target: graph.Point):
		temp_origin = copy(self.board[origin.y][origin.x])
		temp_target = copy(self.board[target.y][target.x])
		self.board[target.y][target.x] = temp_origin
		self.board[origin.y][origin.x] = temp_target
		return target

	# Public methods
	def add_content(self, target: graph.Point, payload) -> graph.Point:
		self.board[target.y][target.x] = payload
		return target

	def call_auto_character(self, origin: graph.Point, target: graph.Point) -> graph.Point:
		if origin in graph.adjacent_points(target, self.size):
			self._call_character_attack(origin, target)
			return origin
		else:
			sides = graph.adjacent_points(origin, self.size)
			closest_point = graph.shortest_distance_from_set(sides, target)
			self._swap_areas(origin, closest_point)
			return closest_point
