from .tools import TextValue

class Interface:
	def __init__(self, title, name="?", health="?", attack="?", size=16):
		self.title = title
		self.name = TextValue("Name", str(name))
		self.health = TextValue("Health", str(health))
		self.attack = TextValue("Attack", str(attack))
		self.size = size + 4

	def __repr__(self):
		border = f"|{'-' * self.size}|"
		title = self._format_to_the_middle(self.title)
		name = self._format_to_the_left(f"{self.name.text}: {self.name.value}")
		health = self._format_to_the_left(f"{self.health.text}: {self.health.value}")
		attack = self._format_to_the_left(f"{self.attack.text}: {self.attack.value}")
		return "\n".join([border, title, border, name, health, attack, border])

	def _format_to_the_left(self, content):
		spaces = " " * (self.size - (len(content) + 1))
		return f"| {content}{spaces}|"

	def _format_to_the_middle(self, content):
		spaces = " " * int((self.size - len(content)) / 2)
		return f"|{spaces}{content}{spaces}|"
