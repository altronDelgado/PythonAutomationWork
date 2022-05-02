from itertools import count
from sys import stdout
import requests

url = "http://matbettv2{}.com/"

def changeNumber(url):

    while True:
        try:
            for n in range(8):
                r = requests.get(url.format(n), timeout=10)
                print(url.format(n), "Deneniyor...")
                if r.status_code == 200 : 
                    print("Bulduk bebeğimmm!")
        except Exception as err:
            print("bırak amk")
            break


changeNumber(url)

# import requests
# url = "http://matbettv25.com/"

# r = requests.get(url)
# r.status_code

# if r.status_code == 200: 
#     print("yes")
# else:
#     print("no")