import json
import os

class JSON:
	def __init__(self, filename):
		self.file = os.path.join(os.getcwd(), filename)

	def __repr__(self):
		with open(self.file) as f:
			content = json.load(f)
			return content
