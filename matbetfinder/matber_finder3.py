# # import requests
# # url = "http://matbettv2{}.com/"

# # sayi = input("sayi: ")


# # def bul(url):
# #     try:
# #         r = requests.get(url.format(sayi))
# #         r.text
# #         print(r.text)
# #         if r.status_code == 200: 
# #             print("Bağlantı başarılı!")
# #     except Exception as err:
# #         print("Bağlantı hatası...")

# # bul(url)

# import re
# import requests
# url = "http://matbettv2{}.com/"

# sayi = input("sayi: ")
# s = 'Canlı Maçlar'

# def bul(url):
#     try:
#         r = requests.get(url.format(sayi))
#         result = re.search(s, r.text)
#         try:
#             if result.group(0) == s:
#                 print("Bağlantı sağlandı ve site bulundu!")
#         except:
#             print("Bağlatnı sağlandı fakat bu site değil.")
#     except Exception as err:
#         print("Bağlantı hatası...")

# bul(url)


import re
import requests

url = "http://matbettv2{}.com/"


s = 'Canlı Maçlar'


def bul(url):
    sayi = 0
    while sayi < 10:
        try:
            print("===============================")
            r = requests.get(url.format(sayi))
            print(url.format(sayi), "\nDeneniyor...")
            result = re.search(s, r.text)
            try:
                if result.group(0) == s:
                    print("Bağlantı sağlandı ve site bulundu!")
                    break
            except:
                print("Bağlatnı sağlandı fakat bu site değil.")
                number+=1
                continue
        except Exception as err:
            print("Bağlantı hatası...")
            sayi +=1
            continue

bul(url)
