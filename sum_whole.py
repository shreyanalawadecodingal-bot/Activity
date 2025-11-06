# Input: upper limit
n = int(input("Enter a number: "))

# Initialize sum
total = 0

# Loop from 0 to n
for i in range(n + 1):
    total += i  # Add each number to total

print("Sum of whole numbers from 0 to", n, "is:", total)
