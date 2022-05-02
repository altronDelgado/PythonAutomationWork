import re
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()


url = "http://matbettv{}.com/"


s = 'Canlı Maçlar'


def bul(url):
    sayi = 2
    while sayi < 100:
        try:
            print(Fore.YELLOW + "===============================")
            r = requests.get(url.format(sayi), timeout=3)
            print(url.format(sayi), Fore.GREEN + "\nAranıyor...")
            result = re.search(s, r.text)
            try:
                if result.group(0) == s:
                    print(Fore.CYAN + Back.BLACK + "Bağlantı sağlandı ve site bulundu!")
                    break
            except:
                print(Fore.MAGENTA + "Bu siteye ulaşılamıyor.")
                sayi+=1
                continue
        except Exception as err:
            print(Fore.RED + "Bağlantı hatası...")
            sayi +=1
            continue

bul(url)
