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
attempts = 6

category = input("Type one of the following: winter, summer, or fall: ")

if category == "winter":
    word = winter_word
elif category == "summer":
    word = summer_word
else:   
    word = fall_word

while counter < len(set(word)) and attempts > 0:
    guess= input("Guess a single letter: ")

    if len (guess) != 1:
        print("Input ONLY 1 letter")
        continue
    elif guess in guesses:
        print("Letter already guessed")
        continue
    elif guess in word:
        answer.append(guess)
        counter += 1
    else:
        print("\n")
        print("Guess again")
        attempts -= 1
        print(f"CAREFUL! You only have {attempts} remaining! ")
    for letter in word:
        if letter in answer:
            print(letter , end="")
        else:
            print ("_", end= "")
    print("\n")

if set(answer) == set(word):
    print("YOU DID IT! Wahoo!")
else:
    print(f"Sorry you didn't guess in the number of attempts. The word was {word}")
