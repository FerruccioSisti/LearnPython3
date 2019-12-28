#Simple text editor exercise
from sys import argv

script, filename = argv

print (f"We are going to erase {filename}.")
print ("If this is not okay, hit CTRL-C (^C).")
print ("If this is okay, hit RETURN/ENTER")

#Prompts the user to do input on their keyboard but doesn't actually save it to a variable
input("?")

print ("Opening the file...")
#Open the file for writing
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
#Truncating erases the contents of the file
target.truncate()

print ("Now I will ask for 3 lines of input")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print ("I will write these to the file")

target.write(line1 + "\n" + line2 + "\n" + line3)

print ("Finally, we can close the file")
target.close()
