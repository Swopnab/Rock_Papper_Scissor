## rock paper scissor

import random
import math
import time

print("               rock paper scissor created by Swopnab                   ")
time.sleep(2)
print("                        please wait.........                           ")
time.sleep(1)

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

# at r>s, p>r, s>p
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

# return true if win condition is fulfilled (r>s, p>r, s>p)
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

# to keep playing until one user wins and to win, must win ceil(n/2) games
def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print('          It is a tie. Player and the computer have both chosen {}.          \n'.format(user))
        # you win
        elif result == 1:
            player_wins += 1
            print('          Player chose {} and the computer chose {}. You won!          \n'.format(user, computer))
        else:
            computer_wins += 1
            print('          Player chose {} and the computer chose {}. You lost :          \n'.format(user, computer))

    if player_wins > computer_wins:
        print('          Player have won the best of {} games! congratulations you have won the game          '.format(n))
    else:
        print('          what a noob, the computer has won the best of {} games. (T_T) You lose, Better luck next time!          '.format(n))

if __name__ == '__main__':
    play_best_of(3)



