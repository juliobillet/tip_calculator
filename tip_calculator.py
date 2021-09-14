print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))

tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))

total_people = input("How many people to split the bill? ")

#YOU CAN DO IT THE FOLLOWING WAY IF YOU DON'T WANT TO TURN IT TO FLOAT AS I DID RIGHT AWAY, BUT YOU NEED TO TURN IT TO FLOAT AFTERWARDS INSIDE THE total_per_person VARIABLE, AS I COMMENTED BELOW.
# print("Welcome to the tip calculator.")
# total_bill = input("What was the total bill? $")

# tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")

# total_people = input("How many people to split the bill? ")

#LIKE THIS: DECLARING IT ALL AS FLOAT INSIDE THIS VARIABLE BELOW- OTHER THAN WHEN YOU RECEIVE THEM BY THE INPUT FUNCTION, AS I DID ABOVE.
# FOR EXAMPLE:
# total_per_person = (float(total_bill) * float((float(tip_percentage) / 100) + 1)) / float(total_people)

total_per_person = (total_bill * ((tip_percentage / 100) + 1)) / float(total_people)

# using {value:.2f} rounds and set the value to be shown as a decimal number with 2 decimal places
message = f"Each person should pay: ${total_per_person:.2f}."
print(message)
