# Round class.


class Round():
	"""
	Round class.
	"""


	def __init__(self, player1_name, player2_name, player1_move, player2_move):
		"""
		Initialise Round object.
		A round requires two players and two moves (one for each player).
		"""
		self.player1_name=player1_name
		self.player2_name=player2_name
		self.player1_move=player1_move
		self.player2_move=player2_move
		

	def calculate_result(self):
		"""
		Calculate the result of the round.
		The winner is determined by the following schema:
			- paper beats (wraps) rock
			- rock beats (blunts) scissors
			- scissors beats (cuts) paper
		"""
		result_schema={
			'Paper': {
				'Paper': {
					'result': 'Draw',
					'winner': None},
				'Scissors':  {
					'result': 'Scissors beats Paper - {player2} wins!'.format(player2=self.player2_name),
					'winner': self.player2_name},
				'Rock':  {
					'result': 'Paper beats Rock - {player1} wins!'.format(player1=self.player1_name),
					'winner': self.player1_name}
			},
			'Scissors': {
				'Paper':  {
					'result': 'Scissors beats Paper - {player1} wins!'.format(player1=self.player1_name),
					'winner': self.player1_name},
				'Scissors':  {
					'result': 'Draw',
					'winner': None},
				'Rock':  {
					'result': 'Rock beats Scissors - {player2} wins!'.format(player2=self.player2_name),
					'winner': self.player2_name}
			},
			'Rock': {
				'Paper':  {
					'result': 'Paper beats Rock - {player2} wins!'.format(player2=self.player2_name),
					'winner': self.player2_name},
				'Scissors':  {
					'result': 'Rock beats scissors - {player1} wins!'.format(player1=self.player1_name),
					'winner': self.player1_name},
				'Rock':  {
					'result': 'Draw',
					'winner': None}
			}
		}
		self.result=result_schema[self.player1_move][self.player2_move]['result']
		self.winner=result_schema[self.player1_move][self.player2_move]['winner']
		return self.result, self.winner
