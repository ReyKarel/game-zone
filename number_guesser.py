import random


def welcome_number_guesser(player):
    print(f'Welcome to the number guessing game, {player.name}!\n'
          f'Each round the computer will generate a number between 1-100\n'
          f'Your goal is to guess it correctly in as few attempts as possible\n'
          f'You have 5 guesses total, the faster you guess the more points you get')
    start_number_guesser(player)


def start_number_guesser(player):
    want_to_play = input('Would you like to play? (y/n)')
    if want_to_play.lower() not in 'yn':
        print('Invalid input, y or n only please.')
        return start_number_guesser(player)
    elif want_to_play.lower() == 'y':
        return number_generator(player)
    else:
        print('Ok, bye!')
        return


def number_generator(player):
    computer_number = random.randint(1, 100)
    return guessing_round(computer_number, player)


def guess_another_number(player):
    answer = input('That was fun! Would you like to play again? (y/n)')
    if answer.lower() not in 'yn':
        print('Invalid input! y/n only!')
        return guess_another_number(player)
    elif answer == 'y':
        return number_generator(player)
    else:
        print('Ok, it was fun!')
        player.update_game_data()
        return


def guessing_round(computer_number, player, attempts=5):
    while attempts > 0:
        user_guess = input('Guess which number I chose!\n'
                           f'(You have {attempts} guesses left) ')
        if user_guess.isdecimal():
            user_guess = int(user_guess)
            if user_guess < 0 or user_guess > 100:
                print('Out of range, numbers between 1-100 only')
                return guessing_round(computer_number, player, attempts)
            else:
                attempts -= 1
                if user_guess == computer_number:
                    print('Congratulations! That is the correct number!\n'
                          f'You guessed correctly in {5 - attempts} attempt(s), you win {attempts + 1} point(s)!')
                    player.win('Number guesser', attempts + 1)
                    player.played('Number guesser')
                    player.totals_update()
                    return guess_another_number(player)
                else:
                    if user_guess > computer_number:
                        print(f'Not quite! My number is lower than {user_guess}!')
                        return guessing_round(computer_number, player, attempts)
                    else:
                        print(f'Not quite! My number is higher than {user_guess}!')
                        return guessing_round(computer_number, player, attempts)
        else:
            print('Invalid input, natural numbers between 1-100 only.')
            return guessing_round(computer_number, player, attempts)

    print(f'Sorry, your final guess was incorrect.\n'
          f'The number was actually {computer_number}, maybe next time!')
    player.played('Number guesser')
    player.totals_update()
    return guess_another_number(player)
