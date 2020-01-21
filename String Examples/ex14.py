#This example is using both argv and input to get information from the user
from sys import argv

#Get the name of the script and the user
script, user_name = argv
prompt = "> "

print (f"Hi {user_name}, I'm the {script} script")
print ("I'd like to ask you a few questions.")
print (f"Do you like me {user_name}?")
likes = input(prompt)

#Entering creepville right now
print (f"Where do you live {user_name}?")
lives = input(prompt)

print ("What kind of computer do you have?")
pc = input(prompt)

print (f"Alright, so you said {likes} about liking me.\nI've also noted you live in {lives}")
print (f"Finally, you said that you own a {pc}")
