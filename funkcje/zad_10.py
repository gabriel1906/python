def kalkulator(liczba_1, liczba_2, operacja):
    liczba_1 = int(input("podaj pierwszą liczbę: "))
    liczba_2 = int(input("podaj drugą liczbę: "))
    operacja = input("podaj rodzaj operacji: ")

    if operacja == "+":
        wynik = liczba_1 + liczba_2
    elif operacja == "-":
        wynik = liczba_1 - liczba_2
    elif operacja == "*":
        wynik = liczba_1 * liczba_2
    elif (operacja == "/"):
        if liczba_2 == 0:
            raise ValueError("Liczba druga jest )")
            wynik = liczba_1 / liczba_2
        else:
            print("pamiętaj nie dziel przez 0")

    return wynik
    print(wynik)
