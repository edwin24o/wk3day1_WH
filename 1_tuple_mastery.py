# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:

# "Itinerary 1: Alice - From New York to London"
#  "Itinerary 2: Bob - From Tokyo to San Francisco"
itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

def flight_itineraries(itineraries):
    for index, (name, origin, destination) in enumerate(itineraries, start=1):
        print(f"Itinerary {index}: {name} - From {origin} to {destination}") 

flight_itineraries(itineraries)

