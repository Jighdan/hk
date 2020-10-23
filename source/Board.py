from copy import copy
from .tools import graph as graph

class Board:
	def __init__(self, size=8):
		self.board = []
		self.size = size
		self._generate_board()

	# Magic Methods
	def __repr__(self):
		lines = [f"{_}\n" for _ in self.board]
		return "".join(lines)

	# Private methods
	def _generate_board(self) -> None:
		"""Generates a board based on the provided size"""
		for _ in range(0, self.size):
			self.board.append([" " for _ in range(self.size)])

	def _call_character_attack(self, origin: graph.Point, target: graph.Point):
		if self.board[target.y][target.x] != " ":
			damage_amount = self.board[origin.y][origin.x].attack
			self.board[target.y][target.x].reduce_health(damage_amount)

	def _move_from_area(self, origin: graph.Point, target: graph.Point):
		temp_value = copy(self.board[origin.y][origin.x])
		self.board[target.y][target.x] = temp_value
		self.board[origin.y][origin.x] = " "
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
			self._move_from_area(origin, closest_point)
			return closest_point
