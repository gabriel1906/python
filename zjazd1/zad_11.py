pozycja_x = int(input("podaj x: "))
pozycja_y = int(input("podaj y: "))


if pozycja_x > 100 or pozycja_y > 100 or pozycja_x < 0 or pozycja_y < 0:
    print("położenie poza planszą")



elif pozycja_x >= 90 and pozycja_y >= 90:
    print("położenie prawy górny róg")

elif pozycja_x >= 90 and pozycja_y <= 10:
    print("położenie prawy dolny róg")

elif pozycja_x <= 10 and pozycja_y <= 10:
    print("położenie lewy dolny róg")

elif pozycja_x <= 10 and pozycja_y >= 90:
    print("położenie lewy dolny róg")



elif pozycja_x > 10 and pozycja_x < 90 and pozycja_y > 10 and pozycja_y < 90:
    print("położenie około centrum")



elif pozycja_x >= 90 and (pozycja_y > 11 and pozycja_y < 90):
    print("położenie prawa krawędź")

elif pozycja_y >= 90 and (pozycja_x > 11 and pozycja_x < 90):
    print("położenie górna krawędź")

elif pozycja_y <= 10 and (pozycja_x > 11 and pozycja_x < 90):
    print("położenie dolna krawędź")

elif pozycja_x <= 10 and (pozycja_y > 11 and pozycja_y < 90):
    print("położenie lewa krawędź")
