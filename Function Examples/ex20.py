#Mixing functions with file IO
from sys import argv

script, inputFile = argv

#Function prints whatever file is passed as a parameter
def printAll(f):
    print (f.read())

#Function sets the cursor? back to the start of the file
def rewind(f):
    f.seek(0)

#Function prints a specific line of a file
def printALine(lineCount, f):
    print(lineCount, f.readline())

currentFile = open(inputFile)

print("First, lets print out the entire file\n")
printAll(currentFile)

print("Now lets rewind it, kind of like a tape")
rewind(currentFile)

#Realistically we should be doing a for loop for this part but since we haven't 'learned' it yet I won't
print("Now, lets print the first three lines")
currLine = 1
printALine(currLine, currentFile)
currLine = currLine + 1
printALine(currLine, currentFile)
currLine = currLine + 1
printALine(currLine, currentFile)
