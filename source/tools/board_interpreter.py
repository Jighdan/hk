from string import ascii_lowercase
from .graph import Point

alphabet = list(ascii_lowercase)
index = [_ for _ in range(len(alphabet))]

alpha_to_index = {alphabet[_]: index[_] for _ in range(len(alphabet))}
