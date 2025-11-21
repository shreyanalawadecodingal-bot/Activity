

from datetime import datetime

def current_datetime():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", current_datetime())
