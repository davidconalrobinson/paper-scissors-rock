# Robot class.


# Imports.
import random
from src.player import Player


class Robot(Player):
	"""
	Robot class - a robot is a player that makes moves autonomously.
	Inherits Player class (i.e.: a robot is a player).
	"""


	def __init__(self, *args, move_model='simple_move_model', **kwargs):
		"""
		Initialise Robot object.
		By default, the robot class will invoke the simple_move_model to generate moves.
		The move model is designed to be a modular component that can be updated/swapped easily.
		"""
		super(Robot, self).__init__(*args, **kwargs)
		self.move_model=move_model


	def simple_move_model(self, prob_weighting={'Paper': 1, 'Scissors': 1, 'Rock': 1}):
		"""
		This simple move model will generate a move randomly.
		The probability of a given move being generated can be adjust using the prob_weighting dict.
		"""
		return random.choices(
			['Paper', 'Scissors', 'Rock'],
			weights=[prob_weighting['Paper'], prob_weighting['Scissors'], prob_weighting['Rock']],
			k=1)[0]


	# def another_mode_model(self, *args, **kwargs):
	# 	"""
	# 	We could define a series of different move models here, using different move algorithms.
	# 	"""
	# 	pass


	def make_move(self, *args, **kwargs):
		"""
		This over-writes the default Player make_move function, this will use a move model rather than a user input.
		This function is also a wrapper for the move model - this enables us to easily modularise the move algorithm and update/switch between different models.
		"""
		method_to_call=getattr(self, self.move_model)
		self.move=method_to_call(*args, **kwargs)
		return '{name} plays {move}'.format(name=self.name, move=self.move)
