def podzielna_przez_2(x):
    return x%2 == 0

print(podzielna_przez_2(12))
print(podzielna_przez_2(11))

# y = lambda x: x%2 == 0
# print(y(4))
# print(y(5))

def wybierz(dane, warunek):
    out = []
    for element in dane:
        if warunek(element):
            out.append(element)
    return(out)

lista = [1, 2, 3, 4, 5, 123, 234,]
print(wybierz(lista, podzielna_przez_2))

def podzielna_przez_3(x):
    return x%3 == 0