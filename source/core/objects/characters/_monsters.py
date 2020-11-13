from . import BasePlayable

class BaseMonster(BasePlayable):
	def __init__(self, icon, health, attack, faction):
		super().__init__(icon=icon, health=health, attack=attack, faction=faction)


class Goblin(BaseMonster):
	def __init__(self, health, attack):
		super().__init__(icon="g", health=health, attack=attack, faction="goblin")
