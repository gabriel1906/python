
a = float (input("podaj długość A: "))
b = float (input("podaj szerokość B: "))
c = float (input("podaj głębokość C: "))
d = float (a*b*c)

if d > 1000:
    print("Opakowanie ma objętość większą od 1 litra")
else:
    print("Opakowanie ma objętość miejszą od 1 litra")