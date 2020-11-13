from .. import BaseObject

class BaseItem:
	def __init__(self, item_section, object_key):
		self.object_key = object_key
		super().__init__(object_datafile="_items.json", object_key=object_key)

