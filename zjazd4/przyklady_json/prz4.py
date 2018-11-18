import json
import urllib.request
import sys
from colection import namedtuple



x = input("Podaj nazwę miasta:  ")

with urllib.request.urlopen(f"https://www.metaweather.com/api/location/search/?query={x}) as f:
    print(f)
    pogoda = json.loads(f.read())
print(pogoda)







# rates = kursy[0]['rates']
# for r in rates:
#     print(f" - {r['code']} - {r['mid']}")
#
# waluta = input("Jaka waluta z powyższej list:? ")
# ile = float(input("Ile? "))
#
# for r in rates:
#     if r['code'] == waluta:
#         result = ile * r['mid']
#
# print('Płacisz', result)


if__name__ == "__"