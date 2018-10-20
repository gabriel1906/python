# a = {1, 2, 3}
# b = {4, 5, 3}
# print(a | b)
# print(a - b)
# print(a & b)
# print(a ^ b)


liczby = set()

while True:
    komenda = input("wprowadź liczbę lub k by zakończyć")
    if komenda == 'k':
        break
    liczba = int(komenda)
    liczby.add(liczba)
print(len(liczby & set(range(2, 100, 2))))
