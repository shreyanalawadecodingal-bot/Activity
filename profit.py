# Input Cost Price and Selling Price
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

# Calculate Profit or Loss
if sp > cp:
    profit = sp - cp
    print(f"Profit = {profit}")
elif cp > sp:
    loss = cp - sp
    print(f"Loss = {loss}")
else:
    print("No Profit, No Loss")
