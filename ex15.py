#Working with file IO before doing anything with loops feelsweirdman
from sys import argv

#get the name of the file we are reading from the command line argument
script, filename = argv

#opens the file with name given as an argument in the command line
txt = open(filename)

print (f"Here are the contents of the file {filename}:\n")
#Calls the read function with the opened file in order to display its contents
print (txt.read())
txt.close()

print ("\nType the file name again please: ")
file_again = input ("> ")
txt_again = open(file_again)
print (txt_again.read())
txt_again.close()
