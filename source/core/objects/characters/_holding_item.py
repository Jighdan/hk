class HoldingItem:
	def __init__(self):
		self.holding = None

	def __repr__(self):
		return self.holding

	def	set_holding(self, payload) -> None:
		self.holding = payload
