import random
from datetime import datetime, timedelta

def random_datetime(start_year=2000, end_year=2035):
    # Create random date
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)

    random_seconds = random.randint(0, int((end - start).total_seconds()))
    dt = start + timedelta(seconds=random_seconds)

    return dt.strftime("%Y-%m-%d %H:%M:%S")

# Example
print("Random Date and Time:", random_datetime())
