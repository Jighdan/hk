from ..tools.graph import Point
from ..tools.board_interpreter import alpha_to_index

def handle_board_position(payload: str) -> Point:
	"""Takes a string such as 'a2' or 'r17' and converts it to a graph point"""
	content = payload.strip().lower()
	x, y = content[:1], content[1:]
	return Point(alpha_to_index[x], int(y) - 1)
	