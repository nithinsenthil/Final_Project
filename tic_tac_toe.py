#Application can be written here

from classes import *

newGame = GameController()
newGame.runtictactoe()


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