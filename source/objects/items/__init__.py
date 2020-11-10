from .. import BaseObject

class BaseItem(BaseObject):
	def __init__(self, icon: str, color: str, name: str, target_attribute: str, value: float):
		super().__init__(icon=icon, color=color)
		self.name = name
		self.target_attribute = target_attribute
		self.value = value

	def __str__(self):
		return self.name
