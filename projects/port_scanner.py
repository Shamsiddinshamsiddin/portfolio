import requests

url = "https://google.com"

try:
    response = requests.get(url, timeout=5) # 5 sekund kutadi
    if response.status_code == 200:
        print(f"Muvaffaqiyatli! {url} ishlayapti.")
    else:
        print(f"Sayt javob berdi, lekin status kod: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Xato: Internet aloqasi yo'q yoki sayt mavjud emas!")
except Exception as e:
    print(f"Kutilmagan xato yuz berdi: {e}")
