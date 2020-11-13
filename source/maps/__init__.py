from ..core.modules.graph import Point, Graph
from ..core._board import Board
from ..core.objects.terrain import Rock, Water

rock = Rock()
water = Water()

class TemplateMap:
	def __init__(self, map_size: int):
		self.board = Board(size=map_size)

	def __repr__(self) -> str:
		return str(self.board)

	def add_line(self, direction: str, payload) -> None:
		pass

	def add_square(self, origin: Point, payload) -> None:
		"""Fills a 2x2 square"""
		self.board.add_content(origin, payload)
		self.board.add_content(Point(origin.x + 1, origin.y), payload)
		self.board.add_content(Point(origin.x, origin.y + 1), payload)
		self.board.add_content(Point(origin.x + 1, origin.y + 1), payload)
