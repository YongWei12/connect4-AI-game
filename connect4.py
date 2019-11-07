import  numpy as np


def create_board():
	board = np.zeros((6,7))
	return board

def drop_piece():
	pass


def is_valid_location():
	return board[5][col] ==0

def get_next_open_row():
	pass



board = create_board()
game_over = False
turn =0;

while not game_over:
	#Ask for player 1 input
	if turn == 0:
		col = input("Player 1 Make your Selection(0-6)")

	#Ask for Player 2 input
	else:
		col = input("Player 2 Make your selection(0-6)")

	turn = turn+ 1
	turn = turn%2
