from .. import BaseObject

class BaseTerrain(BaseObject):
	def __init__(self, icon: str, static: bool, walk_over: bool, color: str):
		super().__init__(icon=icon, color=color)
		self.static = True
		self.walk_over = False
		