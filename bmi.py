# Input weight (kg) and height (m)
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI
print(f"Your BMI is: {bmi:.2f}")

# Determine BMI category
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You have Normal weight")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")
