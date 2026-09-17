#Lista principal: cadastro=[nome_cliente,[["Placa","Marca"]]]
cadastro=[]

#odenar listas por Bubble sort
def ordenar_clientes():
  n = len(cadastro)
  for i in range(n):
    for j in range(0,n-i-1):
      if cadastro[j][0].lower()> cadastro[j+1][0].lower():
        posicao_nova = cadastro[j]
        cadastro[j]=cadastro[j+1]
        cadastro[j+1]=posicao_nova

def ordenar_veiculos(lista_veiculos):
  n=len(lista_veiculos)
  for i in range(n):
    for j in range(0,n-i-1):
      if lista_veiculos[j][0].lower()> lista_veiculos[j+1][0].lower():
        posicao_nova= lista_veiculos[j]
        lista_veiculos[j]=lista_veiculos[j+1]
        lista_veiculos[j+1]=posicao_nova

#busca binária
def buscar_cliente(nome):
  inicio = 0
  fim = len(cadastro)-1
  nome_alvo = nome.lower()
  while inicio <= fim:
    meio= (inicio+fim)//2
    nome_atual= cadastro[meio][0].lower()
    if nome_atual == nome_alvo:
      return meio
    elif nome_atual < nome_alvo:
      inicio = meio+1
    else:
      fim= meio-1
  return None

def buscar_veiculo(placa):
  placa_alvo = placa.lower()

  for id_cliente in range(len(cadastro)):
    veiculos=cadastro[id_cliente][1]
    inicio = 0
    fim= len(veiculos)-1
    while inicio <= fim:
      meio=(inicio+fim)//2
      placa_atual = veiculos[meio][0].lower()
      if placa_atual == placa_alvo:
        return id_cliente,meio
      elif placa_atual< placa_alvo:
        inicio= meio+1
      else:
        fim= meio-1
  return None, None

#evitar entrada vazia
def validacao (mensagem):
  while True:
    valor=input(mensagem).strip()
    if valor:
      return valor
    print("Erro... Campo em branco")

#menu clientes
def menu_clientes():
  while True:
    print(">>> Gerenciamento de Clientes <<<")
    print("1. Cadastro de Cliente")
    print("2. Lista de Clientes cadastrados")
    print("3. Consultar Cliente")
    print("4. Alteração de Cliente")
    print("5. Remoção de cliente")
    print("6. Voltar ao menu principal")
    numero=input("Escolha uma das opções: \n").strip()
    if numero=="1": #CADASTRO DE CLIENTE
      nome = validacao("Nome do cliente: ").strip()
      if buscar_cliente(nome) is not None:
        print("Cliente já cadastrado no sistema!")
      else:
        cadastro.append([nome,[]])
        ordenar_clientes()
        print(f"Cliente '{nome}' cadastrado com sucesso!")
    elif numero == "2": #LISTA TOTAL DE CLIENTES
      if not cadastro:
        print("Nenhum cliente cadastrado no sistema")
      else:
        print("\n ****** LISTA DE CLIENTES CADASTRADOS ******")
        for i in range(len(cadastro)):
          cliente=cadastro[i]
          quantidade_veiculo=len(cliente[1])
          print(f"> cliente:{cliente[0]} | Veículos: {quantidade_veiculo}")
    elif numero== "3": #CONSULTAR CLIENTE
      nome = validacao("Nome do cliente: ").strip()
      id_cliente = buscar_cliente(nome)
      if id_cliente is not None:
        cliente = cadastro[id_cliente]
        nome_cliente = cliente[0]
        lista_veiculos = cliente[1]
        print("\n ****** CLIENTE ENCONTRADO ******")
        print(f"Nome: {nome_cliente}")
        if lista_veiculos:
          print("Veículos cadastrados:")
          for i in lista_veiculos:
            print(f"-> Placa: {i[0]}| Marca: {i[1]}")
        else:
          print("-> Nenhum veículo cadastrado")
      else:
        print("Cliente não encontrado")
    elif numero == "4": #ALTERAR CLIENTE
      nome = validacao("Nome do cliente a ser alterado:")
      id_cliente= buscar_cliente(nome)
      if id_cliente is not None:
        novo_nome = validacao("Digite o novo nome:")
        cadastro[id_cliente][0] = novo_nome
        ordenar_clientes()
        print("Nome do cliente atualizado!")
      else:
        print("Cliente não encontrado")
    elif numero == "5": #REMOÇÃO DE CLIENTE
      nome = validacao ("Nome do cliente a remover:")
      id_cliente = buscar_cliente(nome)
      if id_cliente is not None:
        removido = cadastro.pop(id_cliente)
        print(f"Cliente '{removido[0]}' e seus veículos foram removidos.")
      else:
        print("Cliente não encontrado.")
    elif numero == "6":
      print("Voltando ao menu principal")
      break
    else:
      print("Opção Inválida.")      

#menu Veículos:
def menu_veiculos():
  while True:
    print(">>> Gerenciamento de Veículos <<<")
    print("1. Cadastro de Veículo")
    print("2. Consulta de Veículo")
    print("3. Alteração de Veículo")
    print("4. Remoção de Veículo")
    print("5. Voltar ao menu principal")
    numero=input("Escolha uma das opções: \n").strip()
    if numero=="1": #CADASTRO DO VEÍCULO
      nome = validacao ("Nome do proprietário:")
      id_cliente = buscar_cliente(nome)
      if id_cliente is not None:
        placa= validacao("Placa do veículo:").upper()
        cliente_exite,placa_existe =buscar_veiculo(placa)
        if cliente_exite is not None:
          print("Esta placa já está cadastrada no sistema!")
        else:
          marca= validacao ("Marca/Modelo do veículo:")
          cadastro[id_cliente][1].append([placa,marca])
          ordenar_veiculos(cadastro[id_cliente][1])
          print(f"Veículo {placa} vinculado ao cliente {cadastro[id_cliente][0]}.")
      else:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
    elif numero=="2": #CONSULTA DO VEÍCULO
      placa= validacao("Informe a placa que procura:")
      id_cliente,id_placa=buscar_veiculo(placa)
      if id_cliente is not None:
        cliente = cadastro[id_cliente]
        veiculo=cliente[1][id_placa]
        print("\n ****** VEÍCULO ENCONTRADO ******")
        print(f"Placa: {veiculo[0]}")
        print(f"Marca/Modelo: {veiculo[1]}")
        print(f"Proprietário: {cliente[0]}")
      else:
        print("Veículo não encontrado.")
    elif numero=="3": #ALTERAÇÃO DO VEÍCULO
      placa=validacao("Informe a placa do veículo que deseja alterar:")
      id_cliente,id_placa=buscar_veiculo(placa)
      if id_cliente is not None:
        nova_placa=validacao("Nova Placa:").upper()
        nova_marca=validacao("Nova Marca/Modelo:")
        cliente_exite,placa_existe=buscar_veiculo(nova_placa)
        if cliente_exite is not None and nova_placa.lower() != placa.lower():
          print("Essa placa já existe no sistema")
        else:
          cadastro[id_cliente][1][id_placa]=[nova_placa,nova_marca]
          ordenar_veiculos(cadastro[id_cliente][1])
          print("Dados do veículo atualizados.")
      else:
        print("Veículo não encontrado.")
    elif numero=="4": #REMOÇÃO DO VEÍCULO
      placa=validacao("Informe a placa que deseja remover:")
      id_cliente,id_placa=buscar_veiculo(placa)
      if id_cliente is not None:
        veiculo_removido=cadastro[id_cliente][1].pop(id_placa)
        print(f"Veículo de placa {veiculo_removido[0]} removido com sucesso.")
      else:
        print("Veículo não encontrado")
    elif numero=="5":
      print("Voltando ao menu principal")
      break
    else:
      print("Escolha uma opção válida")  

#Menu principal
def menu_principal():
  while True:
    print("\n" + "*" * 30)
    print("  GERENCIAMENTO DA OFICINA  ")
    print("*" * 30)
    print("1. Gerenciamento de Clientes")
    print("2. Gerenciamento de Veículos")
    print("0. Sair")
    print("*" * 30)
    numero=input("Escolha uma das opções: \n").strip()
    if numero=="1":
      menu_clientes()
    elif numero=="2":
      menu_veiculos()
    elif numero=="0":
      print("Saindo...")
      break
    else:
      print("Escolha uma opção válida")
menu_principal()