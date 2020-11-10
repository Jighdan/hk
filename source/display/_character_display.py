from typing import List

class CharacterLine:
	def __init__(self, name, icon, health):
		self.name = name
		self.icon = icon
		self.health = health

	def __repr__(self) -> str:
		return f"- {self.icon} / {self.name} / HP: {str(self.health)}"

# class CharacterDisplay:
# 	def __init__(self, characters: List):
# 		self.characters = characters

# 	def __str__(self) -> str:
# 		return "\n".join([CharacterLine(_.name, ) for _ in self.characters])
