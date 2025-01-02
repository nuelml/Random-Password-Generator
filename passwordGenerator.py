import random

letters  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

passw = []

for x in random.choices(letters,k=nr_letters):
    passw.append(x)
    
for y in random.choices(symbols, k=nr_symbols):
    passw.append(y)
   
for z in random.choices(numbers, k=nr_numbers):
    passw.append(z)
    
random.shuffle(passw)

print("Your password is: ", end="")
print("".join(str(x) for x in passw))

