#file path to insert: hangman.txt

#Welcome screen of the game
def ascii_art ():
    HANGMAN_ASCII_ART="""
      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_  \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |
                         |___/"""
    print(HANGMAN_ASCII_ART)

#reading the file contains words list
def choose_word(file_path, index):
    input_file = open(file_path, "r")
    words_lst= input_file.read()
    words_lst= words_lst.split(' ')
    unique_word=[]
    len_lst=len(words_lst)
    # in case the user insert an index that not exists (bigger than max),
    # Continue counting from the beginning of the list
    if index > len_lst:
        index=index-len_lst
    for i in words_lst:
        if i not in unique_word:
            unique_word.append(i)
    specific_word= words_lst[index-1]
    return specific_word

#hangman photo for each number of incorrect guesses
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {
    1:"""
        x-------x""",


    2:"""
        x-------x
        |
        |
        |
        |
        |""",

    3:"""
        x-------x
        |       |
        |       0
        |
        |
        |""",

    4:"""
        x-------x
        |       |
        |       0
        |       |
        |
        |""",

    5:"""
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |""",

    6:"""
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |""",

    7:"""
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |"""}
    print (HANGMAN_PHOTOS[num_of_tries])

#showing the current status of the hidden word- letters/blanks
def show_hidden_word(secret_word, old_letters_guessed):
    user_guess_list=[]
    for letter in secret_word:
        if letter in old_letters_guessed:
            user_guess_list.append(letter+" ")
        else:
            user_guess_list.append("_ ")
    user_guess_str= "".join (user_guess_list)
    print( user_guess_str)

#check validation of the guess and show letters that was guessed
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1 or letter_guessed.isalpha() == False or letter_guessed.lower() in old_letters_guessed:
        old_letters_guessed.sort()
        old_letters_guessed_arrow = "-> ".join(old_letters_guessed)
        print ('X')
        print(old_letters_guessed_arrow)
        return False
    else:
        letters_guessed_lower = letter_guessed.lower()
        old_letters_guessed.append(letters_guessed_lower)
        return True

# Check if the user win or lose the game
def check_win(secret_word, old_letters_guessed):
    right_guesses=0
    for letter in secret_word:
        if letter in old_letters_guessed:
            right_guesses+=1
    if right_guesses == len(secret_word):
        print ('WIN')
        return True
    else:
        return False

def main():
    #variables
    num_of_tries=1
    win=False
    MAX_TRIES=int(7)
    old_letters_guessed = []

    ascii_art()
    print ('Number of tries:',MAX_TRIES-1)
    print ('Let’s start!')
    user_path= input ("Enter file path:")
    user_index= int(input ("Enter index:"))
    secret_word= choose_word(user_path,user_index)
    print_hangman(1)
    show_hidden_word(secret_word,old_letters_guessed)

    while num_of_tries < MAX_TRIES and win==False:
        user_guessed = input("Guess a letter:")
        valid_letter = try_update_letter_guessed(user_guessed, old_letters_guessed)
        if valid_letter:
           show_hidden_word(secret_word, old_letters_guessed)
           num_of_tries += 1
           if user_guessed in secret_word:
               if user_guessed not in old_letters_guessed :
                   old_letters_guessed.append(user_guessed)
           else:
               print(':(')
               print_hangman(num_of_tries)
        win = check_win(secret_word, old_letters_guessed)
    if num_of_tries ==MAX_TRIES and win==False:
        print ('LOSE')


if __name__ == "__main__":
    main()