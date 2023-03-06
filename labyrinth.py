'''
#First Map
game = [[0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''

'''
#Second Map
game = [[" ", "0", "0", "0", "0", "0", " ", " ", " ", " "],
        [" ", "0", " ", " ", " ", " ", " ", "0", "0", "0"],
        [" ", "0", "0", "0", "0", "0", " ", "0", " ", " "],
        [" ", " ", " ", "0", " ", "0", " ", "0", "0", " "],
        [" ", "0", "0", "0", " ", "0", " ", " ", " ", " "],
        [" ", " ", " ", "0", " ", " ", " ", "0", "0", "0"],
        [" ", "0", "0", "0", " ", "0", "0", "0", " ", "0"],
        [" ", "0", " ", "0", " ", " ", " ", " ", " ", "0"],
        [" ", "0", " ", "0", "0", "0", "0", " ", "0", "0"],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
'''

#Choose characters to mark the walls and empty spaces the player can move into
emptySpace = " "
wall = "O"

#When player finishes this becomes true
finished = False

#Player and End marker
playerMarker = "p"
endMarker = "F"



#Adds possible horizontal moves to a list (possibleMoves)
def moveColumn(gameboard, currentRow, currentColumn, possibleMoves):
    if currentColumn <= len(game[currentColumn]) - 2 and currentColumn >= 1:
        if gameboard[currentRow][currentColumn + 1] == emptySpace or gameboard[currentRow][currentColumn + 1] == endMarker:
                possibleMoves.append("r")
        if gameboard[currentRow][currentColumn - 1] == emptySpace or gameboard[currentRow][currentColumn - 1] == endMarker:
                possibleMoves.append("l")
    #Player is on the right wall
    elif currentColumn == len(game[currentColumn]) - 1:
        if gameboard[currentRow][currentColumn - 1] == emptySpace or gameboard[currentRow][currentColumn - 1] == endMarker:
                possibleMoves.append("l")
    #Player is on the left wall
    else:
        if gameboard[currentRow][currentColumn + 1] == emptySpace or gameboard[currentRow][currentColumn + 1] == endMarker:
                possibleMoves.append("r")


#Adds possible vertical moves to a list
def moveRow(gameboard, currentRow, currentColumn, possibleMoves):
    if currentRow <= len(game[currentRow]) - 2 and currentRow >= 1:
        if gameboard[currentRow - 1][currentColumn] == emptySpace or gameboard[currentRow - 1][currentColumn] == endMarker:
                possibleMoves.append("u")
        if gameboard[currentRow + 1][currentColumn] == emptySpace or gameboard[currentRow + 1][currentColumn] == endMarker:
                possibleMoves.append("d")
    #Player is on the bottom wall
    elif currentRow == len(game[currentRow]) - 1:
        if gameboard[currentRow - 1][currentColumn] == emptySpace or gameboard[currentRow - 1][currentColumn] == endMarker:
                possibleMoves.append("u")
    #Player is on the top wall
    else:
        if gameboard[currentRow + 1][currentColumn] == emptySpace or gameboard[currentRow + 1][currentColumn] == endMarker:
                possibleMoves.append("d")


#This function displays the gameboard
def displayGame(gameboard):
    for x in gameboard:
        print(x)


#Checks if player won
def win(gameboard, currentRow, currentColumn):
    if gameboard[currentRow][currentColumn] == endMarker:
        return True


#Player chooses next move
def playerChoice (gameboard, currentRow, currentColumn, possibleMoves):
    validMove = False
    #Ensure player enters a possible move
    while not validMove:
        choice = str(input("Please enter a letter from above: "))
        print()
        for x in possibleMoves:
            if choice == x:
                validMove = True
    #Check if player wins and move player marker after each move
    if choice == "u":
        gameboard[currentRow][currentColumn] = emptySpace
        currentRow = currentRow - 1
        if win(gameboard, currentRow, currentColumn):
            return endMarker
        gameboard[currentRow][currentColumn] = playerMarker
        return "u"
    elif choice == "d":
        gameboard[currentRow][currentColumn] = emptySpace
        currentRow = currentRow + 1
        if win(gameboard, currentRow, currentColumn):
            return endMarker
        gameboard[currentRow][currentColumn] = playerMarker
        return "d"
    elif choice == "l":
        gameboard[currentRow][currentColumn] = emptySpace
        currentColumn = currentColumn - 1
        if win(gameboard, currentRow, currentColumn):
            return endMarker
        gameboard[currentRow][currentColumn] = playerMarker
        return "l"
    elif choice == "r":
        gameboard[currentRow][currentColumn] = emptySpace
        currentColumn = currentColumn + 1
        if win(gameboard, currentRow, currentColumn):
            return endMarker
        gameboard[currentRow][currentColumn] = playerMarker
        return "r"
    elif choice == "g":
        return "g"
    else:
        return "q"


#Start of the game
mapChoice = "0"
wins = 0
print("\nWelcome to the labyrinth.\nUp is 'u', down is 'd', left is 'l', right is 'r'.")
print(f"To display the gameboard, enter 'g'.\nYour current position is marked with'{playerMarker}'\n.")
while mapChoice != "3":
    valid = False
    print("What map would you like to play? (1/2)\n1. 10x10\n2. 20x20\n3. Quit\n")
    while not valid:
        mapChoice = str(input())
        if mapChoice == "1":
            #Starting coordinates
            xstart = 9
            ystart = 7
            xend = 1
            yend = 2

            #First Map, start (9, 7) end (1, 2) size 10x10
            game = [[emptySpace,wall,wall,wall,wall,wall,emptySpace,emptySpace,emptySpace,emptySpace],
                    [emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall,wall,wall],
                    [emptySpace,wall,wall,wall,wall,wall,emptySpace,wall,emptySpace,emptySpace],
                    [emptySpace,emptySpace,emptySpace,wall,emptySpace,wall,emptySpace,wall,wall,emptySpace],
                    [emptySpace,wall,wall,wall,emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace],
                    [emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,wall,wall,wall],
                    [emptySpace,wall,wall,wall,emptySpace,wall,wall,wall,emptySpace,wall],
                    [emptySpace,wall,emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall],
                    [emptySpace,wall,emptySpace,wall,wall,wall,wall,emptySpace,wall,wall],
                    [emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace]]
            mapKey = "u u l l l u u r r u u u u l l l l"
            valid = True
        elif mapChoice == "2":
            #Starting coordinates
            xstart = 5
            ystart = 19
            xend = 0
            yend = 11

            #Second Map, start (5, 19) end (0, 11) 20x20
            game = [[emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,wall,wall,emptySpace,emptySpace,emptySpace,emptySpace],
                    [emptySpace,wall,wall,wall,wall,wall,wall,wall,emptySpace,wall,wall,wall,wall,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,wall],
                    [emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,wall,emptySpace,emptySpace,wall,emptySpace,wall,wall,wall,wall,emptySpace,wall],
                    [emptySpace,wall,emptySpace,wall,wall,wall,emptySpace,wall,emptySpace,emptySpace,emptySpace,wall,wall,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall],
                    [emptySpace,wall,emptySpace,wall,emptySpace,wall,emptySpace,emptySpace,emptySpace,wall,wall,wall,wall,emptySpace,wall,wall,wall,emptySpace,wall,wall],
                    [emptySpace,emptySpace,emptySpace,wall,emptySpace,wall,wall,wall,wall,wall,emptySpace,emptySpace,wall,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace],
                    [emptySpace,wall,wall,wall,emptySpace,wall,wall,emptySpace,wall,emptySpace,emptySpace,wall,wall,wall,emptySpace,wall,emptySpace,wall,emptySpace,wall],
                    [emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,wall,wall,emptySpace,wall,emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace],
                    [emptySpace,wall,wall,wall,emptySpace,wall,wall,emptySpace,wall,emptySpace,wall,wall,emptySpace,wall,emptySpace,wall,emptySpace,wall,wall,emptySpace],
                    [emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,wall,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace],
                    [wall,wall,wall,wall,wall,wall,wall,emptySpace,wall,emptySpace,wall,emptySpace,wall,wall,emptySpace,wall,wall,wall,wall,emptySpace],
                    [emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace],
                    [emptySpace,wall,emptySpace,wall,emptySpace,wall,wall,wall,wall,wall,wall,wall,emptySpace,wall,wall,wall,emptySpace,wall,emptySpace,wall],
                    [emptySpace,wall,emptySpace,wall,emptySpace,wall,emptySpace,emptySpace,wall,emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall],
                    [wall,wall,emptySpace,wall,wall,wall,wall,emptySpace,emptySpace,emptySpace,wall,wall,wall,emptySpace,wall,wall,emptySpace,wall,emptySpace,emptySpace],
                    [emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace,wall,emptySpace,wall,wall,emptySpace],
                    [emptySpace,wall,wall,wall,emptySpace,wall,wall,emptySpace,wall,wall,wall,emptySpace,wall,wall,emptySpace,wall,emptySpace,wall,emptySpace,emptySpace],
                    [emptySpace,emptySpace,emptySpace,wall,emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,wall],
                    [emptySpace,wall,wall,wall,emptySpace,wall,wall,wall,wall,emptySpace,wall,wall,wall,emptySpace,wall,wall,wall,wall,emptySpace,emptySpace],
                    [emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,wall,emptySpace,emptySpace,emptySpace,wall]]
            mapKey = "l l l d d l l d d d d r r d d d d d d l l l l l\nu u l l u u u u l l u u l l l l l l l u u u u r\nr u u u r r r r d d r r u u u u r r r"
            valid = True
        elif mapChoice == "3":
            msg = "Good bye"
            finished = True
            valid = True
        else:
            print("Please enter a '1', '2' or '3'")

    if mapChoice != "3":
        #Starting position
        row = xstart
        column = ystart
        game[row][column] = playerMarker

        #End position
        endRow = xend
        endColumn = yend
        game[endRow][endColumn] = endMarker
        
    giveup = False
    while not finished:
        moves = []
        print(f"Your current position is ({row + 1}, {column + 1})")
        moveRow(game, row, column, moves)
        moveColumn(game, row, column, moves)
        print("Possible Moves: ", end = "")
        for x in moves:
            print(x, end = " ")
        print ("\nOther options: g (display gameboard) q (quit)")
        moves.append("g")
        moves.append("q")
        choice = playerChoice(game, row, column, moves)
        if choice == "u":
            row = row - 1
        elif choice == "d":
            row = row + 1
        elif choice == "l":
            column = column - 1
        elif choice == "r":
            column = column + 1
        elif choice == "g":
            displayGame(game)
            print()
        elif choice == "F":
            finished = True
            msg = "Congrats you found your way out!"
            wins = wins + 1
        else:
            finished = True
            giveup = True
            msg = "You'll get it next time."
    print(msg)
    if giveup == True:
        print(f"The correct path was:\n{mapKey}")
    finished = False
if wins != 0:
    print(f"Wins: {wins}")