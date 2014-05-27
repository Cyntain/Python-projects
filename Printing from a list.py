# Printing words from a list

# Imports
import random

WORDS = ["Words", "Chapter", "Task", "Printing", "From"]

# Delete from list then print what was deleted loop
while len(WORDS) != 0:
    index = random.randrange(len(WORDS))
    print(WORDS.pop(index))

input("\n\nPress the Enter key to exit")
    
