from . import Playable

class Goblin(Playable):
	def __init__(self):
		super().__init__(icon="#", health=5, attack=1, faction="goblin")
