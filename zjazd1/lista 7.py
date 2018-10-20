liczby = [5, 2, 1, 4, 3]

min_i = None
max_i = None

print(liczby)
indeksy = list(range(len(liczby)))
for i in indeksy:
    if min_i == None or liczby[i] < liczby[min_i]:
        min_i = i
    if max_i == None or liczby[i] > liczby[max_i]:
        max_i = i
print(i)
print(max_i)


liczby[min_i], liczby[max_i] = liczby[max_i], liczby[min_i]



temp = x[min_i]
x[min_i] = x[max_i]
x[max_i] = temp

print(liczby)


assert liczby == [1, 2, 5, 4, 3]
