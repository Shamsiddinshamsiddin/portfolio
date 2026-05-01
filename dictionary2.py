phone_book = {
    "Ali": "+998909990909",
    "Vali": "+998912223344""
}

name = input("Ism kiriting: ")
if name in phone_book:
    print(phone_book[name])
else:
    print("Bunday ism topilmadi!")
