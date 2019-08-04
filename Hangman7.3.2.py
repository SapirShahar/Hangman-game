secret_word = "friends"
old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']

def check_win(secret_word, old_letters_guessed):
    right_guesses=0
    for letter in secret_word:
        if letter in old_letters_guessed:
            right_guesses+=1

    if right_guesses == len(secret_word):
        return True
    else:
        return False

x=check_win(secret_word,old_letters_guessed)
print(x)