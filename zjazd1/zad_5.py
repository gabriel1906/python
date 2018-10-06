
miasto_A = input("podaj nazwę miasta wyjazdu: ")
miasto_B = input("podaj nazwę miasta docelowego: ")
dystans =  int (input("podaj odległość:" ))
spalanie = float (input("podaj spalanie:" ))
cena_paliwa = float (input("podaj cenę paliwa: "))

a = float (dystans)
b = float (spalanie)
c = float (cena_paliwa)
d = ((b*c)*(a/100))

print("koszt:", d)













