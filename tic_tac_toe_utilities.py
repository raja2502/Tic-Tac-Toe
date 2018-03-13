import boardConfigurations
import rules
import random

#Menu
def printMenu():
    print('----------------------')
    print("   Tic Tac Toe Game     ")
    print('----------------------')
    print("1. User Vs Computer")
    print("2. 4 by 4 Grid")
    print("3. QUIT")
    print('----------------------')

#who first
def whoFirst():
    print(" who want to go first \n 1: you  \n 2: computer)")
    if int(input())== 1:
        return 'player'
    else:
        return 'computer'

#This gets the users choice of the Symbol (X or O)
def chosePlayerSymbol():
    letter = ''
    while not (letter == 1 or letter == 2):
        print('Do you want X(1) or O(2)?')
        letter = int(input())
    if letter == 1:
        return ['X', 'O']
    else:
        return ['O', 'X']
		
#check if user want to play again or not
def repeat():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


#Fill block
def makeMove(board, letter, move):
    board[move] = letter


#Players choice of move for 3 by 3 (default)
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not boardConfigurations.ifExistsFreeSpace(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


#Players move for 4 by 4 grid
def getPlayerMove4by4(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16'.split() or not boardConfigurations.ifExistsFreeSpace(board, int(move)):
        print('What is your next move? (1-16)')
        move = input()
    return int(move)


#Gets random move
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if boardConfigurations.ifExistsFreeSpace(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

#Gets the computers Move for 3 by 3 grid
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = boardConfigurations.getBoardCopy(board)
        if boardConfigurations.ifExistsFreeSpace(copy, i):
            makeMove(copy, computerLetter, i)
            if rules.ifWon3x3(copy, computerLetter):
                return i

    for i in range(1, 10):
        copy = boardConfigurations.getBoardCopy(board)
        if boardConfigurations.ifExistsFreeSpace(copy, i):
            makeMove(copy, playerLetter, i)
            if rules.ifWon3x3(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if boardConfigurations.ifExistsFreeSpace(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

#Gets the computers Move for 4 by 4
def getComputerMove4by4(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 17):
        copy = boardConfigurations.getBoardCopy(board)
        if boardConfigurations.ifExistsFreeSpace(copy, i):
            makeMove(copy, computerLetter, i)
            if rules.ifWon4x4(copy, computerLetter):
                return i

    for i in range(1, 17):
        copy = boardConfigurations.getBoardCopy(board)
        if boardConfigurations.ifExistsFreeSpace(copy, i):
            makeMove(copy, playerLetter, i)
            if rules.ifWon4x4(copy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 4, 13, 16])
    if move != None:
        return move

    move = chooseRandomMoveFromList(board, [6, 7, 10, 11])
    if move != None:
        return move

    return chooseRandomMoveFromList(board, [2, 3, 5, 9, 8, 12, 14, 15])


def getComputerMove4by4Exp(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    move = chooseRandomMoveFromList(board, [1, 4, 13, 16])
    if move != None:
        return move

    move = chooseRandomMoveFromList(board, [6, 7, 10, 11])
    if move != None:
        return move
    return chooseRandomMoveFromList(board, [2, 3, 5, 9, 8, 12, 14, 15])


def getComputerMoveExp(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if boardConfigurations.ifExistsFreeSpace(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

#This is an implementation for beginner level tic tac toe for 3 by 3 grid
def defaultBeginner():
    print(30 * '-')
    print("Welcome to beginner level of 3 by 3")
    print(30 * '-')
    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = chosePlayerSymbol()
        turn = whoFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                boardConfigurations.drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                if rules.ifWon3x3(theBoard, playerLetter):
                    boardConfigurations.drawBoard(theBoard)
                    print('You won!')
                    gameIsPlaying = False
                else:
                    if boardConfigurations.isBoardFull(theBoard):
                        boardConfigurations.drawBoard(theBoard)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'computer'

            else:
                move = getComputerMoveExp(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                if rules.ifWon3x3(theBoard, computerLetter):
                    boardConfigurations.drawBoard(theBoard)
                    print('The computer has beaten you! You lose')
                    gameIsPlaying = False
                else:
                    if boardConfigurations.isBoardFull(theBoard):
                        boardConfigurations.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

        if not repeat():
            break


#implementation of 3 by 3 Expert level
def defaultExpert():   
    print(30 * '-')
    print("Welcome to Expert level 3 by 3")
    print(30 * '-')
    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = chosePlayerSymbol()
        turn = whoFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                boardConfigurations.drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                if rules.ifWon3x3(theBoard, playerLetter):
                    boardConfigurations.drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if boardConfigurations.isBoardFull(theBoard):
                        boardConfigurations.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                if rules.ifWon3x3(theBoard, computerLetter):
                    boardConfigurations.drawBoard(theBoard)
                    print('You lose :( ')
                    gameIsPlaying = False
                else:
                    if boardConfigurations.isBoardFull(theBoard):
                        boardConfigurations.drawBoard(theBoard)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'player'

        if not repeat():
            break

def board4Beginner(): 
    print(30 * '-')
    print("Welcome to beginner level of 4 by 4")
    print(30 * '-')
    while True:
        theBoard = [' '] * 17
        playerLetter, computerLetter = chosePlayerSymbol()
        turn = whoFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                boardConfigurations.drawBoard4by4(theBoard)
                move = getPlayerMove4by4(theBoard)
                makeMove(theBoard, playerLetter, move)
                if rules.ifWon4x4(theBoard, playerLetter):
                    boardConfigurations.drawBoard4by4(theBoard)
                    print('You won')
                    gameIsPlaying = False
                else:
                    if boardConfigurations.isBoardFull(theBoard):
                        boardConfigurations.drawBoard4by4(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove4by4Exp(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                if rules.ifWon4x4(theBoard, computerLetter):
                    boardConfigurations.drawBoard4by4(theBoard)
                    print('You lose')
                    gameIsPlaying = False
                else:
                    if boardConfigurations.isBoardFull(theBoard):
                        boardConfigurations.drawBoard4by4(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
        if not repeat():
            break


def board4Expert():
    print(30 * '-')
    print("Welcome to 4 by 4 block")
    print(30 * '-')
    while True:
        theBoard = [' '] * 17
        playerLetter, computerLetter = chosePlayerSymbol()
        turn = whoFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                
                boardConfigurations.drawBoard4by4(theBoard)
                move = getPlayerMove4by4(theBoard)
                makeMove(theBoard, playerLetter, move)
                if rules.ifWon4x4(theBoard, playerLetter):
                    boardConfigurations.drawBoard4by4(theBoard)
                    print('you won')
                    gameIsPlaying = False
                else:
                    if boardConfigurations.isBoardFull(theBoard):
                        boardConfigurations.drawBoard4by4(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove4by4(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if rules.ifWon4x4(theBoard, computerLetter):
                    boardConfigurations.drawBoard4by4(theBoard)
                    print('You lose')
                    gameIsPlaying = False
                else:
                    if boardConfigurations.isBoardFull(theBoard):
                        boardConfigurations.drawBoard4by4(theBoard)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'player'
        if not repeat():
            break





