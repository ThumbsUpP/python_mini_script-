
# function that can print out a board

from IPython.display import clear_output

board = [' ' for x in range(9)]

def display_board(board):
    
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("__|___|__")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("__|___|__")
    print(board[6]+" | "+board[7]+" | "+board[8])
    print("  |   |  ")
    


#function that can take in a player input and assign their marker as 'X' or 'O'

def player_input():
    while True:
        marker = input('choisis ton signe : \'O\' ou \'X\'')
        if marker == 'X' or marker == 'O':
            break
        print('Vérifie ton entrée ')
    return marker


#function that takes a marker and assigns it to the board
def place_marker(board, marker, position):
    board[position-1] = marker
    return board

#function that checks to see if that mark has won
def win_check(board,mark):
    winnerBoard = [board[0:3], board[3:6], board[6:9], [board[0],board[4],board[8]], board[2],board[4],board[6], [board[0],board[3],board[6]], [board[2],board[5],board[8]], [board[1],board[4],board[7]], [board[2],board[4],board[6]]]
    for i in winnerBoard:
        if i == [mark, mark, mark]:
            return True
    return False
 

# function that uses the random module to randomly decide which player goes first
import random

def choose_first():
    adi = input('Nom du premier joueur ? ')
    das = input('Nom du deuxième joueur ? ')
    player1, player2 = "", ""
    hasard = random.randint(0,100)
    if hasard >= 50:
        player1 = adi
        player2 = das
    else:
        player2 = adi
        player1 = das
    return player1, player2
    

#function that returns a boolean indicating whether a space on the board is freely available
def space_check(board, pos):
    if board[pos-1] == ' ':
        return True
    return False
    

#function that checks if the board is full and returns a boolean value
def full_board_check(board):
    if not ' ' in board:
        return True
    return False
    pass

#function that asks for a player's next position (1 to 9)

def player_choice(board):
    while True:
        
        while True:
            try:
                position = int(input("quelle position choisis-tu?"))
                if position > 0 and position < 10:
                    break
                print("Il n'y a que 9 cases hein !")
            except:
                print("un nombre entre 1 et 9 est attendu")
                
                
                
        if space_check(board, position):
            break
        else:
            print('Position déjà prise')       
    
    return position

#function that asks the player if they want to play again
def replay():
    while True:
        replay = input('Une autre partie ? y/n')
        if replay == 'y' or replay == 'n':
            if replay == 'y':
                return True
            else: 
                return False
        else:
            print('Tu dois répondre par yes or no')
            

#game logic 

print('Welcome to Tic Tac Toe!')

while True:
    board = [' ' for x in range(9)]
    player1, player2 = choose_first()

    
    print(player1," commence la partie")
    plr1, plr2 = player_input(), ""
    if plr1 == 'O':
        plr2 = 'X'
    else:
        plr2 = 'O' 
    position = 0
    
    while not full_board_check(board):
    
        #Player 1 Turn
        print(player1," à ton tour :")
        position = player_choice(board)
        place_marker(board, plr1, position)
        clear_output()
        display_board(board)
        if win_check(board,plr1):
            print(player1, "a gagné la partie")
            break
        
        
        
        # Player2's turn.
        if full_board_check(board):
            print('égalité...')
            break
        print(player2," à toi de jouer :")
        position = player_choice(board)
        place_marker(board, plr2, position)
        clear_output()
        display_board(board)
        if win_check(board,plr2):
            print(player2, "a gagné la partie")
            break
    
    if not replay():
        clear_output()
        print('Belle partie')
        break
    clear_output()
