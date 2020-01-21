#Exercise practicing else/if statements

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We shouldn't take the cars")
else:
    print("We can't decide")

if trucks > cars:
    print("Thats too many trucks hombre")
elif trucks < cars:
    print("Maybe we can take the trucks")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, lets just take the trucks")
else:
    print("Fine, lets stay home then")
