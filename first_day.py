import random

def first_day_experience(category="trip"):
    experiences = {
        "trip": [
            "My first day of the trip was amazing! I explored new places, tried local food, and enjoyed the fresh atmosphere.",
            "On the first day of my trip, I walked around the city, took beautiful photos, and felt excited for the days ahead.",
            "The first day of my journey was full of adventure—new sights, new sounds, and a lot of fun moments."
        ],
        "school": [
            "My first day of school was exciting. I met my new classmates, got my timetable, and felt ready for the year.",
            "On my first day of school, I was nervous at first, but my teacher was kind and helped me settle in.",
            "The first day of school was fun—I made new friends and explored the different classrooms."
        ],
        "work": [
            "My first day at work was busy but enjoyable. I met my team and learned about my responsibilities.",
            "On my first day of work, everyone was welcoming, and I quickly felt comfortable in my new role.",
            "The first day at my new job was full of introductions, training, and excitement for what’s ahead."
        ]
    }

    return random.choice(experiences.get(category, ["Invalid category."]))

# Example:
print(first_day_experience("trip"))
print(first_day_experience("school"))
print(first_day_experience("work"))
