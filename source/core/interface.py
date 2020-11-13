from typing import List
from .modules import TextValue

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
		spaces = int((self.size - len(content)) / 2)
		return content.center(spaces)

class Display:
	def __init__(self):
		self.text_box: List[str] = ["- ...", "- ...", "- ..."]
		self.oldest_text: str = ""
		self.upcoming_text: str = ""

	def __repr__(self) -> str:
		return "\n".join(self.text_box)

	def _update_text_box(self) -> None:
		self.oldest_text = self.text_box.pop(0)
		self.text_box.append(self.upcoming_text)
		self.upcoming_text = ""

	def add_text(self, payload: str) -> None:
		self.upcoming_text = f"- {payload}"
		self._update_text_box()
