# Character creation program
# Version 1

print(
    """
Character Skill Points!
- Version 1
- Maxium skill points = 30\n\n
--------------------------------------------------------------------------------
"""
    )

choice = None
skill_points = 30
char_skills = {
    "Strength": 0,
    "Health": 0,
    "Wisdom": 0,
    "Dexterity": 0
    }

# Main loop
while choice != "0":  
    print(
        """
----------------------------------------------------
0 - Quit                                     
1 - Add skill points to Strength   
2 - Add skill points to Health
3 - Add skill points to Widsom
4 - Add skill points to Dexterity
5 - Show all skill points
----------------------------------------------------
"""
        )
    choice = input("\t\tChoice: ")
    print()

# 0 - Quit
    if choice == "0":
            print("\nGood-Bye!")
            
# 1 - Add skill points to Strength
    elif choice == "1":
        term = "Strength"
            
        if term in char_skills:
            print("Skill points in ", term, " ", char_skills[term])
            print("Remaining skill points: ", skill_points)     
            response = input("\nWould you like to add a skill point to Strength? y or n: ")

            # Adding skill points
            if response.lower() == "y":
                skill_to_add = int(input("How many skill points would you like to add to Strength:" ))
                value = char_skills[term] + skill_to_add
                skill_points = skill_points - skill_to_add
                
                if skill_points <= 0:
                    print("\nOut of skill points!")
                    break
                else:
                    char_skills[term] = value
                    print("\n\t\tSkill points in", term, " ", char_skills[term])
                    
            # Removes skill points
            else:
                skill_to_remove = int(input("How many skill points to remove from Strength: "))
                value_remove = char_skills[term] - skill_to_remove
                skill_points = skill_points + skill_to_remove
                char_skills[term] = value_remove
                
                print("\n\t\tSkill points in", term, ": ", char_skills[term])
        else:
            print("Unknown Skill")
            
# 2 - Add skill points to Health
    elif choice == "2":
        term = "Health"
            
        if term in char_skills:
            print("Skill points in ", term, " ", char_skills[term])
            print("Remaining skill points: ", skill_points)
            response = input("\nWould you like to add a skill point to Health? y or n: ")
            
            # Adding skill points
            if response.lower() == "y":  
                skill_to_add = int(input("How many skill points would you like to add to Health:" ))
                value = char_skills[term] + skill_to_add
                skill_points = skill_points - skill_to_add
                
                if skill_points <= 0:
                    print("Out of skill points!")
                    break
                else:
                    char_skills[term] = value
                    print("\n\t\tSkill points in", term, " ", char_skills[term])
                    
            # Removes skill points
            else:
                skill_to_remove = int(input("How many skill points to remove from Health: "))
                value_remove = char_skills[term] - skill_to_remove
                skill_points = skill_points + skill_to_remove
                char_skills[term] = value_remove
                
                print("\n\t\tSkill points in", term, ": ", char_skills[term])
        else:
            print("Unknown skill")

# 3 - Add skill points to Wisdom
    elif choice == "3": 
        term = "Wisdom"
            
        if term in char_skills:
            print("Skill points in ", term, " ", char_skills[term])
            print("Remaining skill points: ", skill_points)          
            response = input("\nWould you like to add a skill point to Wisdom? y or n: ")
            
            # Adding skill points
            if response.lower() == "y":   
                skill_to_add = int(input("How many skill points would you like to add to Wisdom:" ))
                value = char_skills[term] + skill_to_add
                skill_points = skill_points - skill_to_add
                
                if skill_points <= 0:
                    print("Out of skill points!")
                    break
                else:
                    char_skills[term] = value
                    print("\n\t\tSkill points in", term, ": ", char_skills[term])

            # Removes skill points
            else:
                skill_to_remove = int(input("How many skill points to remove from Wisdom: "))
                value_remove = char_skills[term] - skill_to_remove
                skill_points = skill_points + skill_to_remove
                char_skills[term] = value_remove
                
                print("\n\t\tSkill points in", term, " ", char_skills[term])
        else:
            print("Unknown skill")

# 4 - Add skill points to Dexterity
    elif choice == "4":     
        term = "Dexterity"
            
        if term in char_skills:
            print("Skill points in ", term, " ", char_skills[term])
            print("Remaining skill points: ", skill_points)
            response = input("\nWould you like to add a skill point to Dexterity? y or n: ")

            # Adding skill points
            if response.lower() == "y":
                skill_to_add = int(input("How many skill points would you like to add to Dexterity:" ))
                value = char_skills[term] + skill_to_add
                skill_points = skill_points - skill_to_add
                
                if skill_points <= 0:
                    print("Out of skill points!")
                    break
                else:
                    char_skills[term] = value
                    print("\n\t\tSkill points in", term, " ", char_skills[term])

            # Removes skill points
            else:
                skill_to_remove = int(input("How many skill points to remove from Dexterity: "))
                value_remove = char_skills[term] - skill_to_remove
                skill_points = skill_points + skill_to_remove
                char_skills[term] = value_remove

                print("\n\t\tSkill points in", term, " ", char_skills[term])
        else:
            print("Unknown skill")
            
# 5 - Print out all skills and points
    elif choice == "5":
        keys = ("Strength", "Health", "Wisdom", "Dexterity")
        length = len(keys)
        print("\t\t----Skill points----")
        for i in range(length):
            term = keys[i]
            print("\t\t", keys[i], " : ", char_skills[term]) 
    else:
        print("Unknown choice!")

input("\n\nPress the Enter key to exit.")
    
