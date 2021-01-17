# Unit tests for round class.


# Imports.
from unittest.mock import patch
from unittest import TestCase
from src.round import Round


class RoundTest(TestCase):
	"""
	Round unittest class.
	"""


	def __init__(self, *args, **kwargs):
		super(RoundTest, self).__init__(*args, **kwargs)
		self.player1_name='Player 1'
		self.player2_name='Player 2'


	def test_calculate_result1(self):
		self.player1_move='Paper'
		self.player2_move='Paper'
		test_round=Round(self.player1_name, self.player2_name, self.player1_move, self.player2_move)
		result, winner=test_round.calculate_result()
		self.assertEqual(winner, None)


	def test_calculate_result2(self):
		self.player1_move='Paper'
		self.player2_move='Scissors'
		test_round=Round(self.player1_name, self.player2_name, self.player1_move, self.player2_move)
		result, winner=test_round.calculate_result()
		self.assertEqual(winner, self.player2_name)


	def test_calculate_result3(self):
		self.player1_move='Paper'
		self.player2_move='Rock'
		test_round=Round(self.player1_name, self.player2_name, self.player1_move, self.player2_move)
		result, winner=test_round.calculate_result()
		self.assertEqual(winner, self.player1_name)


	def test_calculate_result4(self):
		self.player1_move='Scissors'
		self.player2_move='Paper'
		test_round=Round(self.player1_name, self.player2_name, self.player1_move, self.player2_move)
		result, winner=test_round.calculate_result()
		self.assertEqual(winner, self.player1_name)


	def test_calculate_result5(self):
		self.player1_move='Scissors'
		self.player2_move='Scissors'
		test_round=Round(self.player1_name, self.player2_name, self.player1_move, self.player2_move)
		result, winner=test_round.calculate_result()
		self.assertEqual(winner, None)


	def test_calculate_result6(self):
		self.player1_move='Scissors'
		self.player2_move='Rock'
		test_round=Round(self.player1_name, self.player2_name, self.player1_move, self.player2_move)
		result, winner=test_round.calculate_result()
		self.assertEqual(winner, self.player2_name)


	def test_calculate_result7(self):
		self.player1_move='Rock'
		self.player2_move='Paper'
		test_round=Round(self.player1_name, self.player2_name, self.player1_move, self.player2_move)
		result, winner=test_round.calculate_result()
		self.assertEqual(winner, self.player2_name)


	def test_calculate_result8(self):
		self.player1_move='Rock'
		self.player2_move='Scissors'
		test_round=Round(self.player1_name, self.player2_name, self.player1_move, self.player2_move)
		result, winner=test_round.calculate_result()
		self.assertEqual(winner, self.player1_name)


	def test_calculate_result9(self):
		self.player1_move='Rock'
		self.player2_move='Rock'
		test_round=Round(self.player1_name, self.player2_name, self.player1_move, self.player2_move)
		result, winner=test_round.calculate_result()
		self.assertEqual(winner, None)
