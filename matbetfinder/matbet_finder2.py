import requests
url = "http://matbettv2{}.com/"

sayi = input("sayi: ")


def bul(url):
    try:
        r = requests.get(url.format(sayi))
        if r.status_code == 200: 
            print("Bağlantı başarılı!")
    except Exception as err:
        print("Bağlantı hatası...")

bul(url)


