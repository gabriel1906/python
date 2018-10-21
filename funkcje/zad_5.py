#  pobieranie danych

def pobieranie_danych():
    miasto_A = input("podaj nazwę miasta wyjazdu: ")
    miasto_B = input("podaj nazwę miasta docelowego: ")
    dystans = int(input("podaj odległość:"))
    spalanie = float(input("podaj spalanie:"))
    cena_paliwa = float(input("podaj cenę paliwa: "))
    return miasto_A, miasto_B, dystans, spalanie, cena_paliwa

def obliczenie_kosztu(miasto_A, miasto_B, dystans, spalanie, cena_paliwa):
    koszt = int(dystans / 100 * spalanie * cena_paliwa)
    return koszt


dane = pobieranie_danych()
# print(dane)
# print(type(dane))
koszt = obliczenie_kosztu(*dane)

print(koszt)

def drukuj_wynik(miasto_A, miasto_B, dystans, spalanie, cena_paliwa):
    koszt = obliczenie_kosztu(dystans, spalanie, cena_paliwa)
    output = f'''
    miasto A: {miasto_A}
    miasto B: {miasto_B
    Dystans 
    '''

#  prezentacja danych






#  obliczenie kosztów




#  prezentacja danych





# a = float(dystans)
# b = float(spalanie)
# c = float(cena_paliwa)
# d = ((b * c) * (a / 100))
#
# print("koszt:", d)
