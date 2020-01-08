#This exercise is outputting a given sentence but adding the types of words used

#Define the (TYPE, PAIR)'s
big_tuple = (('direction', 'north'), ('direction', 'south'), ('direction', 'east'),
            ('direction', 'west'), ('verb', 'go'), ('verb', 'kill'), ('verb', 'eat'),
            ('stop', 'the'), ('stop', 'in'), ('stop', 'of'), ('noun', 'bear'),
            ('noun', 'princess'))

def scan(sentence):
    '''
    Function parses a sentence and then creates a dictionary to display the given
    sentence as well as adding the type for each word
    '''
    words = sentence.split()
    output = []

    #Loop through each word in the sentence
    for w in words:
        i = 0
        #Need this flag to check if word was not appended (if it needs 'error' type)
        flg = True

        #First check if its a number to avoid a needless loop
        if convert_number(w) != None:
            num = ("number", convert_number(w))
            output.append(num)
            flg = False
            continue

        #Iterate through the tuple list checking for a matching type
        for t in big_tuple:
            if w in big_tuple[i]:
                output.append(big_tuple[i])
                flg = False
                break
            i += 1

        #If we don't have a definition or its not a number, its type is 'error'
        if flg is True:
            err = ("error", w)
            output.append(err)
    return output

def convert_number(s):
    '''
    This method converts a string into an int (ONLY IF IT IS AN ACTUAL INT)
    '''
    try:
        return int(s)
    except ValueError: #Return None if there are characters ^(0-9)
        return None
