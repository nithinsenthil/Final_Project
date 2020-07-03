#The class(es) can be written here
class Game:

    def __init__(self):
        pass


class Board(Execution):

    def __init__(self, theBoard):
        self.board = theBoard


    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard
class Player:

    def __init__(self, board, letter):
        super().__init__(board)
        self.letter = letter

    def makeMove(self, letter, move):
        self.board[move] = self.letter

    def isWinner(self):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == self.letter and self.board[8] == self.letter and self.board[9] == self.letter) or  # across the top
                (self.board[4] == self.letter and self.board[5] == self.letter and self.board[6] == self.letter) or  # across the middle
                (self.board[1] == self.letter and self.board[2] == self.letter and self.board[3] == self.letter) or  # across the bottom
                (self.board[7] == self.letter and self.board[4] == self.letter and self.board[1] == self.letter) or  # down the left side
                (self.board[8] == self.letter and self.board[5] == self.letter and self.board[2] == self.letter) or  # down the middle
                (self.board[9] == self.letter and self.board[6] == self.letter and self.board[3] == self.letter) or  # down the right side
                (self.board[7] == self.letter and self.board[5] == self.letter and self.board[3] == self.letter) or  # diagonal
                (self.board[9] == self.letter and self.board[5] == self.letter and self.board[1] == self.letter))  # diagonal

class Human_player(Board):

    def __init__(self, board, letter):
        super().__init__(board)
        self.letter = letter

    def makeMove(self, letter, move):
        self.board[move] = self.letter

    def isWinner(self):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == self.letter and self.board[8] == self.letter and self.board[9] == self.letter) or  # across the top
                (self.board[4] == self.letter and self.board[5] == self.letter and self.board[6] == self.letter) or  # across the middle
                (self.board[1] == self.letter and self.board[2] == self.letter and self.board[3] == self.letter) or  # across the bottom
                (self.board[7] == self.letter and self.board[4] == self.letter and self.board[1] == self.letter) or  # down the left side
                (self.board[8] == self.letter and self.board[5] == self.letter and self.board[2] == self.letter) or  # down the middle
                (self.board[9] == self.letter and self.board[6] == self.letter and self.board[3] == self.letter) or  # down the right side
                (self.board[7] == self.letter and self.board[5] == self.letter and self.board[3] == self.letter) or  # diagonal
                (self.board[9] == self.letter and self.board[5] == self.letter and self.board[1] == self.letter))  # diagonal

class Execution:

    def __init__(self):
        self.theBoard = theBoard = [' '] * 10
        self.playerLetter, self.computerLetter = playerLetter()

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

