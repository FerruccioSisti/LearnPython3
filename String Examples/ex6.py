#You can use the 'f' for formatting strings to include variables from other places in your program
#I definitely knew you could do that sort of stuff but am a silly goose

typesOfPeople = 2
statement = f"There are {typesOfPeople} types of people."

binary = "binary"
dont = "do not"
fact = f"those who know {binary}, and those who {dont}."

print (f"I said: {statement}")
print (f"I also said: {fact}")

#There are like a million ways you can write strings I guess
#If you use .format it fills in all the empty brackets {} in your printed string with whatever
#parameters you give it
hilarious = False
jokeEvaluation = "Isn't that joke so funny? {}"
print (jokeEvaluation.format(hilarious))

#You can also concatenate strings to make one big one which I would be surprised if you couldn't do
#It shmushes them together so you need to account for spacing in your strings
w = "This is a "
z = "concatenated string"
print (w + z)
