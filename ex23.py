#Example using functions, file IO, encoding/decoding bytes and strings
#Very important that you know DBES (deebees) which stands for
#Decode Bytes Encode Strings
#You have to decode bytes to get a string
#You have to encode strings to get bytes
import sys
script, inputEncoding, error = sys.argv

#Recursive function to read line by line
def main(languageFile, encoding, errors):
    #Read the next line
    line = languageFile.readline()
    #If the line has content (as long as you read a line in the previous readLine())
    if line:
        #print the line with the right encoding and error handling
        printLine(line, encoding, errors)
        #call the function again only this time read the next line
        return main(languageFile, encoding, errors)


def printLine(line, encoding, errors):
    #This strips the string and gets rid of the trailing '\n'
    nextLang = line.strip()
    #Encode the string in order to get raw bytes
    rawBytes = nextLang.encode(encoding, errors = errors)
    #Decode the bytes to get a readable string
    cookedString = rawBytes.decode(encoding, errors = errors)

    print(rawBytes, "<====>", cookedString)

languages = open("languages.txt", encoding = "utf-8")

main(languages, inputEncoding, error)
