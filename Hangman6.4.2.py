#old_letters = ['a', 'p', 'c', 'f']

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
   # print (letter_guessed)
    if len(letter_guessed) > 1 or letter_guessed.isalpha() == False or letter_guessed.lower() in old_letters_guessed:
        old_letters_guessed.sort()
        old_letters_guessed_arrow = "-> ".join(old_letters_guessed)
        print ('X')
        print(old_letters_guessed_arrow)
        return False
    else:
        letters_guessed_lower = letter_guessed.lower()
        old_letters_guessed.append(letters_guessed_lower)
        print (old_letters_guessed)
        return True

x = try_update_letter_guessed('a', ['a', 'p', 'c', 'f'])
print (x)