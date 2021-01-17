# Player class.


# Imports.
from src.helpers import get_input, try_again


class Player():
	"""
	Player class.
	
	Players have a name and can make a move during a round.
	"""


	def __init__(self, name=None):
		"""
		Initialise Player object.
		"""
		self.set_name(name)


	def set_name(self, name):
		"""
		Set the player's name.

		If name == None, the user will be prompted to enter a name.
		"""
		name=try_again(get_input, 'Hello, what is your name? ') if name is None else name
		self.name=name


	def make_move(self):
		"""
		Make the player's move.
		"""
		move=try_again(get_input, '{name}, what move are you making? (enter "Paper", "Scissors" or "Rock") '.format(name=self.name), in_list=['Paper', 'Scissors', 'Rock'])
		self.move=move
		return '{name} plays {move}'.format(name=self.name, move=self.move)
		