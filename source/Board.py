from copy import copy
from .tools import Point
from .objects.playable.goblins import Goblin
from .objects.playable.humans import Human

class Board:
	def __init__(self, size=8):
		self.board = []
		self.size = size
		self._generate_board()

	def __repr__(self):
		lines = [f"{_}\n" for _ in self.board]
		return "".join(lines)

	def _generate_board(self):
		"""Generates a board based on the provided size"""
		iterations = 0
		while iterations < self.size:
			self.board.append([" " for _ in range(self.size)])
			iterations += 1

	def set_area(self, target, payload):
		self.board[target.y][target.x] = payload

	def _is_area_in_range(self, target):
		x_in_range = target.x < len(self.board) and target.x >= 0
		y_in_range = target.y < len(self.board) and target.y >= 0
		return True if x_in_range and y_in_range else False

	def _adjacent_areas(self, origin):
		up = Point(origin.y - 1, origin.x)
		down = Point(origin.y + 1, origin.x)
		left = Point(origin.y, origin.x - 1)
		right = Point(origin.y, origin.x + 1)
		possible_points = [up, down, left, right]
		return [_ for _ in possible_points if self._is_area_in_range(_)]

	def _move_piece(self, origin, target):
		if target in self._adjacent_areas(origin):
			temp_value = copy(self.board[origin.y][origin.x])
			self.board[target.y][target.x] = temp_value
			self.board[origin.y][origin.x] = " "

	def call_enemy_move(self, origin, target):
		if origin in self._adjacent_areas(target):
			return
		else:
			y, x = [origin.y, origin.x]
			if origin.x == target.x:
				y = origin.y - 1 if target.y < origin.y else origin.y + 1
			elif origin.y == target.y:
				x = origin.x - 1 if target.x < origin.x else origin.x + 1
			else:
				y = origin.y - 1 if target.y < origin.y else origin.y + 1
				x = origin.x - 1 if target.x < origin.x else origin.x + 1
			self._move_piece(origin, Point(y, x))

	def call_attack(self, origin, target):
		target_contains = self.board[target.y][target.x]
		if target in self._adjacent_areas(origin) and target_contains:
			damage_amount = self.board[origin.y][origin.x].attack
			self.board[target.y][target.x].reduce_health(damage_amount)
