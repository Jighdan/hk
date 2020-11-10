class Gold:
	def __init__(self, amount: float):
		self.amount: float = amount

	def __str__(self):
		return(str(round(self.amount, 2)))

	def __add__(self, payload: float):
		self.amount += payload

	def __sub__(self, payload: float):
		self.amount -= payload
