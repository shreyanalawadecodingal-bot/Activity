# Input: upper limit
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Loop from n down to 0
for i in range(n, -1, -1):  # start=n, stop=-1, step=-1
    total += i  # Add each number to total

print("Sum of whole numbers from", n, "down to 0 is:", total)
