produkty = {"ziemniaki": 2, "bataty": 4, "pomidory": 6}
magazyn = {"ziemniaki": 10, "bataty": 10, "pomidory": 10}
koszyk
do_zaplaty = 0

while True:
    print("-" * 40)
    print("nasz zielnik oferuje: ")

    for produkt in produkty:
        print(f' - {produkt} - {produkty[produkt]} PLN')

    komenda = input("Co chcesz zrobić?: [k]upić, [koniec] by przerwać")
    if komenda == 'koniec':
        break
    elif
    produkt_wybrany = input("Co chcesz kupić?: ")
    # continue

    # if produkt_wybrany not in produkty:
    #     print("Nie mamy takiego produktu")

    waga = float(input("Ile kilogramów? {produkt_wybrany}: "))

    if magazyn[produkt_wybrany] < waga:
        print("Mamy za mało {produkt_wybrany}")
        continue
    magazyn[produkt_wybrany] = magazyn[produkt_wybrany] - waga
    cena = produkty[produkt_wybrany]
    koszt = waga * cena
    do_zaplaty += koszt
elif komenda == 'd':
produkt_do_dodania = input("Jaki produkt chcesz dodać? ")
if produkt_do_dodania not in magazyn:
    magazyn[produkt_do_dodania] = 0
    cena_nowego_produktu = float(input("ZPo ile to sprzedajemy? ")
    produkty[produkt_do_dodania] = cena_nowego_produktu

    ile_produktu_dodajemy = float(input("Ile tego dodać? "))

    print("-" * 40)
    print(f"wyliczony koszt to {do_zaplaty}")
