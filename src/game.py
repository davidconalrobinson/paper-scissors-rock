# Game class.


# Imports.
import pandas as pd
from src.helpers import get_input
from src.round import Round


class Game():
	"""
	Game class.

	A game is played between two players and can continue for n rounds.
	At any point in the game the scores can be tallied.
	"""


	def __init__(self, player1, player2):
		"""
		Initialise Game object.
		"""
		self.player1=player1
		self.player2=player2
		self.round_count=0
		self.winner_dict={}


	def count_one_round(self):
		"""
		Increment the round count.
		"""
		self.round_count+=1
		return self.round_count


	def play_one_round(self, verbose=False):
		"""
		Plays through one complete round. Each player makes a move and then the result of the round is computed.
		"""
		if verbose:
			print('\n--- Round {} ---'.format(self.round_count+1))
		self.count_one_round()
		player1_move=self.player1.make_move()
		player2_move=self.player2.make_move()
		round=Round(self.player1.name, self.player2.name, self.player1.move, self.player2.move)
		result, winner=round.calculate_result()
		self.winner_dict[self.round_count]=winner
		if verbose:
			print(player1_move)
			print(player2_move)
			print(result)


	def tally_results(self, verbose=False):
		"""
		Tallys the results from all the rounds to determine the overall winner.
		"""
		self.tally={
			self.player1.name: {
				'wins': 0,
				'draws': 0,
				'losses': 0
			},
			self.player2.name: {
				'wins': 0,
				'draws': 0,
				'losses': 0
			}
		}
		for key, value in self.winner_dict.items():
			self.tally[self.player1.name]['wins']+=1 if value == self.player1.name else 0
			self.tally[self.player1.name]['draws']+=1 if value is None else 0
			self.tally[self.player1.name]['losses']+=1 if value == self.player2.name else 0
			self.tally[self.player2.name]['wins']+=1 if value == self.player2.name else 0
			self.tally[self.player2.name]['draws']+=1 if value is None else 0
			self.tally[self.player2.name]['losses']+=1 if value == self.player1.name else 0
		if verbose:
			print('\n--- FINAL RESULT ---\n')
			tally_pretty=pd.DataFrame(self.tally).to_markdown()
			print(tally_pretty)
			if self.tally[self.player1.name]['wins'] == self.tally[self.player2.name]['wins']:
				print('\nIt\'s a draw!\n')
			else:
				winner=self.player1.name if self.tally[self.player1.name]['wins'] > self.tally[self.player2.name]['wins'] else self.player2.name
				print('\n{player} wins the game!\n'.format(player=winner))
