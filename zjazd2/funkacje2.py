
def wiecej_niz(napis, prog):
    licznik_liter = {}
    wynik = set()

    for litera in napis.lower():
               # licznik_liter[litera] = licznik_liter.get (litera, 0)
        if napis.count(litera) > prog:
    # for key, value in licznik_liter.items():
    #     if value > prog:
            wynik.add(litera)

    return {znak for znak in napis if napis.lower().count(znak) > prog}



def test_wiecej_niz_dla_pustego_napisu():

    assert wiecej_niz("", 0) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaaAbbbccd", 2) == {'a', 'b'}