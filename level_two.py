import random

words = ["pumpkin", "ghost", "candy", "costume", "leaves","orange", "black", "fall", "autumn"]
word = random.choice(words)
answer= []
guesses =[]
counter = 0



while counter < len(set(word)):  #returns only UNIQUE characters
    
    guess= input("Guess a single letter: ")

    if len(guess) != 1:
        print("Input ONLY 1 letter")
        continue
    if guess in guesses:
        print("Letter already guessed")
        continue 
    guesses.append(guess)
    if guess in word:
        answer.append(guess)
        counter += 1
    else:
        print("Guess again")
    for letter in word:
        if letter in answer:
            print(letter , end="")
        else:
            print ("_", end= "")

        