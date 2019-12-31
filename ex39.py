#This example teaches dict in python, which looks to be literally a hashmap

#Create a map of states to abbreviations
states = {"Oregon": "OR", "Florida": "FL", "California": "CA", "New York": "NY", "Michigan":"MI"}

#Create a basic set of states and some cities in them
cities = {"CA": "San Francisco", "MI": "Detroit", "FL": "Jacksonville"}

#add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

#Print out some cities
print(" - " * 10)
print("NY state has: ", cities["NY"])
print("OR state has: ", cities["OR"])

#Print some states
print(" - " * 10)
print("Michigan's state abbreviation is: ", states["Michigan"])
print("Florida's state abbreviation is: ", states["Florida"])

#Now do it by using the state then cities dict
print(" - " * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

#Print every state abbreviation
print(" - " * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print(" - " * 10)
for abbrev, city in list(cities.items()):
    print(f"{city} is in {abbrev}")

#Now do both at the same time
print(" - " * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev} and has cities {cities[abbrev]}")

#Safely get an abbreviation for a state that might not exist
state = states.get("Texas")

if not state: #If state is not assigned to anything because it doesnt exist
    print("Sorry, no Texas")

#Get a city with a default value
city = cities.get("TX", "Does not exist")
print(f"The city for the state 'TX' is: {city}")
