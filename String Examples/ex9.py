#This example introduces using the newline when printing

days = "Mon Tues Wed Thurs Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print ("Here are the days", days)
print ("Here are the months", months)

#Putting triple quotes around your string allows you to use quotations INSIDE your string without
#Having to use an esacpe sequence (\"). It will keep reading the string until it finds another
#Set of triple quotes
print ("""
There is something happening here
I'm not really sure what the triple quotes do
I think it accomplishes the same thing if we just had
one pair of quotes """)
