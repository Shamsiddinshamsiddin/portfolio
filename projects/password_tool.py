import random

harflar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sonlar = "1234567890"
belgilar = "!@#$%^&*"

print("1. Generate password")
print("2. Check password")

tanlov = input("Choose: ")

# 🔐 GENERATOR
if tanlov == "1":
    uzunlik = int(input("Length: "))
    barcha = harflar + sonlar + belgilar

    parol = ""
    for i in range(uzunlik):
        parol += random.choice(barcha)

    print("Generated password:", parol)

# 🔍 CHECKER
elif tanlov == "2":
    parol = input("Enter password: ").strip()

    if len(parol) < 8:
        print("Weak password")

    elif parol.isdigit():
        print("Only numbers - weak")

    elif parol.isalpha():
        print("Only letters - weak")

    else:
        print("Strong password")

else:
    print("Wrong choice")
