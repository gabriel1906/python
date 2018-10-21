LICZBA_DNI_TYGODNIA = 7
numer_dnia = 1
suma_temperatur = 0

#  pobieranie

def pobieranie_danych(ile_razy=7):
    temperatury = []
    for i in range(ile_razy):
        temp = int(input(f"podaj temperaturę z dnia {i+1}: "))
        temperatury.append(temp)
    return temperatury

#  średnia

def srednia_temp(temperatury):
    srednia_temperatury = sum(temperatury) / len(temperatury)
    return srednia_temperatury

# min max

def znajdz_ekstrema(temperatury):
    min_ = min(temperatury)
    max_ = max(temperatury)
    return min_, max_

# prezentacja

def prezentuj_dane(srednia_temperatura, min_, max_):
    print(f'Średnia temperatura to {srednia_temperatura}')
    print(f'Minimalna temperatura to {min_}')
    print(f'Maksymalna temperatura to {max_}')

dane = pobieranie_danych()
sr_temp = srednia_temp(dane)
min_, max_ = znajdz_ekstrema(dane)
prezentuj_dane(sr_temp, min_, max_)
