from numpy import *
from random import randint

def main():
    gameBoard = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    flower = [random.randint(0,4), random.randint(0,4)]
    gameBoard[flower[0]][flower[1]] = "F"
    kangaroo = [0,0]
    gameBoard[kangaroo[0]][kangaroo[1]] = "Kan"
    
    for i in gameBoard:
        print(i)
    
    gameBoard[kangaroo[0]][kangaroo[1]] = "0"
    hopToFlower(gameBoard)
    hopToPlantFlower(gameBoard)
        
def hopKan(board):
    colHop = int(input("column wanted (0-4): "))
    rowHop = int(input("row wanted (0-4): "))
    
    kangaroo = [rowHop,colHop]
    board[kangaroo[0]][kangaroo[1]] = "Kan"  
    
    for i in board:
        print(i)
    
    board[kangaroo[0]][kangaroo[1]] = "0"
        
def hopPlantFlower(board):
    rowHop = int(input("row for flower(0-4): "))
    colHop = int(input("coloumn for flower (0-4): "))
    
    flower = [rowHop,colHop]
    board[flower[0]][flower[1]] = "Flo"
    
    if(colHop + 1 <= 4):
        kangaroo = [rowHop, colHop + 1]
        board[kangaroo[0]][kangaroo[1]] = "Kan"
    elif(colHop - 1 >= 0):
        kangaroo = [rowHop, colHop-1]
        board[kangaroo[0]][kangaroo[1]] = "Kan"
        
    for i in board:
        print(i)
    
    
        
main()
