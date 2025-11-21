# Creating two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 1. Union (all elements from both sets)
union_set = set1 | set2
print("Union:", union_set)

# 2. Intersection (common elements)
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# 3. Difference (elements in set1 but not in set2)
difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)

# 4. Symmetric Difference (elements in either set, but not both)
sym_diff_set = set1 ^ set2
print("Symmetric Difference:", sym_diff_set)

# 5. Adding an element
set1.add(6)
print("Set1 after adding 6:", set1)

# 6. Removing an element
set1.remove(2)  # Use discard(2) if you want to avoid errors if 2 is missing
print("Set1 after removing 2:", set1)
