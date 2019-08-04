old_letters = ['a', 'b', 'c']
def check_valid_input(letter_guessed, old_letters_guessed):

    if len(letter_guessed) > 1 or letter_guessed.isalpha() == False or letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


x = check_valid_input('s', old_letters)
print(x)