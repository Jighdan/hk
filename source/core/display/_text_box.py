from typing import List
from collections import deque

class TextBox:
	def __init__(self, text_history_size: int, empty_template_length=5):
		self.text_history_size: int = text_history_size
		self.empty_template: str = f"- {'.' * empty_template_length}"
		self.text_box: deque = deque()
		self._initialize_text_box()

	def __repr__(self) -> str:
		return "\n".join(self.text_box)

	def _initialize_text_box(self) -> None:
		for _ in range(self.text_history_size):
			self.text_box.append(self.empty_template)

	def _format_text(self, payload: str) -> str:
		return f"- {payload}."

	def add(self, payload: str) -> None:
		self.text_box.append(self._format_text(payload))
		self.text_box.popleft()
