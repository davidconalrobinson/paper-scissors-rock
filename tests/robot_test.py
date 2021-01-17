# Unit tests for Robot class.


# Imports.
from unittest.mock import patch
from unittest import TestCase
from src.robot import Robot


class RobotTest(TestCase):
	"""
	Robot unittest class.
	"""


	def __init__(self, *args, **kwargs):
		super(RobotTest, self).__init__(*args, **kwargs)
		self.test_robot=Robot(name='my_robot')


	def test_simple_move_model1(self):
		move=self.test_robot.simple_move_model()
		self.assertTrue(move in ['Paper', 'Scissors', 'Rock'])


	def test_simple_move_model2(self):
		move=self.test_robot.simple_move_model(prob_weighting={'Paper': 1, 'Scissors': 0, 'Rock': 0})
		self.assertEqual(move, 'Paper')


	def test_simple_move_model3(self):
		move=self.test_robot.simple_move_model(prob_weighting={'Paper': 0, 'Scissors': 1, 'Rock': 0})
		self.assertEqual(move, 'Scissors')


	def test_simple_move_model4(self):
		move=self.test_robot.simple_move_model(prob_weighting={'Paper': 0, 'Scissors': 0, 'Rock': 1})
		self.assertEqual(move, 'Rock')


	def test_make_move1(self):
		self.test_robot.move_model='simple_move_model'
		self.test_robot.make_move()
		self.assertTrue(self.test_robot.move in ['Paper', 'Scissors', 'Rock'])


	def test_make_move2(self):
		self.test_robot.move_model='simple_move_model'
		self.test_robot.make_move(prob_weighting={'Paper': 1, 'Scissors': 1, 'Rock': 1})
		self.assertTrue(self.test_robot.move in ['Paper', 'Scissors', 'Rock'])
