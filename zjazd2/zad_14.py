zanalezione_max = None
zanalezione_min = None

while True:
    dane = input("Podaj liczbę lub wpisz K by zakończyć: ")
    if dane.lower() == "K":
        break

    liczba = int(dane)
    if zanalezione_max is None or liczba > zanalezione_max:
        zanalezione_max = liczba
    if zanalezione_min is None or liczba < zanalezione_min:
        zanalezione_min = liczba


if not zanalezione_max:
           print("Nie wprowadzono danych")
else:
        print(f" Minimum = {zanalezione_min}, Maximum = {zanalezione_max}")


# if liczba = :
#    print("nie wprowadzono liczby")
