import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator")

number_of_letter = int(input("Enter the number of letters you want: "))
number_of_number = int(input("Enter the number of numbers you want: "))
number_of_symbol = int(input("Enter the number of symbols you want: "))

l = []

for i in range(1, number_of_letter+1):
    l.append(random.choice(letters))

for i in range(1, number_of_number+1):
    l.append(random.choice(numbers))

for i in range(1, number_of_symbol+1):
    l.append(random.choice(symbols))


random.shuffle(l)
print(*l, sep="")
