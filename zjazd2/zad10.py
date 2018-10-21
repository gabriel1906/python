napis = input("Podaj napis: ")
licznik_liter = {}

for litera in napis:
    if litera in licznik_liter:
        licznik_liter[litera] = licznik_liter[litera] + 1
    else:
        licznik_liter[litera] = 1

print(f"litera: {litera} wystąpiła {licznik_liter[litera]} razy")

for litera in licznik_liter:
    licznik_liter[litera] = licznik_liter.get(litera, 0) +1

print(f"litera: {litera} wystąpiła {licznik_liter[litera]} razy")

































