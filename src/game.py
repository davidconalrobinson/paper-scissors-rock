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


	def play_one_round(self):
		"""
		Plays through one complete round. Each player makes a move and then the result of the round is computed.
		"""
		self.count_one_round()
		player1_move=self.player1.make_move()
		player2_move=self.player2.make_move()
		round=Round(self.player1.name, self.player2.name, self.player1.move, self.player2.move)
		result, winner=round.calculate_result()
		self.winner_dict[self.round_count]=winner
		return player1_move, player2_move, result


	def tally_results(self):
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
		tally_df=pd.DataFrame(self.tally)
		return tally_df.to_markdown()
