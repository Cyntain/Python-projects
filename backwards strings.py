# Backwards strings

print("Backwards String Program")
message = input("\nEnter your message: ")

high = len(message)
low = -len(message)
new_word = ""

for i in range(high):
    position = -1 - i
    letter = message[position]
    new_word = new_word + letter

print(new_word)

input("\n\nPress the Enter key to exit.")
