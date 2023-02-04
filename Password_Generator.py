# This program will let you choose everything during creating password. From easiest solutions to hardest that I could think of. For now im developing it so its obviously not completed :D
import string
import random
import re
print("Welcome to my password generator ")


def random_password_1(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password


def password_strength(user_password):
    if len(user_password) < 10:
        return "Too Short. Add more characters than 10"
    if not re.search("[a-z]", user_password):
        return "Too Weak. Add small letters"
    if not re.search("[A-Z]", user_password):
        return "Too Weak. Add upper letters"
    if not re.search("[0-9]", user_password):
        return "Too Weak. Add numbers"
    if not re.search("[!@#$%^&*()]", user_password):
        return "Too Weak. Add symbols"
    return "Your password is Strong"


answer = input("""Which option do you want to use?
1. Upgraded password generator \n
2. Check if your password is strong enough""")

if answer == "1":
    number_of_characters = int(input(
        "How many characters do u want to be in your password? \n"))
    print(random_password_1(number_of_characters))

if answer == "2":
    user_password = input(
        "Whats your password? \n")
    print(password_strength(user_password))
