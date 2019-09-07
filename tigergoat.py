#!/usr/bin/python
 
import sys
 
baseNodeConnectB1 = {
        0 : [1, 2, 3],
        1 : [0, 2, 4],
        2 : [0, 1, 3, 5],
        3 : [0, 2, 6],
        4 : [1, 5, 7],
        5 : [2, 4, 6, 8],
        6 : [3, 5, 9],
        7 : [4, 8],
        8 : [5, 7, 9],
        9 : [6, 8],
        }
jumpNodeConnectB1 = {
        0 : [[1, 4], [2, 5], [3, 6]],
        1 : [[2, 3], [4, 7]],
        2 : [[5, 8]],
        3 : [[2, 1], [6, 9]],
        4 : [[1, 0], [5, 6]],
        5 : [[2, 0]],
        6 : [[5, 4], [3, 0]],
        7 : [[4, 1], [8, 9]],
        8 : [[5, 2]],
        9 : [[6, 3], [8, 7]],
        }
 
baseNodeConnectB2 = {
        0 : [1, 2, 3, 4, 5, 6],
        1 : [0, 2, 7],
        2 : [0, 1, 3, 8],
        3 : [0, 2, 4, 9],
        4 : [0, 3, 5, 10],
        5 : [0, 4, 6, 11],
        6 : [0, 5, 12],
        7 : [1, 8, 13],
        8 : [2, 7, 9, 14],
        9 : [3, 8, 10, 15],
        10 : [4, 9, 11, 16],
        11 : [5, 10, 12, 17],
        12 : [6, 11, 18],
        13 : [7, 14],
        14 : [8, 13, 15, 19],
        15 : [9, 14, 16, 20],
        16 : [10, 15, 17, 21],
        17 : [11, 16, 18, 22],
        18 : [12, 17],
        19 : [14, 20],
        20 : [15, 19, 21],
        21 : [16, 20, 22],
        22 : [17, 21],
        }
jumpNodeConnectB2 = {
        0 : [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11] , [6, 12]],
        1 : [[2, 3], [7, 13]],
        2 : [[3, 4], [8, 14]],
        3 : [[2, 1], [4, 5], [9, 15]],
        4 : [[3, 2], [5, 6], [10, 16]],
        5 : [[4, 3], [11, 17]],
        6 : [[5, 4], [12, 18]],
        7 : [[1, 0], [8, 9]],
        8 : [[2, 0], [9, 10], [14, 19]],
        9 : [[3, 0], [8, 7], [10, 11], [15, 20]],
        10 : [[4, 0], [9, 8], [11, 12], [16, 21]],
        11 : [[5, 0], [10, 9], [17, 22]],
        12 : [[6, 0], [11, 10]],
        13 : [[7, 1], [14, 15]],
        14 : [[8, 2], [15, 16]],
        15 : [[9, 3], [14, 13], [16, 17]],
        16 : [[10, 4], [15, 14], [17, 18]],
        17 : [[11, 5], [16, 15]],
        18 : [[12, 6], [17, 16]],
        19 : [[14, 8], [20, 21]],
        20 : [[15, 9], [21, 22]],
        21 : [[16, 10], [20, 19]],
        22 : [[17, 11], [21, 20]],
        }
 
boardID = 0
 
# Board 0 Settings
goatAvail = 5
goatsAlive = 5
 
gameState = [' '] * 10
gameState[0] = 'T'
tigerPos = [0]
goatPos = [-1] * goatAvail
 
baseNodeConnect = baseNodeConnectB1
jumpNodeConnect = jumpNodeConnectB1
 
def printBoard():
    if boardID == 0:
        print ('          '+"   | "+gameState[0]+'_0'+" | ")
        print ('---------------------------------')
        print ('      '+gameState[1]+'_1'+"   / "+gameState[2]+'_2'+"   \   "+gameState[3]+'_3')
        print ('---------------------------------')
        print ("    "+gameState[4]+'_4'+"    /  "+gameState[5]+'_5'+"    \   "+gameState[6]+'_6'+"        ")
        print ('---------------------------------')
        print ("  "+gameState[7]+'_7'+"     /   "+gameState[8]+'_8'+"     \   "+gameState[9]+'_9'+"            ")
        print ('---------------------------------')
        print (tigerPos)
        print (goatPos)
    else:
        #TODO: add display for other boards
        print('add display for other boards')
 
def isPosValid(posStr, animal):
    try:
        pos = [int(i) for i in posStr]
    except ValueError:
        return False
    print (pos)
    if len(pos) == 2:
        if pos[0] < 0 or pos[0] >= len(gameState) or \
           pos[1] < 0 or pos[1] >= len(gameState) or gameState[pos[1]] != ' ':
               return False
        if animal == 'G':
            if goatAvail != 0:
                return False
            if not pos[0] in goatPos:
                return False
            if not pos[1] in baseNodeConnect[pos[0]]:
                return False
        elif animal == 'T':
            if not pos[0] in tigerPos:
                return False
            if not pos[1] in baseNodeConnect[pos[0]]:
                for i in range(len(jumpNodeConnect[pos[0]])):
                    if gameState[jumpNodeConnect[pos[0]][i][0]] == 'G' and \
                    jumpNodeConnect[pos[0]][i][1] == pos[1]:
                        return True
                return False
    elif len(pos) == 1:
        if animal != 'G' or goatAvail == 0:
            return False
        if pos[0] < 0 or pos[0] >= len(gameState) or gameState[pos[0]] != ' ':
            return False
    else:
        return False
    return True
 
def placeAnimal(posStr, animal):
    pos = [int(i) for i in posStr]
    gameState[pos[0]] = animal
 
def moveAnimal(posStr, animal):
    pos = [int(i) for i in posStr]
    if animal == 'G':
        gameState[pos[1]] = 'G'
        gameState[pos[0]] = ' '
    elif animal == 'T':
        if pos[1] in baseNodeConnect[pos[0]]:
            gameState[pos[1]] = 'T'
            gameState[pos[0]] = ' '   
        else:
            for i in range(len(jumpNodeConnect[pos[0]])):
                if jumpNodeConnect[pos[0]][i][1] == pos[1]:
                    global goatsAlive
                    gameState[pos[1]] = 'T'
                    gameState[pos[0]] = ' '
                    gameState[jumpNodeConnect[pos[0]][i][0]] = ' '
                    idx = goatPos.index(jumpNodeConnect[pos[0]][i][0])
                    goatPos[idx] = -1
                    goatsAlive -= 1
 
def tigerToMove():
    while(1):
        posStr = input('Tiger to Move :: ').split(',')
        if isPosValid(posStr, 'T'):
            global tigerPos
            moveAnimal(posStr, 'T')
            pos = [int(i) for i in posStr]
            idx = tigerPos.index(pos[0])
            tigerPos[idx] = pos[1]
            return
        else:
            print('invalid entry, retry')
 
def goatToMove():
    global goatAvail
    while(1):
        if goatAvail == 0:
            posStr = input('Goat to Move from (ID, ID):: ').split(',')
            if isPosValid(posStr, 'G'):
                moveAnimal(posStr, 'G')
                pos = [int(i) for i in posStr]
                idx = goatPos.index(pos[0])
                goatPos[idx] = pos[1]
                return
            else:
                print('invalid entry, retry')
        else:
            posStr = input('Goat to Place @ ID :: ').split(',')
            if isPosValid(posStr, 'G'):
                placeAnimal(posStr, 'G')
                pos = [int(i) for i in posStr]
                goatPos[(len(goatPos) - goatAvail)] = pos[0]
                goatAvail -= 1
                return
            else:
                print('invalid entry, retry')
 
def isGameOver():
    for j in range(len(tigerPos)):
        for i in range(len(baseNodeConnect[tigerPos[j]])):
            if gameState[i] == ' ':
                return False
    for j in range(len(tigerPos)):
        for i in range(len(jumpNodeConnect[tigerPos[j]])):
            if gameState[jumpNodeConnect[tigerPos[j]][i][1]] == ' ':
                return False
    return True
 
def pulimekha():
    """
    Tiger - Goat :-
 
    Rules for tigers:
 
    They can move to an adjacent free position along the lines.
    1. They can capture goats during any move, and do not need to wait until all
    goats are placed.
    2. They can capture only one goat at a time.
    3. They can jump over a goat in any direction, as long as there is an open
    space for the tiger to complete its turn.
    4. A tiger cannot jump over another tiger.
 
    The goats must move according to these rules:
 
    1. Goats cannot move until all goats have been positioned on the board.
    2. They must leave the board when captured.
    3. They cannot jump over tigers or other goats.
 
    The game is over when either, the tigers capture 'n' goats, or the goats
    have blocked the tigers from being able to move.
   
    Board 1:
               O
           /   |   \
          1____2____3
         /     |     \
        4______5______6
       /       |       \
      7________8________9
     
      TODO:
      Board 2:
                      O
           /    /   /   \   \   \
          1____2___3____4____5____6
         /    /    |    |     \     \
        7_____8____9____10_____11____12
       /     /     |    |       \     \
      13____14____15____16_____17_____18
            |      |     |      |
            19____20____21_____22
    """
    print ('welcome to Tiger - Goat')
    global boardID
    if len(sys.argv) == 2:
        boardID = int(sys.argv[1])
    # Board 1 Settings
    if boardID != 0:
        global goatAvail
        global goatsAlive
        global gameState
        global tigerPos
        global goatPos
        global baseNodeConnect
        global jumpNodeConnect
       
        goatAvail = 20
        goatsAlive = 20
        gameState = [' '] * 23
        gameState[0] = 'T'
        gameState[3] = 'T'
        gameState[4] = 'T'
        tigerPos = [0, 3, 4]
        goatPos = [-1] * goatAvail
        baseNodeConnect = baseNodeConnectB2
        jumpNodeConnect = jumpNodeConnectB2
    while(isGameOver() == False):
        printBoard()
        goatToMove()
        if isGameOver():
            print ('GOATS WON')
            break
        printBoard()
        tigerToMove()
        if goatsAlive < 4:
            print ('TIGER(s) WON')
            break
 
if __name__ == '__main__':
    pulimekha()
