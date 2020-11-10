from collections import namedtuple
from typing import List

Point = namedtuple("Point", "x y")
AlphaPoint = namedtuple("AlphaPoint", "alpha index")

class Graph:
	def _distance_between(self, origin: Point, target: Point) -> float:
		"""Evaluates the distance between two points"""
		return float(abs(origin.x - target.x) + abs(origin.y - target.y))

	def _is_point_in_range(self, target: Point, limiter: float) -> bool:
		"""Checks if a point is within bounds"""
		x_check = target.x < limiter and target.x >= 0
		y_check = target.y < limiter and target.y >= 0
		return True if x_check and y_check else False

	def shortest_distance_from_set(self, set_of_points: List[Point], target: Point) -> Point:
		"""Returns the point from a set of points that is closest to a target point"""
		index_of_shortest = 0
		for index in range(0, len(set_of_points)):
			if _distance_between(set_of_points[index], target) < _distance_between(set_of_points[index_of_shortest], target):
				index_of_shortest = index
		return set_of_points[index_of_shortest]

	def adjacent_points(self, origin: Point, limiter: float) -> List[Point]:
		"""Returns adjacent points, if such points coincide with the limiter parameters"""
		up = Point(origin.x, origin.y - 1)
		down = Point(origin.x, origin.y + 1)
		left = Point(origin.x - 1, origin.y)
		right = Point(origin.x + 1, origin.y)
		return [point for point in [up, down, left, right] if _is_point_in_range(point, limiter)]
