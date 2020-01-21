#There isn't an exercise associated with this chapter, its just a review of the different
#Terms we've seen so far in the textbook

#I don't really know what 'yield' means so I am going to do an example for that

#This example shows all the squares that are under 100
def square():
    i = 1

    while True:
        #This will return the square of the current index
        yield i * i
        #function will resume next time it's called at this point
        i += 1

#now to actually use our function we are going to make a for loop
#num is the value returned or yielded in the function
for num in square():
    if num > 100:
         break
    print(num)
