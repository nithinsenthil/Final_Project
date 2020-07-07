#The class(es) can be written here
from itertools import chain
import os

class Board(): #This class represents a game board
    def __init__(self):
        self.state = [[None] * 3] * 3   #We cannot just leave it empty because then we'll have index out of bounds exceptions to deal with elsewhere
    def getWinner(self):
        #These will be set to True upon encountering 3 in a row from X or O
        xWins = False
        oWins = False

        #First, check for vertical winners
        for x in range(3):
            potentialWinner = self.state[x][0]
            potentialWinnerHasWon = True    #This becomes false upon encountering an empty space or a space occupied by the other side
            for y in range(1, 3):
                if self.state[x][y] != potentialWinner:
                    potentialWinnerHasWon = False
            #If we have found a win, set the appropriate winner
            if potentialWinnerHasWon:
                if potentialWinner == 'X': xWins = True
                elif potentialWinner == 'O': oWins = True
                #It is possible for None to be marked as a winner if there are 3 empty spaces in a row. We don't care about that.

        #Next, check for horizontal winners. (Basically the same as above but with X and Y moved)
        for y in range(3):
            potentialWinner = self.state[0][y]
            potentialWinnerHasWon = True    #This becomes false upon encountering an empty space or a space occupied by the other side
            for x in range(1, 3):
                if self.state[x][y] != potentialWinner:
                    potentialWinnerHasWon = False
            #If we have found a win, set the appropriate winner
            if potentialWinnerHasWon:
                if potentialWinner == 'X': xWins = True
                elif potentialWinner == 'O':
                    oWins = True
                # It is possible for None to be marked as a winner if there are 3 empty spaces in a row. We don't care about that.

        #Finally, check the diagonals
        potentialWinner = self.state[0][0]
        potentialWinnerHasWon = True    #This becomes false upon encountering an empty space or a space occupied by the other side
        for i in range(1, 3):
            if self.state[i][i] != potentialWinner:
                potentialWinnerHasWon = False
        #If we have found a win, set the appropriate winner
        if potentialWinnerHasWon:
            if potentialWinner == 'X': xWins = True
            elif potentialWinner == 'O':
                oWins = True
            # It is possible for None to be marked as a winner if there are 3 empty spaces in a row. We don't care about that.
        potentialWinner = self.state[2][0]
        potentialWinnerHasWon = True    #This becomes false upon encountering an empty space or a space occupied by the other side
        for i in range(1, 3):
            if self.state[2-i][i] != potentialWinner:
                potentialWinnerHasWon = False
        #If we have found a win, set the appropriate winner
        if potentialWinnerHasWon:
            if potentialWinner == 'X': xWins = True
            elif potentialWinner == 'O':
                oWins = True
            # It is possible for None to be marked as a winner if there are 3 empty spaces in a row. We don't care about that.

        #Now that we know if either X or Y won, return the result:
        if xWins and oWins: return 'both'
        elif xWins: return 'X'
        elif oWins: return 'O'
        elif None in chain(*self.state): return None    #itertools.chain(*list) seems to be the recommended way to flatten nested lists in Python
        else: return 'tie'
    def __str__(self):
        #These are all separated into different strings for each line to make it easier to pick a character by line and column number.
        #WARNING: All lines must be the same length
        result = [
            '       #       #       ',
            '       #       #       ',
            '       #       #       ',
            '#######################',
            '       #       #       ',
            '       #       #       ',
            '       #       #       ',
            '#######################',
            '       #       #       ',
            '       #       #       ',
            '       #       #       '
        ]
        xGraphic = [
            '  \\ /  ',
            '   X   ',
            '  / \\  '
        ]
        oGraphic = [
            ' /---\\ ',
            ' |   | ',
            ' \\___/ '
        ]
        #This appears rotated because x references which inner list and the inner lists appear on top of each other here, and y references the position within the inner lists that are displayed horizontally.
        #WARNING: All must be the same size. Do not remove whitespace from shorter labels
        #WARNING: These must each be in their own list with a length of 1. This is done to make it easier to use the same function for drawing both the symbol graphics and the key graphics.
        keyGraphics = [
            [[' 7 '], ['4/U'], ['1/J']],
            [[' 8 '], ['5/I'], ['2/K']],
            [[' 9 '], ['6/O'], ['3/L']]
        ]
        def placeGraphic(graphic, cornerX, cornerY):
            for x in range(len(graphic[0])):
                for y in range(len(graphic)):
                    result [cornerX+x][cornerY+y] = graphic[x][y]

        #Go through all positions on the board and place the graphics as needed
        #WARNING: The method of determining which indexes to use place the graphics relies on the board and graphics being a specific size. If you change either of those, you must redo the math. More details on what to redo in the comments
        for x in range(3):
            for y in range(3):
                #8 and 4 are used here because each space takes up 8 horizontal characters and 4 vertical characters, INCLUDING the bottom and right separators.
                if self.state[x][y] == 'X': placeGraphic(xGraphic, 8*x, 4*y)
                elif self.state[x][y] == 'O': placeGraphic(oGraphic, 8*x, 4*y)
                #8*x and 4*y are used for the same reason as above. x is offset by 2 and y by 1 to center them.
                else: placeGraphic(keyGraphics[x][y], 8*x + 2, 4*y + 1)
        #Convert the result into one string and return it
        resultAsString = ''
        for line in result:
            resultAsString += line
            resultAsString += '\n'
        return resultAsString

class Tictactoe(): #This class represents a game.

    def __init__(self, firstPlayer):
        self.nextPlayer = firstPlayer
        self.winner = None
        self.board = Board()
    def move(self, x, y):
        #Validate that the position exists and is free
        if not (x in range(3) and y in range(3)): raise ValueError('Position out of range')
        if self.board.state[x][y] != None: raise ValueError('Position is occupied')
        #Set the board state, check for winners, and change the next player
        self.board.state[x][y] = self.nextPlayer
        self.winner = self.board.getWinner
        self.nextPlayer = 'X' if self.nextPlayer == 'O' else 'X'

class Player(): #This class represents a generic player. This will be extended for human players, and could theoretically be extended to computer players.
    def __init__(self, symbol):
        if symbol not in ['X', 'O']: raise ValueError('A player\'s symbol must be X or O')
        self.symbol = symbol
        self.name = symbol
    def move(self):
        raise NotImplementedError
    def __str__(self):
        return self.symbol if self.symbol == self.name else f'{self.symbol}:{self.name}'

class HumanPlayer(Player):  #This extends the Player class, and focuses specifically on creating a human player by providing input methods
    def __init__(self, symbol):
        super(symbol)
        userInput = input('Name for player %s: ' % self.symbol)
        self.name = userInput if userInput != '' else self.symbol
    def move(self, game):
        os.system('cls' if os.name == 'nt' else 'clear')    #Clear the screen

        #Print information
        print(f'{self.name}\'s turn:')
        print(game.board)
        print()

        #Get the desired position and perform the move
        translationTable = {    #A table to translate user inputs to tuples representing x and y locations
            '7': (0, 0),
            '8': (1, 0),
            '9': (2, 0),
            '4': (0, 1),
            '5': (1, 1),
            '6': (2, 1),
            '1': (0, 2),
            '2': (1, 2),
            '3': (2, 2),
            'u': (0, 1),
            'i': (1, 1),
            'o': (2, 1),
            'j': (0, 2),
            'k': (1, 2),
            'l': (2, 2)
        }
        while True:
            move = input('%s, what is your next move? ' % (player)).lower()[0]
            if move not in translationTable.keys():
                print('Error: Invalid move')
                continue
            x,y = translationTable[move]
            if game.board.state[x][y] != None:
                print('Error: That space is not empty')
                continue
            break
        game.board.state[x][y] = self.symbol