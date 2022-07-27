import random

hangman_graphics = ['''
    _________
    |         |
    |         0
    |        /|\\
    |        / \\
    |
    |
▔▔▔▔▔▔▔▔▔▔
         ''',
                    '''
                        _________
                        |         |
                        |         0
                        |        /|\\
                        |        / 
                        |
                        |
                    ▔▔▔▔▔▔▔▔▔▔
                             ''',
                    '''
                        _________
                        |         |
                        |         0
                        |        /|\\
                        |        
                        |
                        |
                    ▔▔▔▔▔▔▔▔▔▔
                             ''',
                    '''
                        _________
                        |         |
                        |         0
                        |        /|
                        |        
                        |
                        |
                    ▔▔▔▔▔▔▔▔▔▔
                             ''',
                    '''
                        _________
                        |         |
                        |         0
                        |         |
                        |        
                        |
                        |
                    ▔▔▔▔▔▔▔▔▔▔
                             ''',
                    '''
                        _________
                        |         |
                        |         0
                        |        
                        |        
                        |
                        |
                    ▔▔▔▔▔▔▔▔▔▔
                             ''',
                    '''
                        _________
                        |         |
                        |        
                        |        
                        |        
                        |
                        |
                    ▔▔▔▔▔▔▔▔▔▔
                             ''']

word_list = ['amazing', 'great', 'wonderful', 'incredible', 'unbelievable', 'orange', 'banana', 'mandarin',
             'avocado', 'television', 'armchair', 'firetruck', 'kindergarten', 'police', 'government',
             'python', 'computer', 'language', 'coffee', 'eye', 'dollar', 'pyramid', 'calculator',
             'wok', 'cat', 'dart', 'board', 'table', 'tennis', 'soccer', 'football', 'beethoven',
             'mozart', 'piano', 'violin', 'musical', 'stage', 'actor', 'costume', 'jacket', 'drive',
             'turn', 'alphabet', 'digital', 'accessory', 'turtle', 'rabbit', 'rabbi', 'monkey', 'giraffe',
             'elephant', 'lizard', 'alligator', 'crocodile', 'alpaca', 'ghost', 'underwear', 'cotton',
             'kitchen', 'drawer', 'cabinet', 'cutlery', 'fork', 'spoon', 'salt', 'pepper', 'project',
             'homework', 'saxophone']


def start_hangman(player):
    print(f'Welcome to the game of Hangman {player.name}!\n'
          'In this game you\'ll guess letters to try and find what the secret word is!')
    answer = input('Would you like to play? (y/n) \n')
    if answer.lower() in 'yn' and len(answer) == 1:
        if answer == 'y':
            word_generator(player)
        else:
            print('Okay, bye!')
            return
    else:
        print('Invalid input, y or n only please!')
        start_hangman(player)


def play_hangman_again(player):
    answer = input(f'Would you like to play again {player.name}? (y/n) \n')
    if answer.lower() in 'yn' and len(answer) == 1:
        if answer == 'y':
            word_generator(player)
        else:
            print('Okay, bye!')
            player.update_game_data()
            return
    else:
        print('Invalid input, y or n only please!')
        play_hangman_again(player)


def word_generator(player):
    word = random.choice(word_list)
    return hangman_round(player, word)


def hangman_round(player, answer, attempts=6, current_board=[], wrong_guesses=None):
    filled_answer = []
    if wrong_guesses is None:
        wrong_guesses = []
    for letter in answer:
        filled_answer.append(letter.upper() + ' ')
    board = []
    for letter in answer:
        board.append('_')
    if len(current_board) == 0:
        current_board = board
    print('~' * 80)
    if attempts == 0:
        print(hangman_graphics[attempts - 7], ' '.join(filled_answer))
        print(f'You lost! The word was "{answer.capitalize()}", better luck next time!')
        player.played('Hangman')
        player.totals_update()
        return play_hangman_again(player)
    print(hangman_graphics[attempts - 7], ' '.join(current_board), f'Wrong guesses: {wrong_guesses}')
    guess = input(f'Please guess a letter, you have {attempts} attempt(s) left. \n')
    if not guess.isalpha():
        print('Invalid input, letters only')
        return hangman_round(player, answer, attempts, current_board, wrong_guesses)
    if len(guess) != 1:
        print('Invalid input, 1 letter only please.')
        return hangman_round(player, answer, attempts, current_board, wrong_guesses)
    if guess.lower() in wrong_guesses:
        print(f'You\'ve already guessed {guess} and it\'s not in the word. Guess another one')
        return hangman_round(player, answer, attempts, current_board, wrong_guesses)
    if guess.lower() in ''.join(current_board).lower():
        print(f'You\'ve already guessed {guess} and it was in the word. Guess another one')
        return hangman_round(player, answer, attempts, current_board, wrong_guesses)
    if guess.lower() in answer:
        guess = guess.lower()
        for i in range(len(answer)):
            if answer[i] == guess:
                current_board[i] = guess.upper()
        if '_' not in current_board:
            print(f'You got it! The word was {answer.capitalize()} \nYou won {attempts} point(s)!')
            player.played('Hangman')
            player.win('Hangman', attempts)
            player.totals_update()
            return play_hangman_again(player)
        print('Correct!')
        return hangman_round(player, answer, attempts, current_board, wrong_guesses)
    else:
        print('Sorry, wrong guess!')
        wrong_guesses.append(guess)
        attempts -= 1
        return hangman_round(player, answer, attempts, current_board, wrong_guesses)
