#This exercise is basically the previous one, except it is meant to be short and entirely on our own
from sys import exit

#red room option from starting room
def redRoom():
    print("Everything in this room is red. You can't see any objects other than the outline of the door.")
    print("Do you try and go out the door ?")
    choice = input ("> ")

    if choice == "yes":
        print("you trip over some red spikes and die\nNice")
        exit()
    elif choice == "no":
        print("you don't move out of fear and starve to death\nNice")
        exit()
    else:
        print("idk what that means bro")
        redRoom()

#blue room option from starting room
def blueRoom():
    print("Everything in this room is blue. You can't see any objects other than the outline of the door.")
    print("Do you try and go out the door ?")
    choice = input("> ")

    if choice == "yes":
        print("the door leads outside\nNice")
        exit()
    elif choice == "no":
        print("you didn't notice the room filling up with water and drowned\nNice")
        exit()
    else:
        print("idk what that means bro")
        blueRoom()

#starting room
def startRoom():
    print("You awake sleeping on a couch in a bizarre room\nThere are two coloured doors on the opposite side of the room")
    print("Do you take the blue door or the red door ?")
    choice = input("> ")

    if choice == "blue":
        print("You choose the blue door")
        blueRoom()
    elif choice == "red":
        print("You choose the red door")
        redRoom()
    else:
        print("idk what that means bro\nYou gotta say red or blue")
        startRoom()

startRoom()
