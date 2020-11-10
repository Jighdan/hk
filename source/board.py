from typing import List
from copy import copy
from .tools.graph import Point, adjacent_points, shortest_distance_from_set
from .tools.board_interpreter import alphabet

class Board:
	def __init__(self, size=8):
		self.board: List[List] = []
		self.size: int = size if size <= 26 else 26 # Max size = 26
		self.empty_space: str = "."
		self._generate_board()

	def __str__(self) -> str:
		temp_board = copy(self.board)
		output = []

		# Converts every item in the list to string
		for y in range(0, len(temp_board)):
			for x in range(0, len(temp_board)):
				temp_board[y][x] = str(temp_board[y][x])

		for _ in range(0, self.size):
			template: str = f"{' '.join(temp_board[_])}  {str(_ + 1)}"
			output.append(template)
		alpha_template = [alphabet[_] for _ in range(self.size)]
		output.append(" ".join(alpha_template))
		return "\n".join(output)

	def _is_area_empty(self, target: Point) -> bool:
		return True if self.board[target.y][target.x] == self.empty_space else False

	def _generate_board(self) -> None:
		"""Generates a board based on the provided size"""
		for _ in range(0, self.size):
			self.board.append([f"{self.empty_space}" for _ in range(self.size)])

	def _remove_content(self, target: Point):
		self.board[target.y][target.x] = self.empty_space

	def _swap_areas(self, origin: Point, target: Point):
		temp_origin = copy(self.board[origin.y][origin.x])
		temp_target = copy(self.board[target.y][target.x])
		self.board[target.y][target.x] = temp_origin
		self.board[origin.y][origin.x] = temp_target
		return target

	def move_content(self, origin: Point, target: Point) -> Point:
		temp_origin = self.board[origin.y][origin.x]
		# Check if target is empty
		if self.board[target.y][target.x] == self.empty_space:
			self.board[origin.y][origin.x] = self.empty_space
			self.board[target.y][target.x] = temp_origin
			return target
		else:
			return origin

	def add_content(self, target: Point, payload: any) -> Point:
		if self._is_area_empty(target):
			self.board[target.y][target.x] = payload
		return target

	# def call_character_attack(self, origin: Point, target: Point):
	# 	if self.board[target.y][target.x] != self.empty_space:
	# 		damage_amount = self.board[origin.y][origin.x].attack
	# 		self.board[target.y][target.x].reduce_health(damage_amount)

	# def call_auto_character(self, origin: Point, target: Point) -> Point:
	# 	if origin in adjacent_points(target, self.size):
	# 		self.call_character_attack(origin, target)
	# 		return origin
	# 	else:
	# 		sides = adjacent_points(origin, self.size)
	# 		closest_point = shortest_distance_from_set(sides, target)
	# 		self._swap_areas(origin, closest_point)
	# 		return closest_point
