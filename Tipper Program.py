#Program

print("The Tipper program\n")

# Inputing the amount without a tip
bill_total = int(input("The total bills amount: "))

# caculating the tip
total_20 = (bill_total * 0.20) + bill_total
total_15 = (bill_total * 0.15) + bill_total

# Show the user the bill
print("The bill came to: £", total_20, " with a 20% tip\n Or \nThe bill came to: £",
      total_15, " with a 15% tip")

input("\n\nPress enter key to exit")
