import random

winter_words = ["snow", "december", "january", "snowman", "christmas","cold", "valentines", "carols", "stockings"]
winter_word = random.choice(winter_words)

summer_words = ["pool", "beach", "ocean", "heat", "green","august", "summer", "july", "independence"]
summer_word = random.choice(summer_words)

fall_words = ["pumpkin", "ghost", "candy", "costume", "leaves","orange", "black", "thanksgiving", "autumn"]
fall_word = random.choice(fall_words)

answer= []
guesses =[]
counter = 0
word = ""

category = input("Type one of the following: winter, summer, or fall: ")

if category == "winter":
    word = winter_word
elif category == "summer":
    word = summer_word
else:   
    word = fall_word

    
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

        