import os
import rock_paper
import number_guesser
import hangman
import csv
from tabulate import tabulate  # pip install tabulate


class PlayerLog:
    def __init__(self):
        self.player_list = []


list_of_players = PlayerLog()

game_path = os.getcwd()
if os.path.exists(os.path.join(game_path, 'game_data')):
    data_path = os.path.join(game_path, 'game_data')
    data_log = os.path.join(data_path, "game_data.csv")
    data_header = ['Player name', 'Total points', 'Total times played', 'Times played Rock Paper & Scissors',
                   'Rock Paper & Scissors points won',
                   'Times played Hangman', 'Hangman points won',
                   'Times played Number Guesser', 'Number Guesser points won',
                   ]
else:
    os.mkdir('game_data')
    data_path = os.path.join(game_path, 'game_data')
    data_log = os.path.join(data_path, "game_data.csv")
    data_header = ['Player name', 'Total points', 'Total times played', 'Times played Rock Paper & Scissors',
                   'Rock Paper & Scissors points won',
                   'Times played Hangman', 'Hangman points won',
                   'Times played Number Guesser', 'Number Guesser points won',
                   ]
    with open(data_log, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(data_header)

if not list_of_players.player_list:
    with open(data_log, 'r') as data_file:
        csv_reader = csv.reader(data_file)
        for line in csv_reader:
            if len(line) > 0:
                list_of_players.player_list.append(line[0])
        list_of_players.player_list.pop(0)


class Player(PlayerLog):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.scores = {'RPS': 0, 'Hangman': 0, 'Number guesser': 0}
        self.times_played = {'RPS': 0, 'Hangman': 0, 'Number guesser': 0}
        self.total_score = {'Total score': 0}
        self.total_games = {'Total games played': 0}
        self.data_row = [self.name, self.total_score['Total score'], self.total_games['Total games played'],
                         self.times_played['RPS'], self.scores['RPS'], self.times_played['Hangman'],
                         self.scores['Hangman'], self.times_played['Number guesser'], self.scores['Number guesser']
                         ]

    def show_details(self):
        print(self.name)
        print(self.scores)
        print(self.times_played)

    def totals_update(self):
        total_points = 0
        games_played = 0
        for score in self.scores.values():
            total_points += score
            self.total_score['Total score'] = total_points
        for games in self.times_played.values():
            games_played += games
            self.total_games['Total games played'] = games_played

    def sign_up(self):
        list_of_players.player_list.append(self.name)
        with open(data_log, 'a') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.data_row)

    def played(self, game):
        self.times_played[game] += 1

    def win(self, game, points=None):
        if points is None:
            self.scores[game] += 1
        else:
            self.scores[game] += points

    def update_player_data(self):
        with open(data_log, 'r') as data_file:
            csv_reader = csv.reader(data_file)
            for line in csv_reader:
                if len(line) > 0:
                    if self.name == line[0]:
                        self.times_played['RPS'] = int(line[1])
                        self.scores['RPS'] = int(line[2])
                        self.times_played['Hangman'] = int(line[3])
                        self.scores['Hangman'] = int(line[4])
                        self.times_played['Number guesser'] = int(line[5])
                        self.scores['Number guesser'] = int(line[6])

    def update_game_data(self):
        self.data_row = [self.name, self.total_score['Total score'], self.total_games['Total games played'],
                         self.times_played['RPS'], self.scores['RPS'], self.times_played['Hangman'],
                         self.scores['Hangman'], self.times_played['Number guesser'], self.scores['Number guesser']
                         ]
        temp_list = []
        with open(data_log, 'r') as data_file:
            csv_reader = csv.reader(data_file)
            for line in csv_reader:
                if len(line) > 0:
                    temp_list.append(line)
        temp_list.pop(0)
        new_list = []
        for line in temp_list:
            if self.name == line[0]:
                new_list.append(self.data_row)
            else:
                new_list.append(line)
        new_list = sorted(new_list, key=lambda x: str(x[1]), reverse=True)

        with open(data_log, 'w') as data_file:
            csv_writer = csv.writer(data_file)
            csv_writer.writerow(data_header)
            for line in new_list:
                csv_writer.writerow(line)


for name in list_of_players.player_list:
    globals()[name] = Player(name)
    globals()[name].update_player_data()


def show_scoreboard():
    display_data = []
    with open(data_log, 'r') as score_file:
        csv_reader = csv.reader(score_file)
        for row in csv_reader:
            if len(row) > 0:
                display_data.append(row)
    print(tabulate(display_data))


def main_menu(player=None):
    print('Welcome to the gaming arena!\n'
          'This is the main menu. \n'
          'To navigate, please input the number of your choice.')
    if player is None:
        main_menu_navigation()
    else:
        main_menu_navigation(player)


def main_menu_navigation(player=None):
    if player is None:
        main_menu_choice = input('1 - I am a new player (sign up)\n'
                                 '2 - I am an existing player (log in)\n'
                                 '3 - Show leaderboard\n'
                                 '4 - Exit the gaming zone\n'
                                 'Please enter your choice: ')
        if main_menu_choice not in '1234' or main_menu_choice == '':
            print("Invalid input! Please choose an option between 1-4.")
            main_menu_navigation()
        elif main_menu_choice == '1':
            name_good = 0
            while name_good == 0:
                new_player = input('Please enter your name (3-8 characters, letters only)')
                if len(new_player) < 3 or len(new_player) > 8 or new_player.isalpha() is False:
                    print('Invalid username, please follow the naming rules')
                elif new_player in list_of_players.player_list:
                    name_taken = 0
                    while name_taken == 0:
                        print(
                            f'There\'s already a player named {new_player}, if this is you please go to the login menu.')
                        go_back = input('Would you like to go back? (y/n)')
                        if go_back.lower() == 'y':
                            return main_menu_navigation()
                        elif go_back.lower() == 'n':
                            name_taken += 1
                        else:
                            print('Invalid input, y or n only please')
                else:
                    name_good += 1
                    new_user = Player(new_player)
                    new_user.sign_up()
                    return game_menu(new_user)

        elif str(main_menu_choice) == '2':
            returning_player = input('Please enter your name, player. ')
            if returning_player in list_of_players.player_list:
                return main_menu_navigation(eval(returning_player))
            else:
                print(
                    f'The name {returning_player} is not registered. If you are a new player please go back and sign up.')
                return main_menu_navigation()
        elif str(main_menu_choice) == '3':
            show_scoreboard()
            return main_menu_navigation()
        elif str(main_menu_choice) == '4':
            print('Ok bye bye')
    else:
        main_menu_choice = input('1 - Go to game selection\n'
                                 '2 - Show leaderboard\n'
                                 f'3 - Log out ({player.name})\n'
                                 'Please enter your choice: ')
        if len(main_menu_choice) == 1 and main_menu_choice in '123':
            if main_menu_choice == '1':
                return game_menu(player)
            elif main_menu_choice == '2':
                show_scoreboard()
                return main_menu_navigation(player)
            else:
                return main_menu()
        else:
            print("Invalid input! Please choose an option between 1-3.")
            main_menu_navigation(player)


def game_menu(player):
    print(f'Which game would you like to play now, {player.name}?')
    game_menu_choice = input('1 - Hangman\n2 - Rock paper scissors\n3 - Number guesser\n4 - Back to main menu')
    if game_menu_choice not in '1234':
        print("Invalid input! Please choose an option between 1-4.")
        return game_menu(player)
    elif game_menu_choice == '1':
        hangman.start_hangman(player)
        game_menu(player)
    elif game_menu_choice == '2':
        rock_paper.rock_paper_scissors_menu(player)
        game_menu(player)
    elif game_menu_choice == '3':
        number_guesser.welcome_number_guesser(player)
        game_menu(player)
    else:
        return main_menu(player)


main_menu()
