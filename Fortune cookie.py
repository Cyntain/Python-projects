# Fortune Cookie program

# Imports
import random

#random fortune
fortune = random.randint(1, 5)

fortune_1 = "Look up to see more!"
fortune_2 = "Read more!"
fortune_3 = "Close your mouth when you eat!"
fortune_4 = "Don't be judgemental!"
fortune_5 = "Hans shot first"

if fortune == 1 :
    print(fortune_1)
elif fortune == 2 :
    print(fortune_2)
elif fortune == 3 :
    print(fortune_3)
elif fortune == 4 :
    print(fortune_4)
elif fortune == 5 :
    print(fortune_5)
else :
    print("Invalid number")

input("\n\nPress the Enter key to exit.")
