from typing import List
from copy import copy
from .modules.graph import Point
from .modules.board_interpreter import alphabet

class Board:
	def __init__(self, size=8, empty_area="."):
		self.board: List[List] = []
		self.size: int = size if size <= 26 else 26 # Max size = 26
		self.empty_area: str = empty_area
		self.space_between: str = " "
		self._generate_board()

	def __str__(self) -> str:
		temp_board = copy(self.board)
		# Converts every item in the list to string
		for y in range(0, len(temp_board)):
			for x in range(0, len(temp_board)):
				temp_board[y][x] = str(temp_board[y][x])

		output = [f"{self.space_between.join(temp_board[_])} {str(_ + 1)}" for _ in range(0, self.size)]
		output.append(self.space_between.join([alphabet[_] for _ in range(self.size)]))
		return "\n".join(output)

	def _is_area_empty(self, target: Point) -> bool:
		return True if self.board[target.y][target.x] == self.empty_area else False

	def _generate_board(self) -> None:
		"""Generates a board based on the provided size"""
		for _ in range(0, self.size):
			self.board.append([f"{self.empty_area}" for _ in range(self.size)])

	def _remove_content(self, target: Point):
		self.board[target.y][target.x] = self.empty_area

	def _swap_areas(self, origin: Point, target: Point):
		temp_origin = copy(self.board[origin.y][origin.x])
		temp_target = copy(self.board[target.y][target.x])
		self.board[target.y][target.x] = temp_origin
		self.board[origin.y][origin.x] = temp_target
		return target

	def move_content(self, origin: Point, target: Point) -> Point:
		temp_origin = self.board[origin.y][origin.x]
		# Check if target is empty
		if self.board[target.y][target.x] == self.empty_area:
			self.board[origin.y][origin.x] = self.empty_area
			self.board[target.y][target.x] = temp_origin
			return target
		else:
			return origin

	def add_content(self, target: Point, payload: any) -> Point:
		if self._is_area_empty(target):
			self.board[target.y][target.x] = payload
		return target
