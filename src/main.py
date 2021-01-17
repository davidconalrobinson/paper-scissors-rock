# This is the main Python script
# Run this to start playing!


# Imports.
from src.game import Game
from src.helpers import get_input, try_again
from src.player import Player
from src.robot import Robot


def main():
	"""
	This is the main script.

	It will create one human player and one human player and will keep repeating games until the human player chooses to stop.
	"""
	print('\n##################################################\n### Welcome to the Paper, Scissors, Rock game! ###\n##################################################\n')
	# Create players.
	player1=Player()
	player2=Robot(name='Robot')
	# Set still playing flag to True - keep looping until the user chooses to stop playing.
	still_playing=True
	while(still_playing):
		# Start a new game.
		game=Game(player1=player1, player2=player2)
		print('') # Print empty line - makes output look better.
		# Check how many rounds to play.
		no_rounds=try_again(get_input, 'How many rounds would you like to play? ', is_numeric=True)
		print('\nLets play!')
		# Loop through rounds.
		for i in range(1, int(no_rounds)+1):
			print('\n--- Round {} ---'.format(i))
			player1_move, player2_move, result=game.play_one_round()
			print(player1_move)
			print(player2_move)
			print(result)
		# Tally results and find the overall winner.
		tally=game.tally_results()
		print('\n--- FINAL RESULT ---\n')
		print(tally)
		if game.tally[game.player1.name]['wins'] == game.tally[game.player2.name]['wins']:
			print('\nIt\'s a draw!')
		else:
			winner=game.player1.name if game.tally[game.player1.name]['wins'] > game.tally[game.player2.name]['wins'] else game.player2.name
			print('\n{player} wins the game!\n'.format(player=winner))
		# Check if the user wants to play again.
		still_playing=True if try_again(get_input, 'Would you like to play again? (enter "Yes" or "No") ', in_list=['Yes', 'No']) == 'Yes' else False


if __name__ == '__main__':
	main()
