'''

                                                       Created by Jeet Patel
                                                         October 17, 2016

'''



import turtle
import math

s = turtle.Screen()
boardTurtle = turtle.Turtle()

XTurtle = turtle.Turtle()
OTurtle = turtle.Turtle()
winTurtle = turtle.Turtle()


winTurtle.color('yellow')
winTurtle.width(3)

board = [0,1,2,3,4,5,6,7,8]
playerNames = ()
cellSize = 100
uoCell = []

boardTurtle.ht()
OTurtle.ht()
XTurtle.ht()
winTurtle.ht()

cor = {}

counter = 0
'''
board = [0,1,2,3,4,5,6,7,8]
playerNames = ()
cellSize = 100
uoCell = []
'''
def assignCor(cor):
    cor[0] = [-cellSize, cellSize, 0, 0]
    cor[1] = [0, cellSize, 0, 0]
    cor[2] = [cellSize, cellSize, 0, 0]
    cor[3] = [-cellSize, 0, 0, 0]
    cor[4] = [0, 0, 0, 0]
    cor[5] = [cellSize, 0, 0, 0]
    cor[6] = [-cellSize, -cellSize, 0, 0]
    cor[7] = [0, -cellSize, 0, 0]
    cor[8] = [cellSize, -cellSize, 0, 0]


def reset(cor):
    
    boardTurtle.clear()
    XTurtle.clear()
    OTurtle.clear()
    winTurtle.clear()

    boardTurtle.reset()
    XTurtle.reset()
    OTurtle.reset()
    winTurtle.reset()


    winTurtle.width(3)
    XTurtle.width(3)
    OTurtle.width(3)

    XTurtle.color('red')
    OTurtle.color('blue')
    winTurtle.color('yellow')

    boardTurtle.ht()
    XTurtle.ht()
    OTurtle.ht()
    winTurtle.ht()

    cor.clear()

    del uoCell[:]
    

    
########################################################################################################

def playTTT(boardTurtle, XTurtle, OTurtle, cellSize, board, winTurtle, counter, cor):
    
    assignCor(cor)    
    playerNames = tuple(getPlayerNames())                   #   getPlayerNames()
    drawBoard(boardTurtle,cellSize)                         #   drawBoard()
    turns = []

    turnAsking = input("Who wants to play first? First letter capital. ")

    while turnAsking not in playerNames:
        print("This player is not playing. Please try again.")
        turnAsking = input("Who wants to play first? First letter capital. ")

    if turnAsking.lower() == playerNames[0].lower():
        for i in range(1,10):
            temp = i % 2
            turns.append(temp)
    elif turnAsking.lower() == playerNames[1].lower():
        for i in range(1,10):
            temp = i % 2
            if temp == 1:
                turns.append(0)
            elif temp == 0:
                turns.append(1)
        
    
    for turn in turns:
        if turn == 1:
            temp = print(getMove(board))         #getMove called to see which cells are available for the player
            turnValue = int(input(playerNames[0] + ", select the cell number from the above list: "))
            
            while turnValue not in uoCell:
                print("This cell is already occupied. Please select another cell.")
                turnValue = int(input(playerNames[0] + ", select the cell number from the above list: "))
            cor[turnValue][2] = 1
            cor[turnValue][3] = 'X'
            drawX(XTurtle, turnValue)
            result = gameOver(winTurtle)
            
            if result == 'X':
                print(playerNames[0] + ' wins!')
                goOn()
                break
            else:
                counter += 1
                if counter > 8: 
                    print("Game is a Draw!")
                    goOn()
                else:
                    pass
            
        elif turn == 0:
            temp = print(getMove(board))                    #  getMove()
            turnValue = int(input(playerNames[1] + ", select the cell number from the above list: "))
            
            while turnValue not in uoCell:
                print("Selected cell not in list.")
                turnValue = int(input(playerNames[1] + ", select the cell number from the above list: "))
            cor[turnValue][2] = 1
            cor[turnValue][3] = 'O'
            drawO(OTurtle, turnValue)
            result = gameOver(winTurtle)
            
            if result == 'O':
                print(playerNames[1] + ' wins!')
                goOn()
                break
            else:
                counter += 1
                if counter > 8:
                    print("Game is a Draw!")
                    goOn()
                else:
                    pass
            
########################################################################################################    

def getPlayerNames():
    players = []
    players.append(input("Enter player X:"))
    players.append(input("Enter player O:"))
    return players

########################################################################################################

def drawBoard(t, cellSize):
    t.goto(0,0)
    t.setheading(0)
    t.up()
    t.forward(cellSize/2)
    t.left(90)
    t.forward(cellSize * 1.5)
    t.left(90)
    
    for i in range(2):
        for j in range(4):
            
            if j%2 == 0:
                t.up()
                t.forward(cellSize)
                t.left(90)
                
            else:
                t.down()
                t.forward(cellSize * 3)
                t.left(90)
        t.up()
        t.forward(cellSize * 2)
        t.left(90)
        t.forward(cellSize)
    

        
######################################################################################################################        

def drawX(t, cell):
    t.up()
    t.goto(cor[cell][0],cor[cell][1])
    drawMidline(t, cellSize)

def drawMidline(t,length):
    t.width(3)
    t.color('red')
    t.down()
    t.left(45)
    t.forward(length/4)
    t.backward(length/2)
    t.forward(length/4)
    t.left(90)
    t.forward(length/4)
    t.backward(length/2)
    t.setheading(0)
    t.color('black')
    t.width(1)


######################################################################################################################

    
def drawO(t, cell):
    t.up()
    t.goto(cor[cell][0],cor[cell][1])
    t.setheading(0)
    drawConcentric(t, cellSize)

def drawConcentric(t, radius):
    t.width(3)
    t.color('blue')
    t.right(90)
    t.forward(radius/4)
    t.left(90)
    t.down()
    t.circle(radius/4)
    t.setheading(0)
    t.color('black')
    t.width(1)

###################################################################################################################### 

def getMove(board):
    del uoCell[:]
    
    for cell in board:
        if cor[cell][2]== 0:
            uoCell.append(cell)
            
    return uoCell

###################################################################################################################### 

def gameOver(t):
    t.setheading(0)
    
    for i in range(9):
        
        if (cor[0][3] == 'X' and cor[1][3] == 'X' and cor[2][3] == 'X'):
            t.up()
            t.goto(cor[0][0],cor[0][1])
            t.down()
            t.forward(cellSize*2)
            return 'X'
        elif (cor[0][3] == 'O' and cor[1][3] == 'O' and cor[2][3] == 'O'):
            t.up()
            t.goto(cor[0][0],cor[0][1])
            t.down()
            t.forward(cellSize*2)
            return 'O'


        
        elif (cor[3][3] == 'X' and cor[4][3] == 'X' and cor[5][3] == 'X'):
            t.up()
            t.goto(cor[3][0],cor[3][1])
            t.down()
            t.forward(cellSize*2)
            return 'X'
        elif (cor[3][3] == 'O' and cor[4][3] == 'O' and cor[5][3] == 'O'):
            t.up()
            t.goto(cor[3][0],cor[3][1])
            t.down()
            t.forward(cellSize*2)
            return 'O'



        elif (cor[6][3] == 'X' and cor[7][3] == 'X' and cor[8][3] == 'X'):
            t.up()
            t.goto(cor[6][0],cor[6][1])
            t.down()
            t.forward(cellSize*2)
            return 'X'
        elif (cor[6][3] == 'O' and cor[7][3] == 'O' and cor[8][3] == 'O'):
            t.up()
            t.goto(cor[6][0],cor[6][1])
            t.down()
            t.forward(cellSize*2)
            return 'O'
        

        
        elif (cor[0][3] == 'X' and cor[3][3] == 'X' and cor[6][3] == 'X'):
            t.up()
            t.goto(cor[0][0],cor[0][1])
            t.down()
            t.right(90)
            t.forward(cellSize*2)
            return 'X'
        elif (cor[0][3] == 'O' and cor[3][3] == 'O' and cor[6][3] == 'O'):
            t.up()
            t.goto(cor[0][0],cor[0][1])
            t.down()
            t.right(90)
            t.forward(cellSize*2)
            return 'O'



        elif (cor[1][3] == 'X' and cor[4][3] == 'X' and cor[7][3] == 'X'):
            t.up()
            t.goto(cor[1][0],cor[1][1])
            t.down()
            t.right(90)
            t.forward(cellSize*2)
            return 'X'
        elif (cor[1][3] == 'O' and cor[4][3] == 'O' and cor[7][3] == 'O'):
            t.up()
            t.goto(cor[1][0],cor[1][1])
            t.down()
            t.right(90)
            t.forward(cellSize*2)
            return 'O'



        elif (cor[2][3] == 'X' and cor[5][3] == 'X' and cor[8][3] == 'X'):
            t.up()
            t.goto(cor[2][0],cor[2][1])
            t.down()
            t.right(90)
            t.forward(cellSize*2)
            return 'X'
        elif (cor[2][3] == 'O' and cor[5][3] == 'O' and cor[8][3] == 'O'):
            t.up()
            t.goto(cor[2][0],cor[2][1])
            t.down()
            t.right(90)
            t.forward(cellSize*2)
            return 'O'


        
        elif (cor[0][3] == 'X' and cor[4][3] == 'X' and cor[8][3] == 'X'):
            t.up()
            t.goto(cor[0][0],cor[0][1])
            t.down()
            t.right(45)
            t.forward(2*(math.sqrt(2*((cellSize)**2))))
            return 'X'
        elif (cor[0][3] == 'O' and cor[4][3] == 'O' and cor[8][3] == 'O'):
            t.up()
            t.goto(cor[0][0],cor[0][1])
            t.down()
            t.right(45)
            t.forward(2*(math.sqrt(2*((cellSize)**2))))
            return 'O'


        
        elif (cor[2][3] == 'X' and cor[4][3] == 'X' and cor[6][3] == 'X'):
            t.up()
            t.goto(cor[2][0],cor[2][1])
            t.down()
            t.right(135)
            t.forward(2*(math.sqrt(2*((cellSize)**2))))
            return 'X'
        elif (cor[2][3] == 'O' and cor[4][3] == 'O' and cor[6][3] == 'O'):
            t.up()
            t.goto(cor[2][0],cor[2][1])
            t.down()
            t.right(135)
            t.forward(2*(math.sqrt(2*((cellSize)**2))))
            return 'O'


######################################################################################################################

def goOn():
    answer = input("Do you want to continue playing? Yes or NO : ")
    ans = answer.lower()
    if ans == 'yes':
        reset(cor)
        playTTT(boardTurtle, XTurtle, OTurtle, cellSize, board, winTurtle, counter, cor)
    elif ans == 'no':
        print('Thank you for playing.')
        s.bye()
        
######################################################################################################################

playTTT(boardTurtle, XTurtle, OTurtle, cellSize, board, winTurtle, counter, cor)

