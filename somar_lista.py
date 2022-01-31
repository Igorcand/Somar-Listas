lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [3, 1, 7, 2]
listaSoma = []

for i in range(len(lista2)):
    listaSoma.append(lista1[i] + lista2[i])

print(listaSoma)

listaSomando = [x + y for x, y in zip(lista1, lista2)]
print(listaSomando)