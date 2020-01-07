import re

#Define the lexicon tuples
big_tuple = (("verb", "go"), ("direction", "north"), ("direction", "west"), ("direction", "east"), ("direction", "south"), ("verb", "kill"), ("verb", "eat"), ("stop", "the"), ("stop", "in"),
("stop", "of"), ("noun", "bear"), ("noun", "princess"))
# first_word = ("verb", "go")
# second_word = ("direction", "north")
# third_word = ("direction", "west")
# fourth_word = ("direction", "east")
# fifth_word = ("direction", "south")
# sixth_word = ("verb", "kill")
# seventh_word = ("verb", "eat")
# eight_word = ("stop", "the")
# ninth_word = ("stop", "in")
# tenth_word = ("stop", "of")
# eleventh_word = ("noun", "bear")
# twelth_word = ("noun", "princess")
# sentence = [first_word, second_word, third_word]

def conver_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(words):
    dic = []
    s = words.split()

    for word in s:
        valid = True
        if conver_number(word) != None:
            numbers = ("number", word)
            dic.append(numbers)
            valid = False
        else:
            tuple_num = 0
            for t in big_tuple:
                if word in big_tuple[tuple_num]:
                    dic.append(big_tuple[tuple_num])
                    valid = False
                tuple_num += 1

        if valid:
            errors = ("error", word)
            dic.append(errors)
    return dic

stuff = input("> ")
print(scan(stuff))
