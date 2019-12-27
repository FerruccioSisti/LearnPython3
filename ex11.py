#Finally learning input from users

#if you add ", end=' '" to the print statement, it changes the end character from a newline to a space
print ("How old are you (years)?", end = ' ')
age = input()

print ("How tall are you (in cm)?", end = ' ')
height = input()

print ("How much do you weigh (in pounds)?", end = ' ')
weight = input()

print(f"So, you're {age} years old, {height} cm tall, and weigh {weight} pounds.")
