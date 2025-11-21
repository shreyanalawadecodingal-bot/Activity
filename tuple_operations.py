# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# 2. Slicing
print("Slice (1 to 3):", my_tuple[1:4])

# 3. Length of tuple
print("Length of tuple:", len(my_tuple))

# 4. Concatenation
tuple2 = (60, 70)
new_tuple = my_tuple + tuple2
print("Concatenated tuple:", new_tuple)

# 5. Repetition
print("Repeated tuple:", my_tuple * 2)

# 6. Membership test
print("Is 30 in tuple?", 30 in my_tuple)

# 7. Iteration
print("Elements in tuple:")
for item in my_tuple:
    print(item)
