from . import BaseTerrain

class Rock(BaseTerrain):
	def __init__(self):
		super().__init__(icon="%", static=True, walk_over=False, color="brown")

	def __repr__(self) -> str:
		return "A giant rock!"


class Water(BaseTerrain):
	def __init__(self):
		super().__init__(icon="~", static=True, walk_over=False, color="blue")

	def __repr__(self) -> str:
		return "Blue-ass water"
