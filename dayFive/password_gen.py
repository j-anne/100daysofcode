#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?: ")) 
nr_symbols = int(input("How many symbols would you like?: "))
nr_numbers = int(input("How many numbers would you like?: "))

letter_list = []
symbol_list = []
number_list = []
for l in range(int(nr_letters)):
  rand_letter = random.choice(letters)
  letter_list.append(rand_letter)

for s in range(int(nr_symbols)):
  rand_symbol = random.choice(symbols)
  symbol_list.append(rand_symbol)
  
for n in range(int(nr_numbers)):
  rand_number = random.choice(numbers)
  symbol_list.append(rand_number)

mix_all = letter_list + symbol_list + number_list

password = ""
random.shuffle(mix_all)

for letter in mix_all:
    password += letter

print(f"Here is your password: {password}")

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P