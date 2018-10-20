# napis = "To jest napis mama"
# print('mama' in napis)
#
# for litera in napis:
#     print(litera)
#
# print(dir(napis))

#  słownik

my_dict = {
    "pierwsza": "a",
    "druga": "b"
}
my_dict['trzecia'] = "c"

print(my_dict["pierwsza"])
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())


produkt1 = {'nazwa': "Koper", "cena": 3}
produkt2 = {'nazwa': "Kasza", "cena": 1.99}

produkty = [produkt1, produkt2]
print("Produkty w lodówce")
for p in produkty:
    print(p['nazwa'])

for k in produkt1:
    print(k, produkt1[k])

