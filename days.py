# Input number of days
total_days = int(input("Enter number of days: "))

# Calculate years, months, weeks, and remaining days
years = total_days // 365
remaining_days = total_days % 365

months = remaining_days // 30
remaining_days = remaining_days % 30

weeks = remaining_days // 7
days = remaining_days % 7

# Display the result
print(f"{total_days} days = {years} years, {months} months, {weeks} weeks, {days} days")
