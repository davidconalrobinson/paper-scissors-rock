# Unit tests for Player class.


# Imports.
from unittest.mock import patch
from unittest import TestCase
from src.player import Player


class PlayerTest(TestCase):
	"""
	Player unittest class.
	"""


	def __init__(self, *args, **kwargs):
		super(PlayerTest, self).__init__(*args, **kwargs)
		self.test_player=Player(name='')


	def test_set_name1(self):
		self.test_player.set_name(name='test_name')
		self.assertEqual(self.test_player.name, 'test_name')


	@patch('src.player.get_input', return_value='test_name')
	def test_set_name2(self, input):
		self.test_player.set_name(name=None)
		self.assertEqual(self.test_player.name, 'test_name')


	@patch('src.player.get_input', return_value='')
	def test_set_name3(self, input):
		self.test_player.set_name(name=None)
		self.assertRaises(ValueError)


	@patch('src.player.get_input', return_value='Paper')
	def test_make_move1(self, input):
		self.test_player.is_robot=False
		self.test_player.make_move()
		self.assertEqual(self.test_player.move, 'Paper')


	@patch('src.player.get_input', return_value='Scissors')
	def test_make_move2(self, input):
		self.test_player.is_robot=False
		self.test_player.make_move()
		self.assertEqual(self.test_player.move, 'Scissors')


	@patch('src.player.try_again', return_value='Rock')
	def test_make_move3(self, input):
		self.test_player.is_robot=False
		self.test_player.make_move()
		self.assertEqual(self.test_player.move, 'Rock')


	@patch('src.player.get_input', return_value='Cat')
	def test_make_move4(self, input):
		self.test_player.is_robot=False
		self.test_player.make_move()
		self.assertRaises(ValueError)
