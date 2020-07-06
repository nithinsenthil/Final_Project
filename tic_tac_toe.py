#Application can be written here

import random

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.status = "Error"
        self.winner = None

    def getStatus(self):
        return self.status

    def getWinner(self):
        return self.winner

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'firstPlayer'
        else:
            return 'secondPlayer'

    def getScore(self):
        return self.score

    def reset(self):
        return 'Error, method not implemented.'


class Tictactoe(Game):

    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.playerLetter = self.__inputPlayerLetter(self.players[0])
        self.board = [' '] * 10
        self.status = 'Error'
        self.winner = None
        self.score = [0,0]

    def run(self):
        gameIsPlaying = True
        turn = self.whoGoesFirst()
        while gameIsPlaying:
            if turn == 'firstPlayer':
                # Player's turn.
                print()
                self.__drawBoard()
                print()
                move = self.__getPlayerMove(self.players[0])
                self.__makeMove(self.playerLetter[0], move)

                if self.__isWinner(self.playerLetter[0]):
                    self.__drawBoard()
                    print()
                    self.winner = self.players[0]
                    self.score[0] += 1
                    self.status = 'done'
                    gameIsPlaying = False

                else:
                    if self.__isBoardFull():
                        self.__drawBoard()
                        self.status = 'tie'
                        break
                    else:
                        turn = 'secondPlayer'

            else:
                # Player 2's turn.
                print()
                self.__drawBoard()
                print()
                move = self.__getPlayerMove(self.players[1])
                self.__makeMove(self.playerLetter[1], move)

                if self.__isWinner(self.playerLetter[1]):
                    self.__drawBoard()
                    print()
                    self.winner = self.players[1]
                    self.score[1] += 1
                    self.status = 'done'
                    gameIsPlaying = False

                else:
                    if self.__isBoardFull():
                        self.__drawBoard()
                        self.status = 'tie'
                        break
                    else:
                        turn = 'firstPlayer'

    def reset(self):
        self.board = [' '] * 10
        self.status = 'Error'
        self.winner = None

#The following methods are private methods not to be called from outside the class.
    def __drawBoard(self):
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

    def __makeMove(self, letter, move):
        self.board[move] = letter

    def __isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or  # across the top
                (self.board[4] == le and self.board[5] == le and self.board[6] == le) or  # across the middle
                (self.board[1] == le and self.board[2] == le and self.board[3] == le) or  # across the bottom
                (self.board[7] == le and self.board[4] == le and self.board[1] == le) or  # down the left side
                (self.board[8] == le and self.board[5] == le and self.board[2] == le) or  # down the middle
                (self.board[9] == le and self.board[6] == le and self.board[3] == le) or  # down the right side
                (self.board[7] == le and self.board[5] == le and self.board[3] == le) or  # diagonal
                (self.board[9] == le and self.board[5] == le and self.board[1] == le))  # diagonal

    def __isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def __getPlayerMove(self, player):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.__isSpaceFree(int(move)):
            print('%s, what is your next move? (1-9)' % (player))
            move = input()
        return int(move)

    def __isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.__isSpaceFree(i):
                return False
        return True

    def __inputPlayerLetter(self, player):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('%s, do you want to be X or O?' % (player))
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


class GameController:
    def __init__(self):
        pass

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def runtictactoe(self):
        print('Welcome to Tic Tac Toe')
        first = input("Enter Player 1's name: ")
        second = input("Enter player 2's name: ")
        session = Tictactoe(first, second)
        while True:
            session.run()
            status = session.getStatus()
            if status == 'tie':
                print('The game is a tie!')
            elif status == 'done':
                winner = session.getWinner()
                print('Hooray! %s has won the game!' % (winner))
            elif status == 'Error':
                print('Oh no something went wrong.')

            score = session.getScore()
            print('\nSCOREBOARD:\n%s --- %s\n%s --- %s\n' % (first, score[0], second, score[1]))

            if self.playAgain():
                session.reset()
            else:
                break

newGame = GameController()
newGame.runtictactoe()