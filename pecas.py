pecas = []
historico_movimentacoes = []


def menu():
    while True:
        print("\n===== SISTEMA DE CADASTRO DE PEÇAS VEICULARES =====")
        print("1 - Cadastrar peça")
        print("2 - Buscar peça")
        print("3 - Alterar peça")
        print("4 - Remover peça")
        print("5 - Entrada de estoque")
        print("6 - Saída de estoque")
        print("7 - Exibir histórico de movimentações")
        print("8 - Desfazer última movimentação")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastro_pecas()
        elif opcao == '2':
            busca_pecas()
        elif opcao == '3':
            alteracao_pecas()
        elif opcao == '4':
            remocao_pecas()
        elif opcao == '5':
            entrada_estoque()
        elif opcao == '6':
            saida_estoque()
        elif opcao == '7':
            exibir_historico()
        elif opcao == '8':
            desfazer_ultima_movimentacao()
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


def cadastro_pecas():
    print('CADASTRO DE PEÇAS')

    peca = input('Peça veicular: ')

    if peca == "":
        print('O CADASTRO É OBRIGATORIO')
        return

    quantidade = int(input('Quantidade de estoque dessa peça: '))
    valor = float(input('Qual valor da peça: R$'))

    peca_new = {
        'Peça: ': peca,
        'Quantidade: ': quantidade,
        'Preço: R$': valor,
    }

    pecas.append(peca_new)
    print('Peça cadastrada!')


def ordenar_pecas():
    n = len(pecas)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if pecas[j]['Peça: '] > pecas[j + 1]['Peça: ']:
                pecas[j], pecas[j + 1] = pecas[j + 1], pecas[j]
    return pecas


def busca_binaria(nome_procurado):
    esquerda = 0
    direita = len(pecas) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        nome_meio = pecas[meio]['Peça: ']

        if nome_meio == nome_procurado:
            return meio
        elif nome_meio < nome_procurado:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


def buscar_peca(nome_procurado):
    if len(pecas) == 0:
        return None
    ordenar_pecas()
    indice = busca_binaria(nome_procurado)
    if indice == -1:
        return None
    return pecas[indice]


def busca_pecas():
    print("BUSCA DE PEÇA")

    if len(pecas) == 0:
        print("Nenhuma peça cadastrada!")
        return

    nome_pecas = input("Qual o nome da peça: ")
    peca_encontrada = buscar_peca(nome_pecas)

    if peca_encontrada is None:
        print("Peça não encontrada!")
        return

    print(f"Peça: {peca_encontrada['Peça: ']}")
    print(f"Quantidade: {peca_encontrada['Quantidade: ']}")
    print(f"Preço: R$ {peca_encontrada['Preço: R$']}")


def alteracao_pecas():
    print('ALTERAÇÃO DE PEÇA')

    nome_procurado = input('Qual peça você quer alterar: ')
    peca_encontrada = buscar_peca(nome_procurado)

    if peca_encontrada is None:
        print('Peça não encontrada!')
    else:
        print(f"Peça atual: {peca_encontrada}")

        nova_quantidade = input('Nova quantidade (deixe em branco para não alterar): ')
        if nova_quantidade != "":
            peca_encontrada['Quantidade: '] = int(nova_quantidade)

        novo_valor = input('Novo valor (deixe em branco para não alterar): ')
        if novo_valor != "":
            peca_encontrada['Preço: R$'] = float(novo_valor)

        print('Peça alterada com sucesso!')


def remocao_pecas():
    print('REMOÇÃO DE PEÇA')

    nome_procurado = input('Qual peça você quer remover: ')
    ordenar_pecas()
    indice_encontrado = busca_binaria(nome_procurado)

    if indice_encontrado == -1:
        print('Peça não encontrada!')
    else:
        confirmacao = input(f"Tem certeza que deseja remover '{nome_procurado}'? (s/n): ")
        if confirmacao.lower() == 's':
            pecas.pop(indice_encontrado)
            print('Peça removida com sucesso!')
        else:
            print('Remoção cancelada.')


def entrada_estoque():
    print('ENTRADA DE PEÇAS NO ESTOQUE')

    nome_procurado = input('Qual peça está entrando: ')
    peca_encontrada = buscar_peca(nome_procurado)

    if peca_encontrada is None:
        print('Peça não encontrada!')
        return

    quantidade_entrada = int(input('Quantidade que está entrando: '))

    if quantidade_entrada <= 0:
        print('A quantidade precisa ser maior que zero!')
        return

    peca_encontrada['Quantidade: '] += quantidade_entrada

    historico_movimentacoes.append({
        'tipo': 'entrada',
        'peca': nome_procurado,
        'quantidade': quantidade_entrada,
    })

    print(f'Entrada registrada! Novo estoque de {nome_procurado}: {peca_encontrada["Quantidade: "]}')


def saida_estoque():
    print('SAÍDA DE PEÇAS DO ESTOQUE')

    nome_procurado = input('Qual peça está saindo: ')
    peca_encontrada = buscar_peca(nome_procurado)

    if peca_encontrada is None:
        print('Peça não encontrada!')
        return

    quantidade_saida = int(input('Quantidade que está saindo: '))

    if quantidade_saida <= 0:
        print('A quantidade precisa ser maior que zero!')
        return

    if quantidade_saida > peca_encontrada['Quantidade: ']:
        print(f'Estoque insuficiente! Só existem {peca_encontrada["Quantidade: "]} unidade(s).')
        return

    peca_encontrada['Quantidade: '] -= quantidade_saida

    historico_movimentacoes.append({
        'tipo': 'saida',
        'peca': nome_procurado,
        'quantidade': quantidade_saida,
    })

    print(f'Saída registrada! Novo estoque de {nome_procurado}: {peca_encontrada["Quantidade: "]}')


def exibir_historico():
    print('HISTÓRICO DE MOVIMENTAÇÕES')

    if len(historico_movimentacoes) == 0:
        print('Nenhuma movimentação registrada ainda.')
        return

    for movimento in reversed(historico_movimentacoes):
        print(f"{movimento['tipo'].upper()} - {movimento['peca']} - {movimento['quantidade']} unidade(s)")


def desfazer_ultima_movimentacao():
    print('DESFAZER ÚLTIMA MOVIMENTAÇÃO')

    if len(historico_movimentacoes) == 0:
        print('Não há movimentações para desfazer.')
        return

    ultimo_movimento = historico_movimentacoes.pop()

    peca_encontrada = buscar_peca(ultimo_movimento['peca'])

    if peca_encontrada is None:
        print('A peça dessa movimentação não existe mais no cadastro.')
        return

    if ultimo_movimento['tipo'] == 'entrada':
        peca_encontrada['Quantidade: '] -= ultimo_movimento['quantidade']
    else:
        peca_encontrada['Quantidade: '] += ultimo_movimento['quantidade']

    print(f"Movimentação desfeita: {ultimo_movimento['tipo'].upper()} de "
          f"{ultimo_movimento['quantidade']} unidade(s) em {ultimo_movimento['peca']}")


if __name__ == "__main__":
    menu()
