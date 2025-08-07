dados = {
    "cliente": "Maria",
    "pedidos": [
        {"id": 1, "valor": 42.50},
        {"id": 2, "valor": 28.75},
        {"id": 3, "valor": 34.90}
    ]
}
soma = 0
print(dados.get('cliente'))
print(dados['pedidos'][1]['valor'])
for i in range(len(dados['pedidos'])):
    soma += dados['pedidos'][i]['valor']

print(soma)