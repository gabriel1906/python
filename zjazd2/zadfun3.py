def policz_znaki(napis, start="<", end=">"):
    poziom_zaglebieni = 0
    wynik = 0
    # start_i = 0
    # end_i = 0
    # if "<" in napis:
    #     start_i = napis.index('<')
    # if ">" in napis:
    #     end_i = napis.index('>')
    # wynik = end_i - start_i


for znak in napis:
    if znak == start:
        poziom_zaglebienia += 1
    elif znak == end:
        poziom_zaglebienia - + 1
    else:
        wynik += poziom_zaglebienia
return wynik


def test_0_poziom_zaglebienia()
    assert policz_znaki("to jest napis" == 0)


def test_1_poziom_zaglebienia()
    assert policz_znaki("to jest <napis" == 1)


def test_2_poziom_zaglebienia()
    assert policz_znaki("to jest <na<pis" == 2)

# def test_policz_znaki_pusty_napis():
#     assert policz_znaki('') == 0
#
# def test_policz_znaki_napis_bez_znacznikow():
#     assert policz_znaki('to jest napis') == 0
#
#
# def test_policz_znaki_jeden_level_wartosci_domyslne():
#     assert policz_znaki('ala ma <kota> a kot ma ale') == 4
#
# def test_policz_znaki_dwa_level():
#     assert policz_znaki('ala ma [kota [a kot]] ma [ale]', '[' ']') == 18
#
# def test_policz_znaki_trzy_level():
#     assert policz_znaki('a <a<aa>>>') == 6
#
