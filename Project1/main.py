from GamePlayer import GamePlayer
from TicTacToeGame import TicTacToeGame

tic_tac_toe = TicTacToeGame()
game_player = GamePlayer(tic_tac_toe)

input = input("Which algorithm do you want to play again?\n('m' for Minimax or 'a' for Alpha Beta Pruning or 'mh' for Minimax with help or 'ah'for Alpha Beta Pruning with help)\n")
if input == 'm':
    game_player.play_minimax()
elif input == 'a':
    game_player.play_alpha_beta()
elif input == 'mh':
    game_player.play_minimax_help()
elif input == 'ah':
    game_player.play_alpha_beta_help()