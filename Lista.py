lista = [1,2,3,4,5,6,7,8,9]
pares = []
print(max(lista))
print(min(lista))
print(sum(lista)/len(lista))
for i in lista:
    if i % 2 == 0:
        pares.append(i)
print(pares)