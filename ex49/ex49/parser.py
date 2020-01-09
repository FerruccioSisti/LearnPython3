class ParserError(Exception):
    pass

class Sentence(object):
    '''
    Takes tuples like ('noun', 'princess') and converts them
    '''
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    '''
    Returns what type of word it's given
    '''
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    '''
    Confirms an expected word is the right type, takes it off the light
    and then returns that word
    '''
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    '''
    Skips words that aren't useful (the ones labelled 'stop') ex. the, is, a
    This can skip multiple words at once
    '''
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    '''
    Skips any stop words, then peeks ahead to make sure the next word is a “verb” type.
    If it’s not, then raise the ParserError to say why. If it is a “verb” then match it,
    which takes it off the list
    '''
    skip(word_list, "stop")

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next")

def parse_object(word_list):
    '''
    Skips any stop words, then peeks ahead to make sure the next word is a 'noun' type.
    If it’s not, then raise the ParserError to say why. If it is a "noun" then match it,
    which takes it off the list
    This also needs to check for directions because that can also be a possible object
    '''
    skip(word_list, 'stop')
    #Call the peek here because we don't want to peek multiple times
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next")

def parse_subject(word_list):
    '''
    Skips any stop words, then peeks ahead to make sure the next word is a 'subject' type.
    If it’s not, then raise the ParserError to say why. If it is a "subject" then match it,
    which takes it off the list
    Checks for nouns and then verbs to indicate the subject of the sentence
    '''
    skip(word_list, 'stop')
    #Checking for multiple things so we don't have to peek twice
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next")

def parse_sentence(word_list):
    '''
    Function calls the other parsers and instantiates a 'Sentence' object
    '''
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
