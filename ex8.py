#Showing off printing with formats

#Every print statement that uses 'formatter' will display its parameters one after the other
#Seperated by a space
formatter = "{} {} {} {}"

print (formatter.format(1, 2, 3, 4))
print (formatter.format("one", "two", "three", "four"))
print (formatter.format(True, False, True, True))

#This one does each string of 4 {} for each time it is in the original string (16 {})
print (formatter.format(formatter, formatter, formatter, formatter))
