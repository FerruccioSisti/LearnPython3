#Working with file IO before doing anything with loops feelsweirdman
from sys import argv

#get the name of the file we are reading from the command line argument
script, filename = argv

txt = open(filename)

print (f"Here are the contents of the file {filename}:\n")
print (txt.read())

print ("\nType the file name again please: ")
file_again = input ("> ")
txt_again = open(file_again)
print (txt_again.read())
