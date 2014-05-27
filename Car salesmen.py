# Car sales man program

# Welcome to the program
print("Welcome to the Car Sales Man Program!\n\n")


#Input base amount

price = int(input("Please enter the base price of the car: "))
print("\nPrice of the car without taxes: £", price)

# Add taxes 
tax = 0.21
dealer_prep = 0.1
dest_tax = 0.05
license = 0.1

total_tax = tax + dealer_prep + dest_tax + license

new_price = (price * total_tax) + price

# Print price with taxes
print("The price of the car with taxes is: £", new_price)

input("\n\nPress the Enter key to exit.")
