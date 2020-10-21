class BaseItem:
	def __init__(self, name, attributes):
		self.name = name
		self.attributes = attributes

class Sword(BaseItem):
	def __init__(self):
		self.id = {"target": "attack", "value": 2}
		super().__init__("Sword", self.id)
