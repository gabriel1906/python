lista = [-1, 100, 20, 30 -15, 0, 200, -1000]

licz_uj = 0
licz_dod = 0

for el in lista:
    if el< 0:
        licz_uj += 1
    elif el > 0:
        licz_dod += 1

print("dodatnich:", licz_dod)
print("ujemnych:", licz_uj)
