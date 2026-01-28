import random

def print_ui(l_hidden, l_used, lives):
    print('')
    print(*l_hidden)
    print(*l_used)
    print(f'You have {lives} lives remaining\nPlease enter a letter:')

def check_input(l):
    if type(l) == str and len(l) == 1:
        return True
    else:
        return False

words = ['planet','oxygen','jungle','python','marble','shadow','galaxy','fog','coin','quill','brave','adventure','sunflower','clockwork','magnitude']

word = random.choice(words)
letters_hidden = []
for l in word:
    letters_hidden.append('-')

letters_used = []
lives_remaining = 8

while True:
    print_ui(letters_hidden, letters_used, lives_remaining)
    guess = input()
    if check_input(guess):
        i = 0
        if word.count(guess) > 0:
            for l in word:
                if guess == l:
                    letters_hidden[i] = guess
                i += 1
        else:
            letters_used.append(guess)
            lives_remaining -= 1
    else:
        print('Incorrent input')

    if letters_hidden.count('-') == 0:
        input('You won nice good job')
        break
    if lives_remaining == 0:
        input('You lost...')
        break
    