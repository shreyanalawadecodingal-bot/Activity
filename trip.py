def trip_expense(transport, hotel, food, activities, misc=0):
    total = transport + hotel + food + activities + misc
    return total

# Example:
total = trip_expense(120, 350, 140, 90, 30)
print("Total Trip Expense: $", total)
