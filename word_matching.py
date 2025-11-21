# List of words to check
list1 = ["apple", "banana", "cherry", "date"]
list2 = ["banana", "date", "fig", "grape"]

# Find matching words
matching_words = [word for word in list1 if word in list2]

print("Matching words:", matching_words)
