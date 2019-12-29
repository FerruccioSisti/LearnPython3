#Exercise asking the user for input to work with if/else

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")
door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake\nWhat will you do?")
    print("1. Take the cake\n2. Scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Nice!")
    elif bear == "2":
        print("The bear eats your legs off. Nice!")
    else:
        print(f"Well, doing {bear} is probably better..\n**Bear runs away**")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries\n2. Yellow Jacket Clothespins\n3. Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives, powered by a mind of jello\nNice!")
    else:
        print("The insanity rots your eyes into a pool of muck\nNice!")

else:
    print("You stumble around and fall on a knife and die. Nice!")
