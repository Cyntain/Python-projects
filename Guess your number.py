# Number guessing game

#imports
import random

# Welcome player to the game 
print("""
Welcome to the Number Guessing Game!\n
My job will be to guess your number!\n\n
""")

# Variables
tries = 1
low_num = 0
high_num = 100

players_num = int(input("Enter your number, which is between 1-100: "))
guess = random.randint(low_num, high_num)

#guessing loop
while  guess != players_num:
    print(guess)
    response = input("Is it higher or lower?")
# Player tells the computer if higher or lower and adjusts the parameters
    if response.lower() == "higher":
        low_num = guess + 1
    else:
        high_num = guess - 1
        
    tries += 1
    guess = random.randint(low_num, high_num)

#Finish the game, tell the player number of tries and the number the game guessed
print("I guessed it in", tries, "attempts!")
print("The number was", guess)

input("\n\nPress the Enter Key to exit.")
