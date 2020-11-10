from . import BaseTerrain

class Rock(BaseTerrain):
	def __init__(self):
		super().__init__(icon="^", static=True, walk_over=False, color="yellow")


class Water(BaseTerrain):
	def __init__(self):
		super().__init__(icon="~", static=True, walk_over=False, color="blue")
