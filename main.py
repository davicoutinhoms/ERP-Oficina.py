from services.ordem_service import (
    cadastrar_ordem,
    listar_ordens,
    consultar_ordem,
    alterar_status,
    alterar_prioridade,
    registrar_servico,
    remover_ordem,
    processar_proxima_ordem,
    relatorio_por_prioridade,
    relatorio_por_valor
)


while True:
    print("\n==============================")
    print("        ERP OFICINA")
    print("==============================")

    print("1 - Cadastrar ordem de serviço")
    print("2 - Consultar ordem de serviço")
    print("3 - Listar ordens")
    print("4 - Alterar status")
    print("5 - Alterar prioridade")
    print("6 - Registrar serviço")
    print("7 - Remover ordem")
    print("8 - Processar próxima ordem")
    print("9 - Relatório por prioridade")
    print("10 - Relatório por valor")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_ordem()

    elif opcao == "2":
        consultar_ordem()

    elif opcao == "3":
        listar_ordens()

    elif opcao == "4":
        alterar_status()

    elif opcao == "5":
        alterar_prioridade()

    elif opcao == "6":
        registrar_servico()

    elif opcao == "7":
        remover_ordem()

    elif opcao == "8":
        processar_proxima_ordem()

    elif opcao == "9":
        relatorio_por_prioridade()

    elif opcao == "10":
        relatorio_por_valor()

    elif opcao == "0":
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida.")