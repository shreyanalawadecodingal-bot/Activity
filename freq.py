# Sample dictionary
data = {
    "apple": 3,
    "banana": 5,
    "cherry": 3,
    "date": 2,
    "banana": 4  # Duplicate key in dict will override previous value
}

# Count frequency of keys in a list of keys (example)
keys_list = ["apple", "banana", "cherry", "apple", "banana", "banana"]

# Using dictionary to count frequency
frequency = {}
for key in keys_list:
    if key in frequency:
        frequency[key] += 1
    else:
        frequency[key] = 1

print("Key Frequency:", frequency)
