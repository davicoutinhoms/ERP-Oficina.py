from models.ordem_servico import OrdemServico
from estruturas.fila_prioridade import FilaPrioridade


os1 = OrdemServico(10, "João", "Honda Civic", "Troca de óleo", 2)
os2 = OrdemServico(15, "Maria", "Chevrolet Onix", "Motor não liga", 5)
os3 = OrdemServico(22, "Pedro", "Volkswagen Gol", "Problema nos freios", 4)
os4 = OrdemServico(30, "Lucas", "Fiat Argo", "Revisão preventiva", 1)


fila = FilaPrioridade()

fila.inserir(os1)
fila.inserir(os2)
fila.inserir(os3)
fila.inserir(os4)


print("ORDEM DE PROCESSAMENTO")

while not fila.esta_vazia():

    ordem = fila.remover_maior_prioridade()

    print(
        "OS",
        ordem.codigo,
        "- Prioridade:",
        ordem.prioridade
    )