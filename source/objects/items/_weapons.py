from . import BaseItem
from ...tools._json_read import JSON

BASE_FILE = "_weapons.json"
DATA = JSON(BASE_FILE)

class BaseWeapon(BaseItem):
	def __init__(self, name, value):
		super().__init__(
			icon=DATA["icon"], 
			color=DATA["color"], 
			target_attribute=DATA["target_attribute"],
			name=name, value=value
		)


class WoodenSword(BaseWeapon):
	def __init__(self):
		self.item = "wooden_sword"
		super().__init__(name=self.item["name"], value=self.item["value"])


class IronSword(BaseWeapon):
	def __init__(self):
		self.item = "iron_sword"
		super().__init__(name=self.item["name"], value=self.item["value"])
