class BaseItem:
	def __init__(self, name: str, target_attribute: str, value: float):
		self.name = name
		self.target_attribute = target_attribute
		self.value = value

class Sword(BaseItem):
	def __init__(self):
		super().__init__("Sword", "attack", 2)
