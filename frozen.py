# Creating a frozenset
fs = frozenset([1, 2, 3, 4, 5])

print("Frozenset:", fs)

# Accessing elements (iteration)
print("Elements in frozenset:")
for item in fs:
    print(item)

# Set operations
fs2 = frozenset([4, 5, 6, 7])

# Union
print("Union:", fs | fs2)

# Intersection
print("Intersection:", fs & fs2)

# Difference
print("Difference (fs - fs2):", fs - fs2)
