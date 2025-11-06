# Input conditions
smoke = input("Is smoke detected? (yes/no): ").lower()
temperature = float(input("Enter the temperature in Celsius: "))
flame = input("Is flame detected? (yes/no): ").lower()

# Decision making
if smoke == "yes" or temperature > 50 or flame == "yes":
    print("Alert! Call the Fire Brigade immediately!")
else:
    print("No immediate danger. Fire Brigade not needed.")
