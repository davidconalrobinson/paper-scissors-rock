# Unit tests for Game class.


# Imports.
from unittest.mock import patch
from unittest import TestCase
from src.game import Game
from src.robot import Robot


class GameTest(TestCase):
	"""
	Game unittest class.
	"""


	def __init__(self, *args, **kwargs):
		super(GameTest, self).__init__(*args, **kwargs)
		player1=Robot(name='Player 1')
		player2=Robot(name='Player 2')
		self.test_game=Game(player1, player2)


	def test_count_one_round(self):
		self.test_game.round_count=0
		self.test_game.count_one_round()
		self.assertEqual(self.test_game.round_count, 1)


	def test_play_one_round1(self):
		self.test_game.round_count=0
		self.test_game.play_one_round()
		self.test_game.play_one_round()
		self.assertTrue(1 in self.test_game.winner_dict)
		self.assertTrue(self.test_game.winner_dict[1] in [self.test_game.player1.name, self.test_game.player2.name, None])
		self.assertTrue(2 in self.test_game.winner_dict)
		self.assertTrue(self.test_game.winner_dict[2] in [self.test_game.player1.name, self.test_game.player2.name, None])


	def test_tally_results1(self):
		self.test_game.round_count=0
		self.test_game.play_one_round()
		self.test_game.play_one_round()
		self.test_game.play_one_round()
		self.test_game.play_one_round()
		self.test_game.play_one_round()
		self.test_game.tally_results()
		self.assertTrue(self.test_game.player1.name in self.test_game.tally)
		self.assertTrue(self.test_game.player2.name in self.test_game.tally)
		self.assertEqual(sum(self.test_game.tally[self.test_game.player1.name].values()), self.test_game.round_count)
		self.assertEqual(sum(self.test_game.tally[self.test_game.player2.name].values()), self.test_game.round_count)
		self.assertEqual(self.test_game.tally[self.test_game.player1.name]['wins'], self.test_game.tally[self.test_game.player2.name]['losses'])
		self.assertEqual(self.test_game.tally[self.test_game.player1.name]['draws'], self.test_game.tally[self.test_game.player2.name]['draws'])
		self.assertEqual(self.test_game.tally[self.test_game.player1.name]['losses'], self.test_game.tally[self.test_game.player2.name]['wins'])
