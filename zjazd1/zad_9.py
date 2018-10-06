import datetime
now = datetime.datetime.now()

liczba = int (input("Podaj rok urodzenia: "))
if now.year - liczba >= 18:
    print("Jesteś pełnoletni")
else:
    print("Jesteś niepełnoletni")