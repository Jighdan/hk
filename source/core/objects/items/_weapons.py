from . import BaseItem

class BaseWeapon(BaseItem):
	def __init__(self, object_key: str):
		super().__init__(item_section="weapons", object_key=object_key)

wooden_sword = BaseWeapon("wooden_sword")
iron_sword = BaseWeapon("iron_sword")
