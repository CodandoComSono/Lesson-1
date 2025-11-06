import random
import time

print('\033[1;34m=-=\033[m' * 20)
print('\033[1;36mWelcome to the Rock, Paper, Scissors Game!\033[m'.center(60))
print('\033[1;34m=-=\033[m' * 20)

while True:
    print('''Options:

[ 1 ] - Rock
[ 2 ] - Paper
[ 3 ] - Scissors''')

    print('')

    player = int(input('Enter your choice number: '))

    print('ROCK')
    time.sleep(1)
    print('PAPER')
    time.sleep(1)
    print('SCISSORS!!!')

    print('\033[1;34m=-=\033[m' * 20)

    computer = random.randint(1, 3)

    if player == computer:
        print('It’s a tie! Let’s play again.')
        print('\033[1;34m=-=\033[m' * 20)

    elif player == 1:
        if computer == 3:
            print('You win! Rock beats Scissors.')
            print('\033[1;34m=-=\033[m' * 20)
        else:
            print('You lose! Paper beats Rock.')
            break

    elif player == 2:
        if computer == 1:
            print('You win! Paper beats Rock.')
            print('\033[1;34m=-=\033[m' * 20)
        else:
            print('You lose! Scissors beat Paper.')
            break

    elif player == 3:
        if computer == 2:
            print('You win! Scissors beat Paper.')
            print('\033[1;34m=-=\033[m' * 20)
        else:
            print('You lose! Rock beats Scissors.')
            break

    else:
        print('Please enter a valid option!')

print('Game over. Thanks for playing!')

print('\033[1;34m=-=\033[m' * 20)
