# Tic Tac Toe Game in Python

def print_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('--|---|--')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('--|---|--')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def check_win(board):
    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # vertical
        (0, 4, 8), (2, 4, 6) # diagonal
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != ' ':
            return True
    return False

def play_game():
    board = [' ']*9
    player = 'X'
    while True:
        print_board(board)
        move = input(f"Player {player}, enter your move (1-9): ")
        while not move.isdigit() or int(move) not in range(1, 10) or board[int(move)-1] != ' ':
            print("Invalid move. Please enter a number between 1 and 9 that is not already occupied.")
            move = input(f"Player {player}, enter your move (1-9): ")
        board[int(move)-1] = player
        if check_win(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if ' ' not in board:
            print_board(board)
            print("It's a tie!")
            break
        player = 'O' if player == 'X' else 'X'

if __name__ == '__main__':
    play_game()
