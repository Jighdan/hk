# Base
from random import randint
from typing import List
from .board import Board
from .core.player import Player
from .interface import Display, Interface
from .tools.graph import Point
from .tools.board_interpreter import convert_alpha_to_point, convert_point_to_alpha
from .objects.characters.humans import Human
from .objects.characters.monsters import Goblin
from .objects.terrain import basic as terrain
from .objects.items import _weapons
# from .display

class MainStarter:
	def __init__(self):
		# Internals
		self.display = Display()
		self.seed_points: List[Point] = []
		# Game
		self.board = Board()
		self.hero = Player("Tim")
		self.enemy = Player("Hobo")
		# Initializers
		self._initialize_players_characters()
		self._position_players()

	def __repr__(self) -> str:
		return str(self.board)

	def _seed_board_point(self) -> Point:
		"""Generates a Point from the board, assuring it's not already used in the board"""
		board_size = self.board.size - 1
		seed_point = Point(randint(0, board_size), randint(0, board_size))
		if seed_point not in self.seed_points:
			self.seed_points.append(seed_point)
			return seed_point
		else:
			self._seed_board_point()

	def _initialize_players_characters(self) -> None:
		self.hero.set_character(Human())
		self.enemy.set_character(Goblin())

	def _initialize_terrain(self) -> None:
		rock = terrain.Rock()
		return [rock]

	def _position_players(self) -> None:
		self.hero.set_character_initial_position(self._seed_board_point())
		self.enemy.set_character_initial_position(self._seed_board_point())
		self.board.add_content(self.hero.character_position, self.hero)
		self.board.add_content(self.enemy.character_position, self.enemy)

	def show_board(self):
		print(self.board)

	def map_board(self):
		mapped = zip()
