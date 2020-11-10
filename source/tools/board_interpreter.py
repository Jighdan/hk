from string import ascii_lowercase
from collections import namedtuple
from .graph import Point, AlphaPoint

alphabet = list(ascii_lowercase)
index = [_ for _ in range(len(alphabet))]

alpha_to_index = {alphabet[_]: index[_] for _ in range(len(alphabet))}

def convert_alpha_to_point(payload: AlphaPoint) -> Point:
	return Point(alpha_to_index[payload.alpha], int(payload.index) - 1)

def convert_point_to_alpha(point: Point) -> AlphaPoint:
	return AlphaPoint(alphabet[point.x], str(point.y - 1))
