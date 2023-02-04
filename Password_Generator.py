# This program will let you choose everything during creating password. From easiest solutions to hardest that I could think of. For now im developing it so its obviously not completed :D

import random

print("Welcome to my password generator ")

symbols = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"


def random_password_1(number):
    password = "".join(random.sample(symbols, number))
    return password


answer = input("""Which option do you want to use?
1. Fast Password generator \n""")

if answer == "1":
    number_of_characters = int(input(
        "How many characters do u want to be in your password? \n"))
    print(random_password_1(number_of_characters))
