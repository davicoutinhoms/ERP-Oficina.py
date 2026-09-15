from models.ordem_servico import OrdemServico
from algoritmos.busca import buscar_ordem_por_codigo, busca_binaria_ordem
from algoritmos.ordenacao import ordenar_por_codigo


os1 = OrdemServico(30, "João", "Civic", "Troca de óleo", 2)
os2 = OrdemServico(10, "Maria", "Onix", "Motor não liga", 5)
os3 = OrdemServico(20, "Pedro", "Gol", "Problema nos freios", 4)

ordens = [os1, os2, os3]


print("=== BUSCA LINEAR ===")

indice = buscar_ordem_por_codigo(ordens, 20)

if indice != -1:
    print("Encontrada:", ordens[indice].codigo)
    print("Cliente:", ordens[indice].cliente)
else:
    print("Ordem não encontrada.")


print("\n=== BUSCA BINÁRIA ===")

ordens_ordenadas = ordenar_por_codigo(ordens)

print("Ordem dos códigos:")
for ordem in ordens_ordenadas:
    print(ordem.codigo)

resultado = busca_binaria_ordem(ordens_ordenadas, 20)

if resultado is not None:
    print("\nEncontrada:", resultado.codigo)
    print("Cliente:", resultado.cliente)
else:
    print("Ordem não encontrada.")