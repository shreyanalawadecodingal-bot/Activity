# Sample list
numbers = [1, 2, 3, 4, 5]

# Function to square a number
def square(x):
    return x ** 2

# Using map to apply square function to each element
squared_numbers = list(map(square, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
