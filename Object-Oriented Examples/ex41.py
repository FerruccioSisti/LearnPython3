#This program has a series of questions related to classes and functions in python
#It will ask you a random question from the list of phrases, give you a chance to try and answer
#and then display the correct answer
#it uses random variable names from a list given by the textbook

import random
from urllib.request import urlopen
import sys

wordURL = "http://learncodethehardway.org/words.txt"
words = []

#String in hashmap format with answers and questions
phrases = {
"class %%%(%%%):":
"Make a class named %%% that is a %%%.",
"class %%%(object):\n\tdef __init__(self, ***)" :
"class %%% has-a __init__ that takes self and *** params.",
"class %%%(object):\n\tdef ***(self, @@@)":
"class %%% has-a function *** that takes self and @@@ params.",
"*** = %%%()":
"Set *** to an instance of class %%%.",
"***.***(@@@)":
"From *** get the *** function, call it with params self, @@@.",
"***.*** = '***'":
"From *** get the *** attribute and set it to '***'."
}

#Do they want to drill phrases first
#Check for proper input and that they want them in english
if len(sys.argv) == 2 and sys.argv[1] == "english":
    phraseFirst = True
else:
    phraseFirst = False

#load the words from the website
#goes through every line in the URL
for word in urlopen(wordURL).readlines():
    #Add it to our list of strings after stripping the trailing spaces, etc with strip
    words.append(str(word.strip(), encoding = "utf-8"))

def convert(snippet, phrase):
    #capitalizes the first character of a class name
    #obtained by getting a list the size of the amount of '%%%' in the snippet
    #and randomly picking that many items from 'words' and capitalizing the first characters
    classNames = [w.capitalize() for w in random.sample(words, snippet.count("%%%"))]
    #gets a list of other names by looking how many we need (snippet.count(***))
    #and randomly picking that many from 'words'
    otherNames = random.sample(words, snippet.count("***"))
    results = []
    paramNames = []

    #loops once for every time we need to use parameters in our snippet (params are @@@)
    for i in range (0, snippet.count("@@@")):
        #Gets a random integer from 1-3 inclusive representing the amount of parameters
        paramCount = random.randint(1, 3)
        #randomly picks words to use as parameters from the list (picks 1, 2, or 3 random params)
        #Seperates each param by a comma for proper syntax
        paramNames.append(', '.join(random.sample(words, paramCount)))

    for sentence in snippet, phrase:
        #copies a list using list slice syntax
        #copies the list from x to y-1 --> [x:y]
        #if no x and y it copies the entire list
        result = sentence[:]

        #Fake class names
        for word in classNames:
            #replace the occurance of %%% with what the class name is going to be
            #only replacing the first one with the name so we only put 1 for the count
            result = result.replace("%%%", word, 1)

        #Fake other names
        for word in otherNames:
            #replace all the other names that are in the snippet (they occur at ***)
            #only replacing the first one with that specific string so only 1 for count
            result = result.replace("***", word, 1)

        #Fake parameter lists
        for word in paramNames:
            #replace all the @@@ in the snippet with the randomized param names
            #each param name is only used once so thats why count is 1
            result = result.replace("@@@", word, 1)

        #Our new string with everything properly replaced is results so add the stuff to it
        results.append(result)

    return results

#Keep it going until they hit CTRL-D (^D)
try:
    while True:
        #snippets is a list of all the keys (the answers from the first string in this script)
        snippets = list(phrases.keys())
        #shuffle the order of the list so it is a different question every time
        random.shuffle(snippets)

        for snippet in snippets:
            #set phrase equal to the question associated with the answer in the list
            phrase = phrases[snippet]
            #question and answer are returned in convert and assigned here
            question, answer = convert(snippet, phrase)

            #if they want stuff in english then swap the params so that they will read properly
            if phraseFirst:
                question, answer = answer, question

            print(question)

            #get input from the user but it isn't actually used or checked anywhere
            #so we don't need to assign it to a variable
            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye.")
