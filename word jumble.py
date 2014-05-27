import random

# create a sequence of words and hints to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
HINTS = ("Name of a snake, and a programing language!", "Mess things up, is to... them", "A word for not hard",
         "A word for not simple.", "After doing maths you get a...", "Sounds like bones when played!")

# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
index = WORDS.index(word)
tries = 1

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    tries += 1
    if tries > 3:
        response = input("Would you like a hint? y or n: ")
        if response.lower() == "y":
            print(HINTS[index])
    guess = input("Your guess: ")
    
if guess == correct:
    print("\nThat's it!  You guessed it!\n")

print("\nThanks for playing.")

input("\n\nPress the enter key to exit.")
