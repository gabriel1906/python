# def zmiana(x, *args, **kwargs ):
#     print("cena", x)
#     print("args", args)
#     print("cena", cena)
#     print("kwargs", kwargs)
#  for text in args:
#      print(text)
#
#     for key in kwargs:
#         print(key, kwargs[key])
#
#
# x = ["tekst 1 $cena", "tekst 2 $cena", "tekst 3 $cena"]
#
# zmiana(10, *x)
#
#
# zmiana(x, "text1", 10, "text2")
#
# text =["koszt $cena PLN", "kwota $cena brutto", "koszt 10 PLN"]

def zmienna_cena(*args, **kwargs):
    out = []
    for text in args:
        for k in kwargs:
            text = text.replace(f'${k}', str(kwargs[k]))
        out.append(text)
    return "\n".join(out)



def test_formatuj():
    assert formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena = 10
    ) == "koszt 10 PLN\nkwota 10 brutto"

    assert formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        'sumarycznie $cena',
        'podatek: $podatek',
        cena = 10
    ) == "koszt 10 PLN\nkwota 10 brutto\nsumarycznie 10"
