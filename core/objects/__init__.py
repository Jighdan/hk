# from json import load
# from os import path, getcwd
from termcolor import colored

# class JSON:
# 	def __init__(self, filename):
# 		self.file = path.join(getcwd(), "source/objects/data/", filename)

# 	def __repr__(self):
# 		with open(self.file) as f:
# 			content = load(f)
# 			print(content)
# 			return dict(content)


class BaseObject:
	def __init__(self, icon, color):
		# self.general_data = JSON(object_datafile)
		# print(self.general_data)
		# self.object_key = object_key
		self.icon = icon
		self.color = color

	def __str__(self):
		return colored(self.icon, self.color)

	# def get_object_data(self) -> dict:
	# 	return self.general_data["components"][self.object_key]

	# def get_item_data(self) -> dict:
	# 	item_data: dict = self.get_object_data()
	# 	data = {
	# 		"target_attribute": self.general_data["target_attribute"],
	# 		"name": item_data["name"],
	# 		"value": item_data["value"]
	# 	}
	# 	return data
