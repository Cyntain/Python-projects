# Character creation program
# Version 2

print(
"""
Character Skill points!
- Version 2
- Starting skill point pool = 30
""")

choice = None
skill_pool = 30
char_skill = {
    "Strength": 10,
    "Health": 10,
    "Wisdom": 6,
    "Dexterity": 5
    }
KEYS = ("Strength", "Health", "Wisdom", "Dexterity")
length = len(char_skill)

# Main loop
while choice != 0:
    print(
        """
0 - Exit
1 - Continue to edit skill points
        """
        )
    choice = input("Choice: ")
    print()

# end the loop
    if choice == "0":
        print("good-bye!")
        break

# print out all skills and points
    elif choice == "1":
        for i in range(length):
            term = KEYS[i]
            print(term, " : ", char_skill[term])
        response = input("What skill would you like to edit?")

# Strength
        if response.lower() == KEYS[0].lower():
            key = KEYS[0]
            print("\n" + key, " : ", char_skill[key])
            print("Skill pool : ", skill_pool)
            add_or_minus = input("\nWould you like to take or add skill points? ")
            skill_points = int(input("How many skill points do you want to move?"))

            if add_or_minus.lower() == "add":
                value = char_skill[key] + skill_points
                skill_pool = skill_pool - skill_points
                char_skill[key] = value
            elif add_or_minus.lower() == "take":
                value = char_skill[key] - skill_points
                skill_pool = skill_pool + skill_points
                char_skill[key] = value
            else:
                print("Unknown Choice")

# Health
        elif response.lower() == KEYS[1].lower():
            key = KEYS[1]
            print("\n" + key, " : ", char_skill[key])
            print("Skill pool : ", skill_pool)
            add_or_minus = input("\nWould you like to take or add skill points? ")
            skill_points = int(input("How many skill points do you want to move?"))

            if add_or_minus.lower() == "add":
                value = char_skill[key] + skill_points
                skill_pool = skill_pool - skill_points
                char_skill[key] = value
            elif add_or_minus.lower() == "take":
                value = char_skill[key] - skill_points
                skill_pool = skill_pool + skill_points
                char_skill[key] = value
            else:
                print("Unknown Choice")

# Widsom
        elif response.lower() == KEYS[2].lower():
            key = KEYS[2]
            print("\n" + key, " : ", char_skill[key])
            print("Skill pool : ", skill_pool)
            add_or_minus = input("\nWould you like to take or add skill points? ")
            skill_points = int(input("How many skill points do you want to move?"))

            if add_or_minus.lower() == "add":
                value = char_skill[key] + skill_points
                skill_pool = skill_pool - skill_points
                char_skill[key] = value
            elif add_or_minus.lower() == "take":
                value = char_skill[key] - skill_points
                skill_pool = skill_pool + skill_points
                char_skill[key] = value
            else:
                print("Unknown Choice")

# Dexterity
        if response.lower() == KEYS[3].lower():
            key = KEYS[3]
            print("\n" + key, " : ", char_skill[key])
            print("Skill pool : ", skill_pool)
            add_or_minus = input("\nWould you like to take or add skill points? ")
            skill_points = int(input("How many skill points do you want to move?"))

            if add_or_minus.lower() == "add":
                value = char_skill[key] + skill_points
                skill_pool = skill_pool - skill_points
                char_skill[key] = value
            elif add_or_minus.lower() == "take":
                value = char_skill[key] - skill_points
                skill_pool = skill_pool + skill_points
                char_skill[key] = value
            else:
                print("Unknown Choice")
    else:
        print("Unknown Choice!")
input()
