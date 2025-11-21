import random

def send_well_wish(name):
    wishes = [
        "Wishing you a wonderful day filled with joy!",
        "May success and happiness follow you always!",
        "Sending positive thoughts your way!",
        "Hope your day is as amazing as you are!",
        "May your week be full of blessings and smiles!",
        "Wishing you good health and great achievements!",
        "May all your dreams take flight today!"
    ]
    
    wish = random.choice(wishes)
    return f"Hello {name}! {wish}"

# Example usage:
print(send_well_wish("Alice"))
