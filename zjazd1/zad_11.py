pozycja_x = int (input("podaj x: "))
pozycja_y = int (input("podaj y: "))

if pozycja_x > 100 or pozycja_y > 100:
    print("położenie poza planszą")

if pozycja_x >= 90 and pozycja_y >= 90:
        print("położenie prawy górny róg")

if pozycja_x >= 90 and pozycja_y <= 10:
        print("położenie prawy dolny róg")

if pozycja_x <= 10 and pozycja_y <= 10:
    print("położenie lewy dolny róg")

if pozycja_x <= 10 and pozycja_y >= 90:
    print("położenie lewy dolny róg")

if pozycja_x >= 11 and pozycja_x <= 89 and pozycja_y >= 11 and pozycja_y <= 89:
    print("położenie około centrum")

if pozycja_x >= 90  and (pozycja_y >= 11 and pozycja_y <= 80):
    print("położenie prawa krawędź")

if pozycja_y >= 90  and (pozycja_x >= 11 and pozycja_x <= 80):
    print("położenie prawa krawędź")