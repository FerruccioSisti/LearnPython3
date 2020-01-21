#This is a longer exercise where we practice everything from the previous 23 examples

print("Lets practice everything.")
print('You\'d need to know \'bout escapes with \\ that do: ')
print('\n newlines and \t tabs')

poem = """\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none."""

print(f"---------------\n{poem}\n---------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

#Functions can return multiple variables in python
def secretFormula(started):
    jellyBeans = started * 500
    jars = jellyBeans / 1000
    crates = jars / 100
    return jellyBeans, jars, crates

startPoint = 10000
#You can assign multiple variables if your function returns multiple variables
beans, jars, crates = secretFormula(startPoint)

print("With a starting point of: {}".format(startPoint))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

startPoint = startPoint / 10

print("We can also do it this way: ")
#This makes a list of strings
formula = secretFormula(startPoint)
#This iterates through the list and assigns each {} to an index of the list, with the first {} being index 0
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
