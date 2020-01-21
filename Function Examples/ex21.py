#Examples where you can have functions return something
def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("Now lets do some math only using functions :)")
age = add(12, 8)
height = subtract(200, 20)
weight = multiply(40, 5)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#Puzzle for extra credit? More like to make myself feel better about learning on my own
print("Here is a puzzle")

#This looks atrocious
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "\nCan you do it by hand?")
