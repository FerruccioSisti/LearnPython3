from sys import exit

def goldRoom():
    print("This room is full of gold. How much do you take")

    choice = input("> ")
    if '0' in choice or '1' in choice:
        howMuch = int(choice)
    else:
        dead("Man, learn to type a number")

    if howMuch < 50:
        print("Nice, you're not greedy. You win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bearRoom():
    print("There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bearMoved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and slaps your STUPID face off")
        elif choice == "taunt bear" and not bearMoved:
            print("The bear has moved from the door\nYou can go through it now")
            bearMoved = True
        elif choice == "open door" and bearMoved:
            goldRoom()
        else:
            print("I got no clue what that means homie")

def cthuluRoom():
    print("Here you see the great evil Cthulu\nHe, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthuluRoom()

def dead(why):
    print(why, "Nice!")
    exit(0)

def start():
    print("You are in a dark room\nThere is a door to both your right and your left")
    print("Which door do you take")

    choice = input("> ")

    if choice == "left":
        bearRoom()
    elif choice == "right":
        cthuluRoom()
    else:
        dead("You stumble around the room until you starve")

start()
