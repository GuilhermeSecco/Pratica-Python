palavra = input('Digite uma palavra: ')
lista = []
p = 0
for letra in palavra:
    lista.append(letra.lower())

for letra in range(len(lista)):
    if lista[letra] != lista[-1-letra]:
        p += 1

if p != 0:
    print('Não é Palindromo')
else:
    print('Palindromo')
