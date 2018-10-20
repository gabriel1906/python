
liczby = []

while len(liczby) < 10:
    dane = int(input("Podaj liczbę lub wpisz K by zakończyć: "))
    liczby.append(dane)
    if dane == 'K':
        break

srednia = sum(liczby)/len(liczby)

print(srednia)