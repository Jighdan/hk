from typing import List

class TurnStack:
	def __init__(self, players):
		self.players: List = players
		self.turn_stack: List = players
		self.current_turn = None

	def __repr__(self):
		return self.current_turn

	def _filter_alive_players(self):
		self.turn_stack = [_ for _ in self.players if _.alive]

	def move_turn_ahead(self):
		self._filter_alive_players()
		if self.current_turn == None or self.turn_stack[-1]:
			self.current_turn = self.turn_stack[0]
		else:
			index_of_next_turn: float = self.turn_stack.index(self.current_turn) + 1
			self.current_turn = self.turn_stack[index_of_next_turn]
