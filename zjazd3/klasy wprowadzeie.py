x = 1
napis = "to jest napis"
y = 4.3
slownik = {}

def foo():
    pass
print(type(x), type(napis), type(y), type(slownik), type(foo))

# definicja klasy

class Animal:
    nazwa = "Fauna"
    licznik = 0

    def _init_(self, gatunek):
        self.gatunek = gatunek

    def _str_(self):
        return "Animal"




# tworzenie instancji danej klasy


azor = Animal("Camis Familiaris")
rudolf = Animal("Rangifer tarandus")


# print(type(azor))
# print(dir(azor))
print(azor.nazwa)