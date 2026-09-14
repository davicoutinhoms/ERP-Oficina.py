from models.ordem_servico import OrdemServico
from dados.ordens import ordens
from algoritmos.busca import buscar_ordem_por_codigo
from algoritmos.ordenacao import ordenar_por_prioridade, ordenar_por_valor
from estruturas.fila_prioridade import FilaPrioridade
fila_ordens = FilaPrioridade()

#cadastro e ordem de serviço
def cadastrar_ordem():
    print("\n--- CADASTRO DE ORDEM DE SERVIÇO ---")

    codigo = int(input("Código da OS: "))

    indice = buscar_ordem_por_codigo(ordens, codigo)

    if indice != -1:
        print("Já existe uma ordem com esse código.")
        return

    cliente = input("Nome do cliente: ")
    veiculo = input("Veículo: ")
    problema = input("Problema apresentado: ")

    prioridade = int(input("Prioridade (1 a 5): "))

    if prioridade < 1 or prioridade > 5:
        print("Prioridade inválida.")
        return

    nova_ordem = OrdemServico(
        codigo,
        cliente,
        veiculo,
        problema,
        prioridade
    )

    ordens.append(nova_ordem)
    fila_ordens.inserir(nova_ordem)

    print("Ordem de serviço cadastrada com sucesso!")

#listamento de todas as ordens
def listar_ordens():
    if len(ordens) == 0:
        print("Nenhuma ordem cadastrada.")
        return

    print("\n--- ORDENS DE SERVIÇO ---")

    for ordem in ordens:
        print("\n-------------------------")
        print("Código:", ordem.codigo)
        print("Cliente:", ordem.cliente)
        print("Veículo:", ordem.veiculo)
        print("Problema:", ordem.problema)
        print("Prioridade:", ordem.prioridade)
        print("Status:", ordem.status)
        print(f"Valor: R$ {ordem.valor_total:.2f}")

#consultar uma OS (ordem de serviço)
def consultar_ordem():
    codigo = int(input("Código da OS: "))

    indice = buscar_ordem_por_codigo(ordens, codigo)

    if indice == -1:
        print("Ordem de serviço não encontrada.")
        return

    ordem = ordens[indice]

    print("\n--- ORDEM ENCONTRADA ---")
    print("Código:", ordem.codigo)
    print("Cliente:", ordem.cliente)
    print("Veículo:", ordem.veiculo)
    print("Problema:", ordem.problema)
    print("Prioridade:", ordem.prioridade)
    print("Status:", ordem.status)
    print(f"Valor: R$ {ordem.valor_total:.2f}")

#alterar status
def alterar_status():
    codigo = int(input("Código da OS: "))

    indice = buscar_ordem_por_codigo(ordens, codigo)

    if indice == -1:
        print("Ordem de serviço não encontrada.")
        return

    print("\nStatus atual:", ordens[indice].status)

    print("1 - Aguardando")
    print("2 - Em manutenção")
    print("3 - Concluída")

    opcao = input("Novo status: ")

    if opcao == "1":
        novo_status = "Aguardando"

    elif opcao == "2":
        novo_status = "Em manutenção"

    elif opcao == "3":
        novo_status = "Concluída"

    else:
        print("Opção inválida.")
        return

    ordens[indice].alterar_status(novo_status)

    print("Status alterado com sucesso!")

#alterar prioridade
def alterar_prioridade():
    codigo = int(input("Código da OS: "))

    indice = buscar_ordem_por_codigo(ordens, codigo)

    if indice == -1:
        print("Ordem de serviço não encontrada.")
        return

    print("Prioridade atual:", ordens[indice].prioridade)

    nova_prioridade = int(input("Nova prioridade (1 a 5): "))

    if nova_prioridade < 1 or nova_prioridade > 5:
        print("Prioridade inválida.")
        return

    ordens[indice].alterar_prioridade(nova_prioridade)

    print("Prioridade alterada com sucesso!")

#registrar serviço
def registrar_servico():
    codigo = int(input("Código da OS: "))

    indice = buscar_ordem_por_codigo(ordens, codigo)

    if indice == -1:
        print("Ordem de serviço não encontrada.")
        return

    descricao = input("Descrição do serviço: ")
    valor = float(input("Valor do serviço: R$ "))

    ordens[indice].adicionar_servico(
        descricao,
        valor
    )

    print("Serviço registrado com sucesso!")
    print(
        f"Valor atual da OS: R$ {ordens[indice].valor_total:.2f}"
    )

#remover ordem
def remover_ordem():
    codigo = int(input("Código da OS que deseja remover: "))

    indice = buscar_ordem_por_codigo(ordens, codigo)

    if indice == -1:
        print("Ordem de serviço não encontrada.")
        return

    ordens.pop(indice)

    fila_ordens.remover_por_codigo(codigo)

    print("Ordem removida com sucesso!")

#processamento da próxima ordem
def processar_proxima_ordem():
    ordem = fila_ordens.remover_maior_prioridade()

    if ordem is None:
        print("Não existem ordens aguardando atendimento.")
        return

    ordem.alterar_status("Em manutenção")

    print("\n--- PRÓXIMA ORDEM ---")
    print("Código:", ordem.codigo)
    print("Cliente:", ordem.cliente)
    print("Veículo:", ordem.veiculo)
    print("Problema:", ordem.problema)
    print("Prioridade:", ordem.prioridade)
    print("Status:", ordem.status)

#relatório por prioridade
def relatorio_por_prioridade():
    if len(ordens) == 0:
        print("Nenhuma ordem cadastrada.")
        return

    ordenadas = ordenar_por_prioridade(ordens)

    print("\n--- RELATÓRIO POR PRIORIDADE ---")

    for ordem in ordenadas:
        print(
            "OS",
            ordem.codigo,
            "| Prioridade:",
            ordem.prioridade,
            "| Cliente:",
            ordem.cliente
        )

#relatório por valor
def relatorio_por_valor():
    if len(ordens) == 0:
        print("Nenhuma ordem cadastrada.")
        return

    ordenadas = ordenar_por_valor(ordens)

    print("\n--- RELATÓRIO POR VALOR ---")

    for ordem in ordenadas:
        print(
            "OS",
            ordem.codigo,
            "| Cliente:",
            ordem.cliente,
            f"| Valor: R$ {ordem.valor_total:.2f}"
        )