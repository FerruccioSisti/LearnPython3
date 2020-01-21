#Exercise for importing things from one file to another
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Copying contents from {from_file} to {to_file}")

#We are only reading the file to one variable one time, so we dont have to make a variable
#to keep it open since we are only using it in this one case
#Don't need in_file = open(from_file) line
inputData = open(from_file).read()

print (f"The input file is {len(inputData)} bytes long")
print (f"Does the output file exist? : {exists(to_file)}")
print ("Ready.. Hit RETURN to continue, or CRTL-C (^C) to abort..")
input("> ")

#We are only writing the file using a variable we already have, so we dont have to make a variable
#to keep it open since we are only using it in this one case
#Don't need out_file = open(to_file, 'w') line
open(to_file, 'w').write(inputData)

print ("Alright. Copying has been completed..")
#Don't need to close anything since there is no variables set to any open files
#(files were only opened for one thing)
#out_file.close()
#inputData.close()
