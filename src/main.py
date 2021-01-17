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
	print('')
	print('##################################################')
	print('### Welcome to the Paper, Scissors, Rock game! ###')
	print('##################################################')
	print('')
	# Create players.
	player1=Player()
	player2=Robot(name='Robot')
	# Set still playing flag to True - keep looping until the user chooses to stop playing.
	still_playing=True
	while(still_playing):
		# Start a new game.
		game=Game(player1=player1, player2=player2)
		# Check how many rounds to play.
		print('') # Print a blank line to help with formating the output.
		no_rounds=try_again(get_input, 'How many rounds would you like to play? ', is_numeric=True)
		# Loop through rounds.
		for i in range(1, int(no_rounds)+1):
			game.play_one_round(verbose=True)
		# Tally results and find the overall winner.
		game.tally_results(verbose=True)
		# Check if the user wants to play again.
		still_playing=True if try_again(get_input, 'Would you like to play again? (enter "Yes" or "No") ', in_list=['Yes', 'No']) == 'Yes' else False


if __name__ == '__main__':
	main()
