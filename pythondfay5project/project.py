#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= (input("How many letters would you like in your password?\n")) 
nr_symbols = (input(f"How many symbols would you like?\n"))
nr_numbers = (input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password= ""
# if not nr_letters.isdigit() 
# for char in range (0, nr_letters):
#     password += random.choice(letters)
# for char in range (0,nr_numbers):
#     password += random.choice(numbers)
# for char in range (0,nr_symbols):
#     password += random.choice(symbols)#
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

if not nr_letters.isdigit() or not nr_numbers.isdigit() or not nr_symbols.isdigit():
    print("u did not add a number retry")
else:
    list_password= []
    nr_letters = int(nr_letters)
    nr_symbols = int(nr_symbols)
    nr_numbers = int(nr_numbers)
    for _  in range (nr_letters):
        list_password.append(random.choice(letters))
    for _  in range (nr_numbers):
        list_password.append( random.choice(numbers))
    for _  in range (nr_symbols):
        list_password.append(random.choice(symbols))
    # print(list_password)
    random.shuffle(list_password)
    # print(list_password)
    password ="".join(list_password)
    # for char in list_password:
    #     password += char
    print(f"this is ur password {password}")
    password_length = len(list_password)

    if password_length <= 6:
        print("weak")
    elif password_length == 7 :
        print("not bad")
    else:
        print("good") 