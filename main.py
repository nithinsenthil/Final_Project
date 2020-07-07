#Application can be written here

from classes import *

#Introduction
print('''#######             #######                  #######               
   #    #  ####        #      ##    ####        #     ####  ###### 
   #    # #    #       #     #  #  #    #       #    #    # #      
   #    # #            #    #    # #            #    #    # #####  
   #    # #            #    ###### #            #    #    # #      
   #    # #    #       #    #    # #    #       #    #    # #      
   #    #  ####        #    #    #  ####        #     ####  ######''')
print('-------------Created by Nithin Senthil and Bruce Blore-------------')

#Initiate players and score
xPlayer = HumanPlayer('X')
oPlayer = HumanPlayer('O')
firstPlayer = ' '
while firstPlayer.upper()[0] not in 'XO':
    firstPlayer = input('Who goes first (X/O)? ')
score = [0, 0]

while True:
    game = Tictactoe(firstPlayer)

    while True:
        if game.winner != None:
            break
        if game.nextPlayer == 'X':
            xPlayer.move(game)
        else:
            oPlayer.move(game)

    if game.winner == 'tie': print('It is a tie.')
    elif game.winner == 'both': raise ValueError('Both X and O have completed a line. This should not be possible and indicates a bug in the code.')
    else:
        def winner():   #Get the object representing the winning player
            if game.winner == 'X': return xPlayer
            elif game.winner == 'O': return oPlayer
            else: raise ValueError('This method should only be called when game.winner is X or O')
        print('Hooray! %s has won the game!' % winner())
        score[0 if game.winner == 'X' else 1] += 1

    print('\nSCOREBOARD:\n%s --- %s\n%s --- %s\n' % (xPlayer, score[0], oPlayer, score[1]))
    if input('Do you want to play again? (y/n) ').lower()[0] == 'n':
        break