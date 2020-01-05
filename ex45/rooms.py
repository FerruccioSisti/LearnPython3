#This file contains all the classes for the different rooms
from sys import exit
from textwrap import dedent
from random import randint

#Base class for the rooms
class Room(object):
    #Method for what happens when you enter a room
    def enter(self):
        print("This is the default room, you did something wrong")
        print("Make a subclass to use instead (don't forget to implement enter()!)")
        exit(1)

class Death(Room):
    #Different quips you can get from losing the game
    quips = [
        "OUHHH THIS'LL STING ALOT",
        "Nice game lul",
        "Have you tried getting gooder?",
        "You might want to consider uninstalling",
        "lol noob"
    ]
    #Method for what happens when you enter a room
    def enter(self):
        print("\n", "*" * 10, "\n")
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

class Finished(Room):
    #Method called when you win the game
    def enter(self):
        print("\n", "*" * 10, "\n")
        print("Congrats! You won! Bet you didn't see that weird shiz coming amirite")
        return "finished"

class PannittoHouse(Room):
    #Method for what happens when you enter the starting room
    def enter(self):
        print(dedent("""
            wha.... whats going on here...
            this looks like the Pannitto house...
            **You run to the nearest window and look outside
            It's the dead of night but you can tell by the surroundings that
            your suspicions were right. You're somehow in Simon's house**
            You can't seem to find anybody with you in the house. Its quiet..
            too quiet..

            You should try to see if anybody is home to help you!
            Do you:
            a) Freak out and open the front door and run outside
            b) Tiptoe over to Simon's room to see if he is in there
            c) Run to his parents room and frantically hammer on the door
            d) Reluctantly approach Julia's room as a desperate attempt to get help
        """))

        action = input("> ")

        if action == "a":
            print("\n", "*" * 10, "\n")
            return "outside"
        elif action == "b":
            print("\n", "*" * 10, "\n")
            return "simons_room"
        elif action == "c":
            print("\n", "*" * 10, "\n")
            return "parents_room"
        elif action == "d":
            print("\n", "*" * 10, "\n")
            return "julias_room"
        else:
            print("Why are you difficult? You just broke the game my dude")
            print("\n-----RELOADING ROOM-----\n")
            return "pannitto_house"

class Outside(Room):
    #Method for what happens when you try and escape outside
    def enter(self):
        print(dedent("""
            You open the door and run outside....and he's waiting there for you
            That's right...doubleyuh, George doubleyuh that is
            He embraces you with open arms
            "I was so worried! What happened?" says George
            You answer that you don't have any recent recollection of the events
            that transpired this night and step into the limo sitting idle there
            with the former president
        """))
        return "finished"

class SimonsRoom(Room):
    #Method for what happens when you enter simon's room
    def enter(self):
        print(dedent("""
            You tiptoe over to Simon's room.. The door is left open ajar
            You slowly creak open the door and see he is asleep in his bed
            You inch closer and notice that he is cuddling his anime waifu
            body pillow and muttering in his sleep

            "Let's say you've been a bad girl. Let's say, hypotethically, you've
            been a naughty girl even. ok, and if you were a naughty girl you
            would also be my dirty little slut right? then hypotethically
            speaking you would be my little cumslut. now let's say that you're
            also a daddy's girl..."

            Do you:
            a) Gently wake him up and try to get him to help you figure out the
            bizarre situation you find yourself in
            b) Aggressively wake him up by assaulting him for being a pedo creep
            c) Slowly leave the room, and head back to the main corridor
        """))

        action = input("> ")

        if action == "a":
            print(dedent("""
                Simon wakes up and panicks..
                "You weren't supposed to wake up for another few hours" he says
                He jumps out of bed and walks over to his dresser
                He takes the katana he has hidden there and stabs you like the
                true weeaboo he is deep down inside

                You die within a few minutes
            """))
            return "death"
        elif action == "b":
            print(dedent("""
                Simon wakes up in a rage!
                He jumps out of bed and grabs his hidden katana
                "NYARHGG" screeches Simon as he slashes you down
                "I have truly ascended to anime god tier villain" gloats the
                neckbeard

                You die within a few minutes
            """))
            return "death"
        elif action == "c":
            print(dedent("""
                You slowly creep out of the room without disturbing him
                "What a frickin weeb" you think to yourself as you head back to
                the main corridor
            """))
            return "pannitto_house"
        else:
            print("That wasn't an option you frickin numpty")
            print("\n-----RELOADING ROOM-----\n")
            return "simons_room"

class ParentsRoom(Room):
    #Method that gets called when the parents room is entered
    def enter(self):
        print(dedent("""
            The door swings open with the force of your knocks
            You slowly creep forwards into the room and yack with the sheer
            horror of what you see on the bed..

            Simon's parents have been turned into anime body pillows! There's
            only one person who could've done this....Simon...

            You hear something behind you..
            You have barely any time to react
            Do you:
            a) Grab the glock off the nightstand
            b) Turn around without thinking
            c) Hide
        """))

        action = input("> ")

        if action == "a":
            print(dedent("""
                You grab the glock just sitting there. It's already loaded
                You turn around to face the doorway and there he stands
                Simon sees that you noticed him and begins to charge you with
                his katana in hand.

                *POP*
                *POP*

                Two shots and he goes down
                "YOU HAVE DEFEATED ME! NYARHGG"
            """))
            return "finished"
        elif action == "b":
            print(dedent("""
                You panick and turn around as fast as you can.
                "I need to get the FRICK out of here" you think to yourself

                As you turn around you get a vague glimpse of Simon in the
                shadows. He jumps forward, katana raised, and with a mighty
                scream "NYARHGG" he strikes you down

                You die within minutes
            """))
            return "death"
        elif action == "c":
            print(dedent("""
                You panick and dive under the bed in a futile attempt to hide..
                He enters the room.. It's Simon..
                You peak out from under the covers only to find him standing
                right there as he searches to find you
                "NYARHGG!" he screams as he brings his mighty katana down over
                your neck

                You die instantly
            """))
            return "death"
        else:
            print("That wasn't an option you frickin numpty")
            print("\n-----RELOADING ROOM-----\n")
            return "parents_room"

class JuliasRoom(Room):
    #Method that gets called when user chooses Julia's room
    def enter(self):
        print(dedent("""
            You head over in the direction of Julia's room
            Reluctantly, you approach the door
            You hear weird noises... those sound like grunts
            You swing the door open and see REEEEEANN furiously powerlifting
            You think to yourself "That guy is curling 420 lbs in each arm what
            the FRICK"
            Julia is sitting on her bed, watching this God among men do this
            with ease
            They notice you UwU

            With the rage of 1000 suns, Julia rips the weights out of Rian's
            gorgeous arms and chucks them at your face

            My dude, you are deader than dead
        """))
        return "death"
