from collections import namedtuple
from copy import copy
from Area import Area
from objects.playable.Human import Human
from objects.playable.Goblin import Goblin

Point = namedtuple("Point", "y x")

class Board:
	def __init__(self, size=4):
		self.board = []
		self.size = size
		self._generate_board()

	def _generate_board(self):
		iterations = 0
		while iterations < self.size:
			self.board.append([" " for _ in range(self.size)])
			iterations += 1

	def show_board(self):
		for line in self.board:
			print(line)
		print("\n")

	def set_piece(self, payload, point):
		self.board[point.y][point.x] = payload

	def move_piece(self, from_point, to_point):
		point_exists = True if from_point.x and from_point.y < len(self.board) else False
		if point_exists:
			moving_value = copy(self.board[from_point.y][from_point.x])
			self.board[to_point.y][to_point.x] = moving_value
			self.board[from_point.y][from_point.x] = " "

	def call_attack(self, origin, to):
		damage = self.board[origin.y][origin.x].attack
		self.board[to.y][to.x].reduce_health(damage)

b = Board()
h = Human()
g = Goblin()

b.set_piece(h, Point(0, 2))
b.set_piece(g, Point(3, 1))
b.show_board()

b.move_piece(Point(0, 2), Point(0, 3))
b.show_board()
b.move_piece(Point(0, 3), Point(1, 3))

b.show_board()
b.call_attack(Point(1, 3), Point(3, 1))

b.show_board()
