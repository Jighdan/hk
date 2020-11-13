from .. import BaseObject

class BaseTerrain(BaseObject):
	def __init__(self, icon: str, static: bool, walk_over: bool, color: str):
		super().__init__(icon=icon, color=color)
		self.static = True
		self.walk_over = False


class Rock(BaseTerrain):
	def __init__(self):
		super().__init__(icon="^", static=True, walk_over=False, color="yellow")


class Water(BaseTerrain):
	def __init__(self):
		super().__init__(icon="~", static=True, walk_over=False, color="blue")
