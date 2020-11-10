class Inventory:
	def __init__(self):
		self.bag: dict = {}

	def __str__(self) -> str:
		formatted_items = [f"- {self.bag[_]['name']} x{str(self.bag[_]['quantity'])}" for _ in self.bag.keys()]
		return formatted_items.join("\n")

	def add(self, item, quantity = 1) -> None:
		# Checks if the item exists in the bag
		if self.bag[item.name]:
			self.bag[item.name][quantity] += 1
		else:
			self.bag[item.name] = {"quantity": quantity, item.name: item}

	def consume(self, item) -> None:
		self.bag[item.name][quantity] -= 1
		if not self.bag[item][quantity]:
			del self.bag[item]
