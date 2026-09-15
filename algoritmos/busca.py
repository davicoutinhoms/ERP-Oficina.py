def buscar_ordem_por_codigo(ordens, codigo):
    for i in range(len(ordens)):
        if ordens[i].codigo == codigo:
            return i

    return -1

def busca_binaria_ordem(ordens_ordenadas, codigo):
    inicio = 0
    fim = len(ordens_ordenadas) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if ordens_ordenadas[meio].codigo == codigo:
            return ordens_ordenadas[meio]
        elif ordens_ordenadas[meio].codigo < codigo:
            inicio = meio + 1

        else:
            fim = meio - 1
    return None