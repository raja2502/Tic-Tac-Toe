#AI Project 1

import tic_tac_toe_utilities

tic_tac_toe_utilities.printMenu()
userChoice = int(input('Enter your choice : '))
if userChoice == 1:
    print("Level1 : Beginner")
    print("Level2 : Expert")
    level = int(input('Enter your choice \n 1: Level1 \n 2: Level2'))
    choiceLevel= level
    if choiceLevel == 1:
        tic_tac_toe_utilities.defaultBeginner()
    elif choiceLevel == 2:
        tic_tac_toe_utilities.defaultExpert()
    else:
        print("Please enter your choice again.Invalid Input")
elif userChoice == 2:
    print("Level1 : Beginner")
    print("Level2 : Expert")
    level = int(input('Enter your choice \n 1: Level1 \n 2: Level2'))
    choiceLevel = level
    if choiceLevel == 1:
        tic_tac_toe_utilities.board4Beginner()
    elif choiceLevel == 2:
        tic_tac_toe_utilities.board4Expert()
    else:
        print("Invalid Input, Enter again")
else:
    print("Invalid Input. Try again!")
