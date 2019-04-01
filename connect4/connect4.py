import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0 #checking if first row is not filled in collumn where piece is dropped

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
def print_board(board):
    print(np.flip(board, 0)) #rotating board (list) upsidedown

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT)


board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over: #initial state true not not
    #Ask for Player 1 input
    if turn == 0:
        col = int(input("Player 1 Make you Selection (0-6): "))

        if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
    
    #Ask for Player 2 input
    else:
        col = int(input("Player 2 Make you Selection (0-6): "))

        if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
    print_board(board) #invoking borad in upside down function
    turn +=1
    turn = turn % 2
    