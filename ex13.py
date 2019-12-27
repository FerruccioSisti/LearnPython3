#This example uses command line arguments when running the script to get input
from sys import argv

#This takes command line arguments and assigns them in a leftmost order
#The last argument will be assigned to third, second last to second, etc
script, first, second, third = argv

print ("The script is called: ", script)
print ("The first variable is: ", first)
print ("The second variable is: ", second)
print ("The third variable is: ", third)
