import csv

with open("dane/titanic_train.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    dlugosci = {}
    for row in data:
        dlugosci[row['Survived']] = dlugosci.get(row['Survived'], 0) + 1
    print(dlugosci)

    przezylo = dlugosci['1']
    zginelo = dlugosci['0']

    print(f"Przeżyło ogółem {round(100*przezylo/(przezylo+zginelo), 2)}")
    print(f"Zginęło ogółem {round(100*przezylo/(przezylo+zginelo), 2)}")


    kobiet = {}
    for row in data:
        if row['Sex'] == female:
        kobiety[row['Survived']] = kobiety.get(row['Survived'], 0) + 1
    print(kobiety)
