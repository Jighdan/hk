from . import Playable

class Goblin(Playable):
	def __init__(self):
		super().__init__(name="#", health=5, attack=1, faction="Goblin")
