class Product:
    def _init_(self, id, nazwa, cena):
        self.ID = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        return f'Product: {self.nazwa}, ID: {self.ID}, cena: {self.cena} PLN'






def test_product():
product = Product(1, 'Woda', 10.99)
    assert product.ID == 1
    assert product.nazwa == "Woda"
    assert product.cena == 10.99

def test_product.print_info():
    product = Product(1, 'Woda', 10.99)
    assert product_print_info() == 'Product "Woda", ID: 1, cena: 10.99 PLN'