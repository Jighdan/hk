from source.tools.graph import Point
from source.Board import Board
from source.Interface import Interface
from source.objects.characters.humans import Human
from source.objects.characters.goblins import Goblin

board = Board(6)
human = Human()
goblin = Goblin()
player_interface = Interface("Player", human.name, human.health, human.attack)

human_pos = Point(4, 2)
gob_pos = Point(1, 4)
board.add_content(human_pos, human)
board.add_content(gob_pos, goblin)

print(board)

gob_pos = board.call_auto_character(gob_pos, human_pos)
print(board)

gob_pos = board.call_auto_character(gob_pos, human_pos)
print(board)
gob_pos = board.call_auto_character(gob_pos, human_pos)
print(board)

gob_pos = board.call_auto_character(gob_pos, human_pos)
print(board)

gob_pos = board.call_auto_character(gob_pos, human_pos)
print(board)
