import random

alphabet_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol_chars = ["@", "$", "#", "!"]
current = []

yes_list = ["YES", "Yes", "yes", "Y", "y"]

password = ""

print("Include letters?")  # ask for a password
letters_inc = input()

print("Include numbers?")
numbers_inc = input()

print("Include symbols?")
symbols_inc = input()

print("How long?")
length = int(input())

if letters_inc not in yes_list and numbers_inc not in yes_list and symbols_inc not in yes_list:
    print("Error: no characters chosen for the password")
else:
    if letters_inc in yes_list:
        current.extend(alphabet_chars)
    if numbers_inc in yes_list:
        current.extend(number_chars)
    if symbols_inc in yes_list:
        current.extend(symbol_chars)

    for i in range(length):
        password += random.choice(current)
    print(f"Password: {password}")
