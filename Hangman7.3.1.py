secret_word="mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']

def show_hidden_word(secret_word, old_letters_guessed):

    user_guess_list=[]
    for letter in secret_word:
        if letter in old_letters_guessed:
            user_guess_list.append(letter+" ")
        else:
            user_guess_list.append("_ ")
    user_guess_str= "".join (user_guess_list)
    print( user_guess_str)



print(show_hidden_word(secret_word, old_letters_guessed))