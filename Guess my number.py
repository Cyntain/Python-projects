# Guess My Number

import random  

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
attempts = 6
# guessing loop
while guess != the_number and tries < attempts:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
            
    guess = int(input("Take a guess: "))
    tries += 1

if tries > attempts - 1:
    print("You did not manage to guess the number!")
elif guess == the_number:
    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
