from ...modules.graph import Point
from .. import BaseObject

faction_colors = {
	"human": "white",
	"goblin": "green",
}

class BasePlayable(BaseObject):
	def __init__(self, icon: str, health: float, attack: float, faction: str):
		super().__init__(icon=icon, color=faction_colors[faction])
		self.alive: bool = True
		self.health = health
		self.attack = attack
		self.position: Point = None
		
	def _is_dead(self) -> bool:
		if self.health <= 0:
			return True

	def reduce_health(self, payload: float) -> None:
		self.health -= payload
		if self._is_dead():
			self.alive = False

	def update_position(self, payload: Point) -> Point:
		self.position = payload
		return self.position
