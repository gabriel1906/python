import sys

input("Podaj nazwę pliku: ")

if len(sys.argv) > 1:
    nazwa_pliku = sys.argv[1]

    with open(nazwa_pliku) as f:

        for i, line in enumerate(f, start=1):
            print(i, line, end="")

else:
    input("P: ")








# with open("ścieżka", w, encoding='utf-8') as f:
#     f.write("text")


# if nazwa_pliku = sys.argv():
#     with open("nazwa_pliku") as f:
#     print(f.read())