
def is_valid_input(letter_guessed):

    if len(letter_guessed) > 1 or letter_guessed.isalpha() == False:
        return False
    else:
        return True

x = is_valid_input('kdkdk*')
print(x)