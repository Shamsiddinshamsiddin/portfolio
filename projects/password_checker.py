password = input("Enter password: ")

if len(password) < 8:
    print("Weak password")

elif password.isdigit():
    print("Only numbers - weak")

elif password.isalpha():
    print("Only letters - weak")

else:
    print("Strong password")
