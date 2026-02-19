estoque = {}

# ===== Cadastro Produtos =====
def cadastrar_produtos(estoque):
    code = len(estoque) + 1
    
    nome = input("Nome do produto: ")
    
    try:
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))
    except ValueError:
        print("Digite valores numéricos válidos!\n")
        return

    if preco < 0 or quantidade < 0:
        print("Preço e quantidade não podem ser negativos!\n")
        return

    estoque[code] = {
        "Nome": nome,
        "Preço": preco,
        "Quantidade": quantidade,
        "Historico": [f"Cadastro inicial: {quantidade} unidades"]
    }

    print(f"Produto cadastrado com sucesso! Código: {code}\n")


# ===== Entrada de Estoque =====
def entrada_estoque(estoque):
    try:
        code = int(input("Código do produto: "))
    except ValueError:
        print("Código inválido!\n")
        return

    if code in estoque:
        try:
            quantidade = int(input("Quantidade de entrada: "))
        except ValueError:
            print("Digite um número válido!\n")
            return

        if quantidade <= 0:
            print("Quantidade inválida!\n")
            return

        estoque[code]["Quantidade"] += quantidade
        estoque[code]["Historico"].append(f"Entrada: +{quantidade}")

        print("Entrada realizada com sucesso!\n")
    else:
        print("Código não encontrado!\n")


# ===== Saída de Estoque =====
def saida_estoque(estoque):
    try:
        code = int(input("Código do produto: "))
    except ValueError:
        print("Código inválido!\n")
        return

    if code in estoque:
        try:
            quantidade = int(input("Quantidade de saída: "))
        except ValueError:
            print("Digite um número válido!\n")
            return

        if quantidade <= 0:
            print("Quantidade inválida!\n")
            return

        if quantidade > estoque[code]["Quantidade"]:
            print("Estoque insuficiente!\n")
            return

        estoque[code]["Quantidade"] -= quantidade
        estoque[code]["Historico"].append(f"Saída: -{quantidade}")

        print("Saída realizada com sucesso!\n")
    else:
        print("Código não encontrado!\n")


# ===== Listagem de Produtos =====
def lista_produtos(estoque):
    if not estoque:
        print("Estoque vazio!\n")
        return

    print("===== LISTA DE PRODUTOS =====")
    for code, dados in estoque.items():
        print(f"Código: {code}")
        print(f"Nome: {dados['Nome']}")
        print(f"Preço: R$ {dados['Preço']:.2f}")
        print(f"Quantidade: {dados['Quantidade']}")
        print("-" * 30)
    print()


# ===== Relatório Geral =====
def relatorio(estoque):
    if not estoque:
        print("Estoque vazio!\n")
        return

    valor_total = 0

    for dados in estoque.values():
        valor_total += dados["Preço"] * dados["Quantidade"]

    print("===== RELATÓRIO GERAL =====")
    print(f"Valor total em estoque: R$ {valor_total:.2f}\n")


# ===== Menu =====
def menu():
    print("===== CONTROLE DE ESTOQUE =====")
    print("1 - Cadastrar Produto")
    print("2 - Entrada no Estoque")
    print("3 - Saída do Estoque")
    print("4 - Listagem de Produtos")
    print("5 - Relatório Geral")
    print("6 - Sair")


# ===== Loop Principal =====
while True:
    menu()
    
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite um número válido!\n")
        continue

    if opcao == 1:
        cadastrar_produtos(estoque)

    elif opcao == 2:
        entrada_estoque(estoque)

    elif opcao == 3:
        saida_estoque(estoque)

    elif opcao == 4:
        lista_produtos(estoque)

    elif opcao == 5:
        relatorio(estoque)

    elif opcao == 6:
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!\n")
