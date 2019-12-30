#Exercise using lists and for loops

theCount = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#The first loops we are going to do iterates through the lists
for number in theCount:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

#We can also build a list if we wanted to
elements = []

#Then we can use the range function to help us add stuff in a loop
for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i)

#Now we will print our new list
for i in elements:
    print(f"Element was: {i}")
