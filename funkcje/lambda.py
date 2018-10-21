

data = [1, 2, 3, 4, 5, 6, 7]

def przytnij(data, start, stop):
    resylt = []

    for element in data:
        if start(element):
            if stop(element):
                break
            result.append(element)
    return result






# print(lista, lambda x: x > 3)
# print(lista, lambda x: x == 6)
