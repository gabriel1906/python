import json

try:
    with open("pracownicy.json") as f:
        pracownicy = json.load(f)
except FileNotFoundError:
    pracownicy = []

komenda = input("Co chcesz zrobić?: - [d]odaj pracownika, [w]ypisz pracownika:  ")
if komenda == 'd':
    pracownik = {}
    imie = input("Podaj imię:  ")
    nazwisko = input("Podaj nazwisko:  ")
    rok_urodzenia = int(input("Podaj rok urodzenia:  "))
    pensja = float(input("Wysokość wynagrodzenia:  "))

    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "urodzony": rok_urodzenia,
        "pensja": pensja}

    pracownicy.append(pracownik)
    with open("pracownicy.json", 'w') as f:
        json.dump(pracownicy. f)

print(pracownicy)

# if komenda  == 'w':
#     print("Pracownicy:")
#     for i, pracownik in enumerate(pracownicy, start=1):
#         print(f" - [{i"}] {pracownik['imie']} {pracownik['nazwisko']} - {
# else:
#     break




# pracownicy = json.dumps(pracownicy)








# print(type(meble_as_json))
#
#
# odczytanie_z_jsona_meble = json.loads(meble_as_json)
# print(type(odczytanie_z_jsona_meble))
# print(odczytanie_z_jsona_meble)
#
# with open("meble.json", 'w')  as f:
#     json.dump(meble, f)
#
# with open("meble.json")  as f:
#     meble = json.load(f)
#     meble.append("taboret")
#     print(meble)
#
# with open("meble.json", 'w')  as f:
#     json.dump(meble, f)