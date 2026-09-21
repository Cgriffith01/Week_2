#Tip calculator exercise (Week 2)

cost = input("What is the total cost of the meal?: ")

try:
    cost = float(cost)
except ValueError:
    print("Please enter a valid number for the meal cost.")
else:
    tip_15 = cost * .15
    tip_18 = cost * .18
    tip_20 = cost * .20

    total_15 = cost + tip_15
    total_18 = cost + tip_18
    total_20 = cost + tip_20

    print(f"A 15% tip would be ${tip_15:.2f}. This brings the total to ${total_15:.2f}.")
    print(f"A 18% tip would be ${tip_18:.2f}. This brings the total to ${total_18:.2f}.")
    print(f"A 20% tip would be ${tip_20:.2f}. This brings the total to ${total_20:.2f}.")
