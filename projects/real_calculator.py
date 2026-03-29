def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        x = int(input("Number 1: "))
        y = int(input("Number 2: "))
        print("Result:", add(x, y))

    elif choice == "2":
        x = int(input("Number 1: "))
        y = int(input("Number 2: "))
        print("Result:", sub(x, y))

    elif choice == "3":
        x = int(input("Number 1: "))
        y = int(input("Number 2: "))
        print("Result:", mul(x, y))

    elif choice == "4":
        x = int(input("Number 1: "))
        y = int(input("Number 2: "))
        
        if y == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", div(x, y))

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Wrong choice")
