#Function time

#Function that works like argv
def printTwo(*args):
    arg1, arg2 = args
    print (f"arg1: {arg1}, arg2: {arg2}")

#Doing *args is lowkey pointless
def printTwoAgain(arg1, arg2):
    print (f"arg1: {arg1}, arg2: {arg2}")

#This one only takes one argument
def printOne(arg1):
    print (f"arg1: {arg1}")

#This one doesn't take any arguments
def printNone():
    print ("I got nothin")

printTwo("Zed", "Shaw")
printTwoAgain("Zed", "Shaw")
printOne("First!")
printNone()
