from random import  randint
from .maps import board
from .players.humans import human_trainee, human_paladin
from .players.monsters import goblin_young
from .core.modules.board_interpreter import alpha_to_index, convert_alpha_to_point, convert_point_to_alpha
from .core.modules.graph import Point, AlphaPoint
from .core.display._text_box import TextBox
from .core.display._strings_templates import on_move

class Game:
	def __init__(self):
		self.board = board
		self.text_box = TextBox(text_history_size=3)
		self.players = [human_trainee, goblin_young]
		self._player_turn = True
		self._points_seed = []

		self._seed_map()
		self._set_characters_in_board()

	def _seed_map(self) -> list:
		board_size = self.board.size - 1
		while len(self._points_seed) != len(self.players):
			gen_point = Point(randint(0, board_size), randint(0, board_size))
			if gen_point not in self._points_seed:
				self._points_seed.append(gen_point)

	def _set_characters_in_board(self):
		for _ in range(len(self.players)):
			self.players[_].position = self._points_seed[_]
			self.players[_].position = self.board.add_content(self.players[_], self.players[_].position)

	def _switch_turn(self):
		self._player_turn = not self._player_turn

	def request_move(self):
		move= input()
		## This is wacky yo
		move = convert_alpha_to_point(AlphaPoint(move[0], move[-1]))
		if self._player_turn:
			self.text_box.add(on_move(payload=self.players[0], origin=self.players[0].position, target=move))
			self.players[0].position = board.move_content(self.players[0].position, move)
		elif not self._player_turn:
			self.players[-1].position = board.move_content(self.players[-1].position, move)


# human_trainee.position = board.move_content(human_trainee.position, Point(4, 5))
g = Game()
print(g.board)
print(g.text_box)

g.request_move()

print(g.board)
print(g.text_box)