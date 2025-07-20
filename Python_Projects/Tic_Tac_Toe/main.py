import random


def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
test_board = ['#','1','2','3','4','5','6','7','8','9']
display_board(test_board)


def user_selction():
    print("---Player1 selection---")
    symbol_selected = input("Enter one symbol either X or O: " ).upper()
    if symbol_selected == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_symbol(board, symbol, position):
    board[position] = symbol
    

def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def first_chance():
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print("!!!Welcome to Tic-Tac-Toe game!!!")

while True:
    new_board = [' '] * 10
    player1_symbol, player2_symbol = user_selction()
    turn = first_chance()
    
    print(f"{turn} goes first")
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'player1':
            
            display_board(new_board)
            position = player_choice(new_board)
            place_symbol(new_board, player1_symbol, position)
            
            if win_check(new_board, player1_symbol):
                display_board(new_board)
                print('Congratulations! You have won the game!')
                game_on = False
            
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player2'
        else:
            
            display_board(new_board)
            position = player_choice(new_board)
            place_symbol(new_board, player2_symbol, position)
            
            if win_check(new_board, player2_symbol):
                display_board(new_board)
                print('Player 2 has won!')
                game_on = False
                
            else:
                if full_board_check(new_board):
                    display_board(new_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player1'

    if not replay():
        break
            