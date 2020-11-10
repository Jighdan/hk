from . import BaseItem

data = {
	"icon": "+",
	"color": "gray",
	"items": {
		"sword": {
			"name": "Sword",
			"target_attribute": "attack",
			"value": 2
		}
	}
}

class Sword(BaseItem):
	def __init__(self):
		super().__init__(icon=data["icon"], color=data["color"], attributes=data["items"]["sword"])
