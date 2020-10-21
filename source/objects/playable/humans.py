from . import Playable

class Human(Playable):
	def __init__(self):
		super().__init__(name="@", health=10, attack=1, faction="Human")

