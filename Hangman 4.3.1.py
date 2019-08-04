user_guess=input("Guess a letter:")

if len(user_guess)>1:
    if user_guess.isalpha() == False:
        print ("E3")
    else:
        print("E1")
elif user_guess.isalpha() == False:
    print("E2")
else:
    print(user_guess.lower())