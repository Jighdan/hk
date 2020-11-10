from .. import BaseObject

class BaseItem(BaseObject):
	def __init__(self, attributes: dict, icon: str, color: str):
		super().__init__(icon=icon, color=color)
		self.name, self.target_attribute, self.value = attributes

	def __repr__(self):
		return {
			"name": self.name,
			"target": self.target_attribute,
			"value": self.value
		}
