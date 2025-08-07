def objeto(n,q,p,c):
    item = {
        "nome": n,
        "quantidade": int(q),
        "preco": float(p),
        "categoria": c}
    return item

estoque = []

while True:
    x = int(input("1 - Cadastrar Produto\n2 - Ver Produtos\n3 - Quantidade de Produtos\n4 - Valor total do Produto\n0 - Sair\n"))
    if x == 1:
        Nome = input('Digite o nome do produto: ')
        Quantidade = input('Digite a quantidade de produtos: ')
        Preco = input('Digite o preço do produto: ')
        Categoria = input('Digite o categoria do produto: ')

        produto = objeto(Nome,Quantidade,Preco,Categoria)
        estoque.append(produto)

    elif x == 2:
        for j in range(len(estoque)):
            print(estoque[j])

    elif x == 3:
        for p in range(len(estoque)):
            if estoque[p]['quantidade'] < 10:
                print(estoque[p])
    elif x == 4:
        for i in range(len(estoque)):
            soma = estoque[i]['quantidade'] * estoque[i]['preco']
            print("O estoque de",estoque[i]['nome'],"vale um total de:",soma,"Reais")
    elif x == 0:
        break
    else:
        print("Opção Invalida")