'''
HANGMAN FRUIT GAME
'''
import random  # import random
from os import system, name  # import system from os for clear function
import pyfiglet  # import pyfiglet for hangman logo
import colorama  # import colorama fore, back and style


gameState = [" +->-+\n |   |\n     |>\n     |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n     |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n  |  |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n /|  |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n /|\ |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n /|\ |>\n /   |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n /|\ |>\n / \ |>\n     |>\n<=====>",

             " +->-+\n |   |\n[Q   |>\n /|\ |>\n / \ |>\n     |>\n<=====>",

             " +->-+\n |   |\n[Q]  |>\n /|\ |>\n / \ |>\n     |>\n<=====>"]


words = 'ant baboon badger bat bear beaver camel' \
    'cat clam cobra cougar coyote crow deer' \
    ' dog donkey duck eagle ferret fox frog goat' \
    ' goose hawk lion lizard llama mole monkey moose' \
    ' mouse mule newt otter owl panda parrot ' \
    ' pigeon python rabbit ram rat raven rhino' \
    ' salmon seal shark sheep skunk sloth' \
    ' snake spider stork swan tiger' \
    ' toad trout turkey turtle weasel whale wolf wombat zebra'.split()


# define our clear function
def clear():
    '''
    This function is to clear console on windows and mac/linux
    '''
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def getRandomWord(wordList):
    '''
    This function returns a random string from the passed list of strings.
    '''
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def display_the_board(missingLetter, foundLetter, randomWord):
    '''
    This function displays the asii hangman
    Displays the board, letters tried, the word length
    '''
    from colorama import Fore
    print(Fore.BLUE)
    print(pyfiglet.figlet_format("HANGMAN", justify="left"))
    print(Fore.LIGHTBLACK_EX)
    print(gameState[len(missingLetter)])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Fruit letters you have tried:', end=' ')
    for letter in missingLetter:
        print(letter, end=' ')
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    blanks = '_' * len(randomWord)
    # cover blanks _ with correct letter
    for i in range(len(randomWord)):
        if randomWord[i] in foundLetter:
            blanks = blanks[:i] + randomWord[i] + blanks[i+1:]

    print('The word length is:')
    from colorama import Fore
    print(Fore.YELLOW)
    for letter in blanks:  # show the random word from the words list
        print(letter, end=' ')


def getGuess(already_guessed):
    '''
    Returns the letter the player entered.
    This function checks that the player entered
    a single letter.
    '''
    while True:
        from colorama import Fore
        print(Fore.BLUE)
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Pick a letter of a fruit?   ')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~')
        guess = input()
        guess = guess.lower()
        clear()
        if len(guess) != 1:
            clear()
            from colorama import Fore
            print(Fore.BLUE)
            print(pyfiglet.figlet_format("HANGMAN", justify="left"))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            check_guess_already = "{} isn't acceptable!".format(guess)
            print(check_guess_already)
            print('Enter a single fruit letter only!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif guess in already_guessed:
            clear()
            from colorama import Fore
            print(Fore.BLUE)
            print(pyfiglet.figlet_format("HANGMAN", justify="left"))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            check_guess_already = "{} is already used!".format(guess)
            print(check_guess_already)
            print('Choose another letter!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            clear()
            from colorama import Fore
            print(Fore.BLUE)
            print(pyfiglet.figlet_format("HANGMAN", justify="left"))
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            check_guess_already = "{} isn't a letter!".format(guess)
            print(check_guess_already)
            print('Enter a LETTER only!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
        else:
            return guess


def play_again():
    '''
    This function returns True if the
    player wants to play again.
    '''
    print(Fore.LIGHTBLACK_EX)
    print('--------------------------------------')
    print('Do you want to play again? (yes or no)')
    print('--------------------------------------')
    return input().lower().startswith('y')


missingLetter = ''
foundLetter = ''
randomWord = getRandomWord(words)
game_is_over = False

while True:
    display_the_board(missingLetter, foundLetter, randomWord)

    # Let the player enter a letter.
    guess = getGuess(missingLetter + foundLetter)

    if guess in randomWord:
        foundLetter = foundLetter + guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(randomWord)):
            if randomWord[i] not in foundLetter:
                foundAllLetters = False
                break
        if foundAllLetters:
            clear()
            from colorama import Fore
            print(Fore.BLUE)
            print(pyfiglet.figlet_format("HANGMAN", justify="left"))
            from colorama import Fore
            print(Fore.GREEN)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('You had ' + str(len(missingLetter)) + ' missed letters!')
            print('You had ' + str(len(foundLetter)) + ' correct letters!')
            from colorama import Fore
            print(Fore.CYAN)
            print('You have WON')
            from colorama import Fore
            print(Fore.GREEN)
            print('The word was "' + randomWord + '"!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            game_is_over = True
    else:
        missingLetter = missingLetter + guess

        # Check if player has guessed too many times and lost.
        if len(missingLetter) == len(gameState) - 1:
            clear()
            from colorama import Fore
            print(Fore.BLUE)
            print(pyfiglet.figlet_format("HANGMAN", justify="left"))
            from colorama import Fore
            print(Fore.RED)
            print('You have run out of guesses!\n')
            print('You had ' + str(len(missingLetter)) + ' missed letters!')
            print('Missed Letters:', end=' ')
            for letter in missingLetter:
                print(letter, end=' ')
            print('')
            print('\nYou had ' + str(len(foundLetter)) + ' correct!')
            print('Correct Letters:', end=' ')
            for letter in foundLetter:
                print(letter, end=' ')
            print('')
            print('\nThe word was "' + randomWord + '".\n')
            game_is_over = True

    # Ask the player if they want to play again (but only if the game is done).
    if game_is_over:
        if play_again():
            clear()
            missingLetter = ''
            foundLetter = ''
            game_is_over = False
            randomWord = getRandomWord(words)
        else:
            break
