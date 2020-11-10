from . import BaseItem
from ...tools._json_read import JSON

BASE_FILE = "_potions.json"
DATA = JSON(BASE_FILE)

class BasePotion(BaseItem):
	def __init__(self, name, value):
		super().__init__(
			icon=DATA["icon"],
			color=DATA["color"],
			target_attribute=DATA["target_attribute"],
			name=name, value=value
		)

