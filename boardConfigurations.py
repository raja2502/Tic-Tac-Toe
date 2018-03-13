#4 by 4 grid
def drawBoard4by4(board4by4):
    print(' ' + board4by4[13] + ' | ' + board4by4[14] + ' | ' + board4by4[15] + ' | ' + board4by4[16])
    print('*******************************')
    print(' ' + board4by4[9] + ' | ' + board4by4[10] + ' | ' + board4by4[11] + ' | ' + board4by4[12])
    print('*******************************')
    print(' ' + board4by4[5] + ' | ' + board4by4[6] + ' | ' + board4by4[7] + ' | ' + board4by4[8])
    print('*******************************')
    print(' ' + board4by4[1] + ' | ' + board4by4[2] + ' | ' + board4by4[3] + ' | ' + board4by4[4])

#3 by 3 grid
def drawBoard(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('*******************************')    
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('*******************************')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    

#Returns grid copy
def getBoardCopy(board):
    copyBoard = []
    for block in board:
        copyBoard.append(block)
    return copyBoard

#Checks availability of free space in grid
def ifExistsFreeSpace(board, pos):
    return board[pos]== ' '

# check if the board is full or not		
def isBoardFull(board):
    for block in range(1, 10):
        if ifExistsFreeSpace(board, block):
            return False
    return True
	
# check if the 4x4 board is full or not
def is4x4BoardFull(board):
    for block in range(1, 17):
        if ifExistsFreeSpace(board, block):
            return False
    return True
