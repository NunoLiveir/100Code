import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
random_letter = ""
random_sym = ""
random_num = ""

for letter in range(nr_letters):
  random_letter += random.choice(letters)

for symbol in range(nr_symbols):
  random_sym += random.choice(symbols)

for num in range(nr_numbers):
  random_num += random.choice(numbers)

final_letter = str(random_letter)
final_sym = str(random_sym)
final_num = str(random_num)
  
print(f"Your new password is: {final_letter}{final_sym}{final_num}")  #Order not random
  
new_password = final_letter + final_sym + final_num
final_password = "".join(random.sample(new_password, len(new_password)))
print(f"Your new password, with extra security on top is: {final_password}") #Order random
