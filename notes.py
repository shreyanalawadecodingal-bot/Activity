# Input the amount
amount = int(input("Enter the amount: "))

# List of available notes in descending order
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# Dictionary to store count of each note
note_count = {}

remaining_amount = amount

for note in notes:
    count = remaining_amount // note  # number of notes of this denomination
    if count > 0:
        note_count[note] = count
        remaining_amount = remaining_amount % note  # remaining amount after using these notes

# Display the result
print(f"\nBreakdown of ₹{amount} into notes:")
for note, count in note_count.items():
    print(f"₹{note} x {count}")
