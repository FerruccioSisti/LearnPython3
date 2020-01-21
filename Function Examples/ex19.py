#Exercise demonstrating that variables in functions aren't connected to the rest of the ones in the script

def cheeseAndCrackers (cheeseCount, crackerCount):
    print (f"You have {cheeseCount} cheeses")
    print (f"You have {crackerCount} boxes of crackers")
    print ("Man, thats enough for a party!\nLets get a blanket\n")

print ("We can give the function numbers directly: ")
cheeseAndCrackers(20, 30)

print("OR we can use variables from our script: ")
amtCheese = 10
amtCracker = 50

cheeseAndCrackers(amtCheese, amtCracker)

print ("We can also do math inside the function: ")
cheeseAndCrackers(10 + 20, 5 * 6)

print ("AND we can combine both variables and math")
cheeseAndCrackers(amtCheese + 5, amtCracker * 2)
