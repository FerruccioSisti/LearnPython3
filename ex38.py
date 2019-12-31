#This exercise is working with lists and using the built in functions for them

tenThings = "Apples Oranges Crows Telephones Light Sugar"

print("Wait, there isn't 10 things in that list...lets fix that")

stuff = tenThings.split(" ")
moreStuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    nextOne = moreStuff.pop()
    print("Adding: ", nextOne)
    stuff.append(nextOne)
    print(f"There are {len(stuff)} items now")

print("There we go: ", stuff)

print("Now lets do some things with stuff")

print(stuff[1])
print(stuff[-1]) #print the last item in the list
print(stuff.pop())
#.join uses the given string and puts it between list elements, instead of having a comma and quotes seperate them
print(' '.join(stuff))
print('#'.join(stuff[3:5])) #goes UP TO index 5, but does not include it
