def rock_paper_scissors_menu(player):
    print('Welcome to the game of Rock Paper & Scissors!')
    return start_playing_rps(player)


def play_rps_again(player):
    answer = input(f'Would you like to play again {player.name}? (y/n)')
    if answer.lower() not in 'yn' or len(answer) != 1:
        print('Invalid input, only y or n please.')
        return play_rps_again(player)
    elif answer.lower() == 'y':
        print('Great! Let\'s play again!')
        return rock_paper_scissors(player)
    else:
        print('Good times.')
        player.update_game_data()
        return


def rock_paper_scissors(player):
    import random
    rock, paper, scissors = 'rock', 'paper', 'scissors'
    choices = [rock, paper, scissors]
    computer_choice = choices[random.randint(0, 2)]
    user_choice = input('Please choose rock, paper or scissors (Enter r/p/s)')
    if user_choice.lower() not in 'rps' or len(user_choice) != 1:
        print('Error, invalid input')
        return rock_paper_scissors(player)
    if user_choice.lower() == 'r':
        user_choice = rock
    elif user_choice.lower() == 'p':
        user_choice = paper
    else:
        user_choice = scissors
    if user_choice == computer_choice:
        print(f'We both chose {user_choice}! It\'s a draw!')
        player.played('RPS')
        player.totals_update()
        return play_rps_again(player)
    if user_choice == rock:
        if computer_choice == paper:
            print(f'You chose rock, but I chose paper. You lose.')
            player.played('RPS')
            player.totals_update()
            return play_rps_again(player)
        else:
            print(
                f'You chose {user_choice} and I chose {computer_choice}. You win this time, but the statistics are on my side..')
            player.played('RPS')
            player.win('RPS')
            player.totals_update()
            return play_rps_again(player)
    elif user_choice == paper:
        if computer_choice == scissors:
            print(f'You chose {user_choice}, but I chose {computer_choice}. You lose.')
            player.played('RPS')
            player.totals_update()
            return play_rps_again(player)
        else:
            print(
                f'You chose {user_choice} and I chose {computer_choice}. You win this time, but the statistics are on my side..')
            player.played('RPS')
            player.win('RPS')
            player.totals_update()
            return play_rps_again(player)
    else:
        if computer_choice == rock:
            print(f'You chose {user_choice}, but I chose {computer_choice}. You lose.')
            player.played('RPS')
            player.totals_update()
            return play_rps_again(player)
        else:
            print(
                f'You chose {user_choice} and I chose {computer_choice}. You win this time, but the statistics are on my side..')
            player.played('RPS')
            player.win('RPS')
            player.totals_update()
            return play_rps_again(player)


def start_playing_rps(player):
    answer = input('Would you like to play(y/n)')
    if answer.lower() not in 'yn' or len(answer) != 1:
        print('Invalid input, only y or n please.')
        return start_playing_rps(player)
    elif answer.lower() == 'y':
        print('Great! Let\'s play!')
        return rock_paper_scissors(player)
    else:
        print('Good times, bye!')
        return
