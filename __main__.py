# Source Tools
from source.tools.graph import Point
from source.input.handlers import handle_board_position
# Source Objects
from source.objects.characters.humans import Human
from source.objects.characters.goblins import Goblin
# Source Main
from source.logic import TurnStack
from source.board import Board
from source.interface import Interface

board = Board(60)
human = Human()
goblin = Goblin()

human_pos = handle_board_position("a1")
gob_pos = handle_board_position("z26")
board.add_content(human_pos, human)
board.add_content(gob_pos, goblin)

print(board)

# gob_pos = board.call_auto_character(gob_pos, human_pos)
# print(board)

# gob_pos = board.call_auto_character(gob_pos, human_pos)
# print(board)
# gob_pos = board.call_auto_character(gob_pos, human_pos)
# print(board)

# gob_pos = board.call_auto_character(gob_pos, human_pos)
# print(board)

# gob_pos = board.call_auto_character(gob_pos, human_pos)
# print(board)
