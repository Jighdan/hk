from ..core.modules.graph import Point, Graph
from . import TemplateMap, rock, water

# Rocky slopes
rocky_slopes = TemplateMap(7)
rocky_slopes.add_square(Point(0, 4), rock)
rocky_slopes.add_square(Point(4, 2), rock)
rocky_slopes.add_square(Point(5, 5), rock)
