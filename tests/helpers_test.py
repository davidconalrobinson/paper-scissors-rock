# Unit tests for helper functions.


# Imports.
from unittest.mock import patch
from unittest import TestCase
from src.helpers import get_input_sub_func, get_input, try_again


class HelpersTest(TestCase):
	"""
	Helper functions unittest class.
	"""


	@patch('tests.helpers_test.get_input_sub_func', return_value='test_input')
	def test_get_input_sub_func1(self, input):
		input_value=get_input_sub_func('')
		self.assertEqual(input_value, 'test_input')


	@patch('tests.helpers_test.get_input_sub_func', return_value='1234')
	def test_get_input_sub_func2(self, input):
		input_value=get_input_sub_func('')
		self.assertEqual(input_value, '1234')


	@patch('tests.helpers_test.get_input_sub_func', return_value='')
	def test_get_input_sub_func3(self, input):
		input_value=get_input_sub_func('')
		self.assertEqual(input_value, '')


	@patch('src.helpers.get_input_sub_func', return_value='test_input')
	def test_get_input1(self, input):
		input_value=get_input('')
		self.assertEqual(input_value, 'test_input')


	def test_try_again1(self, no_tries=1):
		def func(x):
			return x
		r=try_again(func, True)
		self.assertEqual(r, True)


	def test_try_again2(self, no_tries=1):
		def func(x):
			return x
		r=try_again(func, Exception())
		self.assertRaises(Exception)


	def test_try_again3(self, no_tries=2):
		def func(x):
			return x
		r=try_again(func, Exception())
		r=try_again(func, True)
		self.assertEqual(r, True)
