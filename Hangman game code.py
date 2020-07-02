# importing Libraries
import random as r

# variables
game_over = False
char_guessed = 'aeiou'
words = ['promote','intelligent','facebook','alphabate','objective','individual','successful','character','otherwise','mountain','beautiful','processor','instagram']
word = r.choice(words)
turns = 0

# welcome prints
user_name = input('Type Your name : ').title()
print(f'\nWelcome {user_name}.\nLet\'s play Word Guessing game.')
print('you have 6 chance to guess the word.\nIf you can guess the word then write it.\nOtherwise type any charachter.\nEvery guess -1 from your total guess.')

print(f'\nThe word has {len(word)} characters.only vowles are already given.\nGood Luck !')


# function
# ` for printing characters
def loops():
    for i in word:
        if i in char_guessed:
            print(i,end='')
        else:
            print(' _ ',end='')

#   for guess print
def guess_left():
    print(f'You have {6-turns} guess left.')

loops() # first call this for show the first word only with vowles.

# real things
while game_over != True:
    # checking user input duplicate or not
    if turns == 6:
        print(f'sorry no guesses left. The word is "{word}".')
        break

    user_guessed = input('\nGuess any character or the word : ').lower()

    if user_guessed == word:
        print('Congrats you guessed the word.')
        print(f'You guess the word in {turns} times')
        game_over = True

    elif user_guessed in char_guessed:
        print('Already guesses.')
        turns += 1
        guess_left()
        continue

    elif user_guessed not in word:
        print('Character not in the word.')
        turns += 1
        guess_left()

    else:
        print(f'\nYes "{user_guessed}" is in the word.')
        char_guessed += user_guessed
        turns += 1
        loops()
        print()
        guess_left()



