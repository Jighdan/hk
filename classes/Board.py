from collections import namedtuple
from copy import copy
from Area import Area
from objects.playable.Human import Human

Point = namedtuple("Point", "y x")

class Board:
	def __init__(self, size=4):
		self.board = []
		self.size = size
		self._generate_board()

	def _generate_board(self):
		iterations = 0
		while iterations < self.size:
			row = [Area() ]
			self.board.append([Area() for _ in range(self.size)])
			iterations += 1

	def __repr__(self):
		lines = [f"{line}\n" for line in self.board]
		return "".join(lines)

	def set_piece(self, payload, point):
		self.board[point.y][point.x].update(payload)

	def move_piece(self, from_point, to_point):
		point_exists = True if from_point.x and from_point.y < len(self.board) else False
		if point_exists:
			moving_value = copy(self.board[from_point.y][from_point.x])
			self.board[to_point.y][to_point.x].update(moving_value)
			self.board[from_point.y][from_point.x].clear()

b = Board()
p = Human("@")

b.set_piece(p, Point(0, 2))
print(b)

b.move_piece(Point(0, 2), Point(0, 3))
print(b)
b.move_piece(Point(0, 3), Point(1, 3))
print(b)