#This example is basically working with while loops (VERY SIMPLE)
i = 0
numbers = []

while i < 6:
    #print the current index of i and add it to the list
    print(f"At the top of i is {i}")
    numbers.append(i)

    #increment i by one 
    i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
