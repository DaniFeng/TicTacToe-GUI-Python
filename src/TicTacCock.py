'''
Created on Nov 14, 2018

@author: Dani
'''

#hey so this is really crappy and has a fuck ton of bugs, but I know too little about python to try to work with it
#so yeah Shiteng you deal with this now thanks
#for some reason after the first player input their move, the program keeps asking that same player to input 
#and then after the second input, there's an error. The program is supposed to print out the current updated of the board after a player makes a move
#fix it pls

from pip._vendor.distlib.compat import raw_input
import random

#player 1 is X, player 2 is O
player1 = ""
player2 = ""
turn = True
board = [["1", "2", "3"], 
["4", "5", "6"],
["7", "8", "9"]]
spacesFilled = 0
 
    # prints out the rules of the game
def displayRules():
    print("The object of Tic Tac Toe is to get three in a row.")
    print("You play on a three by three game board.")
    print("One player uses 'X' and the other uses 'O' to make their move.")
    print("Players alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled.")
    print("-------------------------------------------------")
    print()
    # prompts user to input a location on the grid (labeled 1-9)
def inputMove():
        
    currentPlayer = player1
        
    if not turn:
        currentPlayer = player2
        
    move = raw_input(currentPlayer + ", enter where you want to put your move: ")
        
    while True:
        move = raw_input(currentPlayer + ", enter where you want to put your move: ")
        if not moveValid(move):
            print("that move is already taken, bitch")
            break
        
    return move
    
    # checks if location is valid on the grid
def moveValid(self, location):
    if location == "X" or location == "O" :
            return False
         
    for row in board:
        if location in row:
            return True
            
    return False
     
    # if a move is returned, it updates the Board with either an "X" or an "O" in the location specified by the player
def updateBoard(location):
    for row in board:
        for col in row: 
            if turn:
                col = "X"
                    
            else:
                col = "O"
                    
            turn = not turn
            return
     
    # displays the tic tac toe board
def displayBoard():
    for row in board:
        print(row)
                
    # checks if the whole board is completely occupied with moves, in that case, it is a draw
def isFull():        
    if spacesFilled == 9:
        return True
          
    return False

    # determines if there's a win, who's the winner, and returns a boolean on whether or not the game should end
def winner():
    if checkRows() or checkCols() or checkDiagonal():
        name = player1
            
        if(turn):
            name = player2

        print(name + " is the winner!")
                
        return True
            
    elif isFull():
        print("The game is a draw. You're both losers.")
        return True
            
    return False
        
     # checks each row for matching values to see if there's a win
def checkRows():
    for row in board:
        if row[0] == row[1] and row[0] == row [2]:
            return True

    return False     
        
    # checks each column for matching values to see if there's a win
def checkCols():
    i = 0
        
    while i < 3:
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return True

    return False
     
    # checks if there is a 3-way win diagonally both ways
def checkDiagonal():
            
        # first, checks from top right to bottom left
    value = board[0][0]       
    if(value.equals(board[1][1]) and value.equals(board[2][2])):
        return True
            
        # then checks from top left to bottom right
    value = board[0][2]      
    if(value.equals(board[1][1]) and value.equals(board[2][0])):
        return True
                        
    return False

       
#private method to determine who goes first. If returns true, player1 goes first
def p1GoesFirst():
    return (random.randint(0,2)) == 1

#start of the program       
print("heyyyy bitch wanna play some tic tac toe?!!?!?")

player1 = raw_input("Enter player 1 name: ")
player2 = raw_input("Enter player 2 name: ")

if p1GoesFirst() is True:
    temp = player1
    player1 = player2
    player2 = temp

displayRules()
        
while True: 
   
    displayBoard()

    while True:
        choice = inputMove()
        
        if moveValid(choice) is False:
            break
        
        else:
            spacesFilled = spacesFilled + 1
            
    updateBoard(choice)
    
    if winner() is False:
        break

displayBoard()
