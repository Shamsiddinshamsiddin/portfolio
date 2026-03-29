import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Password length: "))

password = ""

for i in range(length):
    password += random.choice(chars)

print("Your password:", password)
