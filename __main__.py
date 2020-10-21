from source.tools import Point
from source.Board import Board
from source.Interface import Interface
from source.objects.playable.humans import Human
from source.objects.playable.goblins import Goblin

board = Board(6)
human = Human()
goblin = Goblin()
player_interface = Interface("Player", human.name, human.health, human.attack)
