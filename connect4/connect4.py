import numpy as np


def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece():
    pass

def is_valid_location(board, col):
    pass

def get_next_open_row():
    pass



board = create_board()
print(board)
game_over = False
turn = 0

while not game_over: #initial state true not not
    #Ask for Player 1 input
    if turn == 0:
        col = int(input("Player 1 Make you Selection (0-6): "))
        print(selection)
        print(type(selection))
    else:
        col = int(input("Player 2 Make you Selection (0-6): "))
    #Ask for Player 2 input

    turn +=1
    turn = turn % 2
    