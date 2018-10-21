def przywitaj_sie(imie):
    print("Witaj ", imie)
    if wzrost > 178:
        print("Ale z ciebie drągal")
    if wiek > 39:
        print("Jeszcze żyjesz?")
    if waga > 100:
        print("Boczek")

lista_osób = [
    {
    'imie': "Rafał",
     'wiek:' 38,
     'wzrost': 178,
     'waga': 80,
}
{
    'imie': "Adam",
     'wiek:' 40,
     'wzrost': 181,
     'waga': 109,

]
lista_imion = ["Rafał", "Adam"]

for imie in lista_imion:
    przywitaj_sie(imie)






# print(type(przywitaj_sie))
# print(x)