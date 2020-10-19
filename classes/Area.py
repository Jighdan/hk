class Area:
	def __init__(self):
		self.contains = " "

	def __repr__(self):
		return self.contains

	def clear(self):
		self.contains = " "

	def update(self, payload):
		payload = " " if payload is None else payload
		self.contains = payload
