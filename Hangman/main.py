import random
words = ["bag", "best", "create", "rainbow", "arrow", "balloon", "wall", "computer", "watch", "xylophone", "glass", "piano", "telephone", "screen", "shirt"]
word = random.choice(words)
turns = 12
guesses = ''
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win, congratulations!!!")

        print("The word is", word)
        break
    
    guess = input("Enter your character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses!")

        if turns == 0:
            print("You have lost.. Better luck next time!")