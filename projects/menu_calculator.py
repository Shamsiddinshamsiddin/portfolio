def add(a, b):
    return a + b
while True:
    print("1. Add")
    print("2. Exit")
    choice = input("Choose: ")
if choice == "1":
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
    print("Result:"), add(x, y))
elif choice == "2":
    break
else:
    print("Wrong choise")
