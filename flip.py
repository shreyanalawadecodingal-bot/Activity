# Original list
binary_list = [0, 1, 1, 0, 0, 1]

# Flip 0 to 1 and 1 to 0
flipped_list = [1 if x == 0 else 0 for x in binary_list]

print("Original List:", binary_list)
print("Flipped List:", flipped_list)
